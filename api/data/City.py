from sqlalchemy import Column, Integer, VARCHAR, CHAR, Numeric, ForeignKey

from api.data.platforms.PLD import PLD
from api.handlers.Handler import Base


class City(Base): # ORM City
    __tablename__ = 'city'
    id_city = Column('id_city', Integer, primary_key=True)
    id_pld = Column('id_pld', Integer, ForeignKey(PLD.id_pld))
    name = Column('name', VARCHAR(50))
    postal_code = Column('postal_code', CHAR(5))
    insee_code = Column('insee_code', VARCHAR(5))
    gps_lat = Column('gps_lat', Numeric)
    gps_long = Column('gps_lng', Numeric)

    def __init__(self, id_city, id_pld, name, postal_code, insee_code, gps_lat, gps_long): # constructeur
        self.id_pld = id_pld
        self.id_city = id_city
        self.name = name
        self.insee_code = insee_code
        self.postal_code = postal_code
        self.gps_lat = gps_lat
        self.gps_long = gps_long

    def as_dict(self): # return all values in dict
        return {
            "id_city": self.id_city,
            "id_pld": self.id_pld,
            "name": self.name,
            "postal_code": self.postal_code,
            "insee_code": self.insee_code,
            "gps_lat": self.gps_lat,
            "gps_long": self.gps_long,
        }
