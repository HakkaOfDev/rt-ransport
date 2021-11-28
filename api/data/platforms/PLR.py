from sqlalchemy import Column, Integer, VARCHAR

from api.handlers.Handler import Base


class PLR(Base): # ORM PLR
    __tablename__ = 'plr'
    id_plr = Column('id_plr', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(6))
    name = Column('name', VARCHAR(50))

    def __init__(self, ref, name): # constructeur
        self.ref = ref
        self.name = name

    def as_dict(self): # return all values in dict
        return {
            "id_plr": self.id_pld,
            "ref": self.ref,
            "name": self.name
        }
