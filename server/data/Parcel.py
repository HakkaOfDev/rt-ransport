from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, BOOLEAN, ForeignKey

from data.workers.Customer import Customer
from data.workers.Operator import Operator
from data.workers.Supplier import Supplier
from handlers.Handler import Base


class Parcel(Base):
    __tablename__ = 'parcels'
    parcel_id = Column('id_parcel', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(30))
    operator_ref = Column('operator_ref', VARCHAR(15))
    customer_ref = Column('customer_ref', VARCHAR(15))
    supplier_ref = Column('supplier_ref', VARCHAR(15))
    type = Column('type', VARCHAR(20))
    height = Column('height', NUMERIC)
    width = Column('width', NUMERIC)
    depth = Column('depth', NUMERIC)
    weight = Column('weight', NUMERIC)
    packaging = Column('packaging', VARCHAR(20))
    assured = Column('assured', Integer)
    fragile = Column('fragile', BOOLEAN)

    def __init__(self, ref, operator_ref, customer_ref, supplier_ref, type, height, width, depth, weight, packaging, assured, fragile):
        self.ref = ref
        self.operator_ref = operator_ref
        self.customer_ref = customer_ref
        self.supplier_ref = supplier_ref
        self.type = type
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.packaging = packaging
        self.assured = assured
        self.fragile = fragile
