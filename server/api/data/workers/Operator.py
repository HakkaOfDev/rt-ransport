from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from api.data.platforms.PLD import PLD
from api.handlers.Handler import Base


class Operator(Base, UserMixin):
    __tablename__ = 'operators'
    operator_id = Column('operator_id', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(15))
    id_pld = Column('id_pld', Integer, ForeignKey(PLD.id_pld))
    lastname = Column('lastname', VARCHAR(50))
    firstname = Column('firstname', VARCHAR(50))
    login = Column('login', VARCHAR(15))
    password = Column('password', VARCHAR(15))

    def __init__(self, ref, id_pld, lastname, firstname, login, password):
        self.ref = ref
        self.id_pld = id_pld
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}