from db import db

class WeatherModel(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    rainProbability = db.Column(db.Integer, nullable=False)
    rainPrecipitation = db.Column(db.Integer, nullable=False)
    minTemperature = db.Column(db.Integer, nullable=False)
    maxTemperature = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('city', 'date', name='cityDate'),
    )

    def __init__(self, city, date, state, country, rainProbability, rainPrecipitation, minTemperature, maxTemperature):
        self.city = city
        self.date = date
        self.state = state
        self.country = country
        self.rainProbability = rainProbability
        self.rainPrecipitation = rainPrecipitation
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature

    def __repr__(self, ):
        return f'WeatherModel(city={self.city}, state={self.state}, country={self.country}, date={self.date})'

    def json(self, ):
        return {
            'city': self.city,
            'date': self.date,
            'state': self.state,
            'country': self.country,
            'rainProbability': self.rainProbability,
            'rainPrecipitation': self.rainPrecipitation,
            'minTemperature': self.minTemperature,
            'maxTemperature': self.maxTemperature
        }
    
    @classmethod
    def findById(cls, id):
        print(id)
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def findByCity(cls, city):
        return cls.query.filter_by(city=city).first()
    
    @classmethod
    def findAll(cls):
        return cls.query.all()
    
    def saveToDb(self):
        db.session.add(self)
        db.session.commit()
    
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()