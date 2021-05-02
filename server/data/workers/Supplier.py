from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from data.City import City
from handlers.Handler import Base


class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column('id', Integer, primary_key=True)
    id_city = Column('id_city', Integer, ForeignKey(City.id_city))
    ref = Column('ref', VARCHAR(15))
    name = Column('name', VARCHAR(30))
    address = Column('address', VARCHAR(100))
    login = Column('login', VARCHAR(15))
    password = Column("password", VARCHAR(15))

    def __init__(self, id_city, ref, name, address, login, password):
        self.id_city = id_city
        self.ref = ref
        self.name = name
        self.address = address
        self.login = login
        self.password = password
