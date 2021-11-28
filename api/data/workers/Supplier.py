from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from api.data.City import City
from api.handlers.Handler import Base


class Supplier(Base): # ORM Supplier
    __tablename__ = 'suppliers'
    id = Column('id', Integer, primary_key=True)
    id_city = Column('id_city', Integer, ForeignKey(City.id_city))
    ref = Column('ref', VARCHAR(15))
    name = Column('name', VARCHAR(30))
    address = Column('address', VARCHAR(100))
    login = Column('login', VARCHAR(15))
    password = Column("password", VARCHAR(15))
    role = Column("role", VARCHAR(15))

    def __init__(self, id_city, ref, name, address, login, password, role): # constructeur
        self.id_city = id_city
        self.ref = ref
        self.name = name
        self.address = address
        self.login = login
        self.password = password
        self.role = role

    def as_dict(self): # return all values in dict
        return {
            "id_city": self.id_city,
            "ref": self.ref,
            "name": self.name,
            "address": self.address,
            "login": self.login,
            "password": self.password,
            "role": self.role,
        }
