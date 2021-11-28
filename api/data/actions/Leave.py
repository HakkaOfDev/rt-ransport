from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, DateTime

from api.data.platforms.PLD import PLD
from api.handlers.Handler import Base


class Leave(Base): # ORM Leave
    __tablename__ = 'leave'
    id = Column('leave_id', Integer, primary_key=True)
    parcel = Column('parcel', VARCHAR(50))
    pld = Column('pld', Integer, ForeignKey(PLD.id_pld))
    supplier = Column('supplier', VARCHAR(15))
    deposit_date = Column('deposit_date', DateTime)

    def __init__(self, parcel, pld, supplier, deposit_date): # constructeur
        self.parcel = parcel
        self.pld = pld
        self.supplier = supplier
        self.deposit_date = deposit_date

    def as_dict(self): # return all values in dict
        return {
            "parcel": self.parcel,
            "pld": self.pld,
            "supplier": self.supplier,
            "deposit_date": self.deposit_date,
        }
