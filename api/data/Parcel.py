from sqlalchemy import Column, Integer, VARCHAR, BOOLEAN

from api.handlers.Handler import Base


class Parcel(Base): # ORM Parcel
    __tablename__ = 'parcels'
    parcel_id = Column('id_parcel', Integer, primary_key=True)
    ref = Column('ref', VARCHAR(50))
    operator_ref = Column('operator_ref', VARCHAR(15))
    customer_ref = Column('customer_ref', VARCHAR(15))
    supplier_ref = Column('supplier_ref', VARCHAR(15))
    type = Column('type', VARCHAR(20))
    height = Column('height', Integer)
    width = Column('width', Integer)
    depth = Column('depth', Integer)
    weight = Column('weight', Integer)
    packaging = Column('packaging', VARCHAR(20))
    assured = Column('assured', BOOLEAN)
    fragile = Column('fragile', BOOLEAN)
    current = Column('current', VARCHAR(50))
    end_dest = Column('end_dest', VARCHAR(50))

    def __init__(self, ref, operator_ref, customer_ref, supplier_ref, type, height, width, depth, weight, packaging,
                 assured, fragile, current, end_dest): # constructeur
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
        self.current = current
        self.end_dest = end_dest

    def as_dict(self): # return all values in dict
        return {
            "ref": self.ref,
            "operator_ref": self.operator_ref,
            "customer_ref": self.customer_ref,
            "supplier_ref": self.supplier_ref,
            "type": self.type,
            "height": self.height,
            "width": self.width,
            "depth": self.depth,
            "weight": self.weight,
            "packaging": self.packaging,
            "assured": self.assured,
            "fragile": self.fragile,
            "current": self.current,
            "end_dest": self.end_dest,
        }
