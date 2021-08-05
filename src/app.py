from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from server.instance import server
from controllers.weather import Weather, WeatherList, WeatherAnalysis

api = server.api
app = server.app

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(Weather, '/cidade')
api.add_resource(WeatherList, '/cidades')
api.add_resource(WeatherAnalysis, '/analise')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()