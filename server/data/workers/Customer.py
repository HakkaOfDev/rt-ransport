from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from data.City import City
from handlers.Handler import Base


class Customer(Base):
    __tablename__ = 'customers'
    id = Column('id', Integer, primary_key=True)
    id_city = Column('id_city', Integer, ForeignKey(City.id_city))
    ref = Column('ref', VARCHAR(15))
    lastname = Column('lastname', VARCHAR(30))
    firstname = Column('firstname', VARCHAR(30))
    address = Column('address', VARCHAR(100))
    login = Column('login', VARCHAR(15))
    password = Column("password", VARCHAR(15))

    def __init__(self, id_city, ref, lastname, firstname, address, login, password):
        self.id_city = id_city
        self.ref = ref
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
        self.login = login
        self.password = password

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
