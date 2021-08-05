from flask import request
from flask_restx import Resource, fields
import requests
import json
import datetime

from models.weather import WeatherModel
from schemas.weather import WeatherSchema

from server.instance import server

weatherNs = server.weatherNs

weatherSchema = WeatherSchema()
weatherListSchema = WeatherSchema(many=True)

class Weather(Resource):
    def get(self):
        try:
            cityId = request.args.get('id')

            token = 'b22460a8b91ac5f1d48f5b7029891b53'

            url = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{cityId}/days/15?token={token}'

            response = requests.request('GET', url)
            content = response.content.decode('utf-8')
            data = json.loads(content)

            city = data['name']
            state = data['state']
            country = data['country']

            dataByDate = [{
                'date': date['date'],
                'rainProbability': date['rain']['probability'],
                'rainPrecipitation': date['rain']['precipitation'],
                'minTemperature': date['temperature']['min'],
                'maxTemperature': date['temperature']['max'],
            } for date in data['data']]

            for data in dataByDate:
                dataToSave = {
                    'city': city,
                    'cityId': cityId,
                    'state': state,
                    'country': country,
                    'date': data['date'],
                    'rainProbability': data['rainProbability'],
                    'rainPrecipitation': data['rainPrecipitation'],
                    'minTemperature': data['minTemperature'],
                    'maxTemperature': data['maxTemperature'],
                }


                weatherData = weatherSchema.load(dataToSave)

                weatherData.saveToDb()

            return {'message': 'Dados coletados.'}, 201
        except:
            return {'message': 'Erro na coleta de dados.'}, 400

class WeatherList(Resource):
    def get(self):
        return weatherListSchema.dump(WeatherModel.findAll()), 200

class WeatherAnalysis(Resource):
    def get(self):
        beginString = request.args.get('data_inicial')
        endString = request.args.get('data_final')

        beginTimestamp = int(datetime.datetime.strptime(beginString, '%Y-%m-%d').strftime("%s"))
        endTimestamp = int(datetime.datetime.strptime(endString, '%Y-%m-%d').strftime("%s"))

        datas = weatherListSchema.dump(WeatherModel.findAll())

        cityWithHigherTemperature = -1

        precipitations = {}

        for data in datas:
            current = int(datetime.datetime.strptime(data['date'], '%Y-%m-%d').strftime("%s"))

            if current > beginTimestamp and current < endTimestamp:
                if cityWithHigherTemperature == -1:
                    cityWithHigherTemperature = data

                if data['maxTemperature'] > cityWithHigherTemperature['maxTemperature']:
                    cityWithHigherTemperature = data
                
                if precipitations.get(data['city']):
                    precipitations[data['city']].append(data['rainPrecipitation'])
                else:
                    precipitations[data['city']] = [data['rainPrecipitation']]
        
        if cityWithHigherTemperature == -1:
            cityWithHigherTemperature = {}
        
        precipitationAverage = {k:(sum(v) / len(v)) for (k, v) in precipitations.items()}
        
        return {'cityWithHigherTemperature': cityWithHigherTemperature, 'precipitationAverage': precipitationAverage}, 200