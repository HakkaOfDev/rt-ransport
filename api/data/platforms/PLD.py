from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from api.data.platforms.PLR import PLR
from api.handlers.Handler import Base


class PLD(Base): # ORM PLD
    __tablename__ = 'pld'
    id_pld = Column('id_pld', Integer, primary_key=True)
    id_plr = Column('id_plr', Integer, ForeignKey(PLR.id_plr))
    ref = Column('ref', VARCHAR(6))
    name = Column('name', VARCHAR(50))

    def __init__(self, id_pld, id_plr, ref, name): # constructeur
        self.id_pld = id_pld
        self.id_plr = id_plr
        self.ref = ref
        self.name = name

    def as_dict(self): # return all values in dict
        return {
            "id_pld": self.id_pld,
            "id_plr": self.id_plr,
            "ref": self.ref,
            "name": self.name
        }

