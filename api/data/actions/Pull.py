from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, DateTime

from api.data.platforms.PLD import PLD
from api.data.workers.Customer import Customer
from api.handlers.Handler import Base


class Pull(Base): # ORM Base
    __tablename__ = 'pull'
    id = Column('pull_id', Integer, primary_key=True)
    parcel = Column('parcel', VARCHAR(50))
    pld = Column('pld', Integer, ForeignKey(PLD.id_pld))
    customer = Column('customer', Integer, ForeignKey(Customer.id_customer))
    pull_date = Column('pull_date', DateTime)

    def __init__(self, parcel, pld, customer, pull_date): # constructeur
        self.parcel = parcel
        self.pld = pld
        self.customer = customer
        self.pull_date = pull_date

    def as_dict(self): # return all values in dict
        return {
            "parcel": self.parcel,
            "pld": self.pld,
            "customer": self.customer,
            "send_date": self.send_date,
            "pull_date": self.pull_date,
        }
