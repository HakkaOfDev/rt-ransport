from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from data.platforms.PLR import PLR
from handlers.Handler import Base


class PLD(Base):
    __tablename__ = 'pld'
    id_pld = Column('id_pld', Integer, primary_key=True)
    id_plr = Column('id_plr', Integer, ForeignKey(PLR.id_plr))
    ref = Column('ref', VARCHAR(6))
    name = Column('name', VARCHAR(50))

    def __init__(self, id_pld, id_plr, ref, name):
        self.id_pld = id_pld
        self.id_plr = id_plr
        self.ref = ref
        self.name = name
