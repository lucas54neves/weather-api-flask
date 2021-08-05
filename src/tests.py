import unittest
import json
import datetime

from ma import ma
from db import db
from app import app, api

class TestWeather(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.init_app(app)
        ma.init_app(app)
    
    def testCidades(self):
        response = self.app.get('/cidades')
        self.assertEqual(200, response.status_code)
    
    def testCidade(self):
        response = self.app.get('/cidades')
        cities = json.loads(response.get_data(as_text=True))
        citiesById = [city for city in cities if city['cityId'] == 3477]
        if (len(citiesById) == 0):
            response = self.app.get('/cidade?id=3477')
            self.assertEqual(201, response.status_code)
            response = self.app.get('/cidades')
            cities = json.loads(response.get_data(as_text=True))
            self.assertGreater(len(cities), 0)
        else:
            self.assertEqual(200, response.status_code)
    
    def testAnalise(self):
        response = self.app.get('/cidades')
        cities = json.loads(response.get_data(as_text=True))
        city3754 = [city for city in cities if city['cityId'] == 3754]
        if (len(city3754) == 0):
            response = self.app.get('/cidade?id=3754')
            self.assertEqual(201, response.status_code)
        city3654 = [city for city in cities if city['cityId'] == 3654]
        if (len(city3654) == 0):
            response = self.app.get('/cidade?id=3654')
            self.assertEqual(201, response.status_code)
        city3604 = [city for city in cities if city['cityId'] == 3604]
        if (len(city3604) == 0):
            response = self.app.get('/cidade?id=3604')
            self.assertEqual(201, response.status_code)
        today = {
            'day': datetime.datetime.today().day,
            'month': datetime.datetime.today().month,
            'year': datetime.datetime.today().year
        }
        data_inicial = f'{today["year"]}-{today["month"]}-{today["day"]}'
        data_final = f'{today["year"]}-{today["month"]+1}-{today["day"]}'
        response = self.app.get(f'/analise?data_inicial={data_inicial}&data_final={data_final}')
        data = json.loads(response.get_data(as_text=True))
        self.assertNotEqual(data['cityWithHigherTemperature'], {})
        self.assertNotEqual(data['precipitationAverage'], {})
            
if __name__ == '__main__':
    unittest.main()