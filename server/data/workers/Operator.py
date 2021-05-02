from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from data.platforms.PLD import PLD
from handlers.Handler import Base


class Operator(Base):
    __tablename__ = 'operators'
    id = Column('id', Integer, primary_key=True)
    id_pld = Column('id_pld', Integer, ForeignKey(PLD.id_pld))
    lastname = Column('lastname', VARCHAR(50))
    firstname = Column('firstname', VARCHAR(50))
    login = Column('login', VARCHAR(15))
    password = Column('password', VARCHAR(15))

    def __init__(self, id_pld, lastname, firstname, login, password):
        self.id_pld = id_pld
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password
