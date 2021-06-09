from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from data.Parcel import Parcel
from data.platforms.PLD import PLD
from data.workers.Customer import Customer
from handlers.Handler import Base


class Pull(Base):
    __tablename__ = 'pull'
    parcel = Column('parcel', ForeignKey(Parcel.id_parcel), primary_key=True)
    pld = Column('pld', ForeignKey(PLD.id_pld), primary_key=True)
    customer = Column('customer', ForeignKey(Customer.id_customer), primary_key=True)
    pull_date = Column('pull_date', Date)

    def __init__(self, parcel, pld, customer, pull_date: date):
        self.parcel = parcel
        self.pld = pld
        self.customer = customer
        self.pull_date = pull_date