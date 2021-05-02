from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, BOOLEAN

from handlers.Handler import Base


class Parcel(Base):
    __tablename__ = 'parcels'
    id_parcel = Column('id_parcel', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(30))
    type = Column('type', VARCHAR(20))
    height = Column('height', NUMERIC)
    width = Column('width', NUMERIC)
    depth = Column('depth', NUMERIC)
    weight = Column('weight', NUMERIC)
    packaging = Column('packaging', VARCHAR(20))
    assured = Column('assured', Integer)
    fragile = Column('fragile', BOOLEAN)

    def __init__(self, ref, type, height, width, depth, weight, packaging, assured, fragile):
        self.ref = ref
        self.type = type
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.packaging = packaging
        self.assured = assured
        self.fragile = fragile
