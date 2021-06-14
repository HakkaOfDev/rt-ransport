from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from api.data.platforms.PLD import PLD
from api.handlers.Handler import Base


class Operator(Base): # ORM Operator
    __tablename__ = 'operators'
    operator_id = Column('operator_id', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(15))
    id_pld = Column('id_pld', Integer, ForeignKey(PLD.id_pld))
    lastname = Column('lastname', VARCHAR(50))
    firstname = Column('firstname', VARCHAR(50))
    login = Column('login', VARCHAR(15))
    password = Column('password', VARCHAR(15))
    role = Column('role', VARCHAR(15))

    def __init__(self, ref, id_pld, lastname, firstname, login, password, role): # constructeur
        self.ref = ref
        self.id_pld = id_pld
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password
        self.role = role

    def as_dict(self): # return all values in dict
        return {
            "ref": self.ref,
            "id_pld": self.id_pld,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "login": self.login,
            "password": self.password,
            "role": self.role,
        }
