from sqlalchemy import Column, Integer, VARCHAR

from handlers.Handler import Base


class PLR(Base):
    __tablename__ = 'plr'
    id_plr = Column('id_plr', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(6))
    name = Column('name', VARCHAR(50))

    def __init__(self, ref, name):
        self.ref = ref
        self.name = name
