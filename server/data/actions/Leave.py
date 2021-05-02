from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from data.Parcel import Parcel
from data.platforms.PLD import PLD
from data.workers.Supplier import Supplier
from handlers.Handler import Base


class Leave(Base):
    __tablename__ = 'leave'
    parcel = Column('parcel', ForeignKey(Parcel.id_parcel), primary_key=True)
    pld = Column('pld', ForeignKey(PLD.id_pld), primary_key=True)
    supplier = Column('supplier', ForeignKey(Supplier.id_supplier), primary_key=True)
    deposit_date = Column('deposit_date', Date)

    def __init__(self, parcel, pld, supplier, deposit_date: date):
        self.parcel = parcel
        self.pld = pld
        self.supplier = supplier
        self.deposit_date = deposit_date
