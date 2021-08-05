from ma import ma
from models.weather import WeatherModel

class WeatherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WeatherModel
        load_instance = True