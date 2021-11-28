from sqlalchemy import Column, Boolean, Integer, VARCHAR, DateTime

from api.handlers.Handler import Base


class Send(Base): # ORM Send
    __tablename__ = 'send'
    id = Column('send_id', Integer, primary_key=True)
    parcel = Column('parcel', VARCHAR(50))
    pld = Column('pld', Integer)
    plr = Column('plr', Integer)
    send_date = Column('send_date', DateTime)
    reception_date = Column('reception_date', DateTime)
    pld_to_plr = Column('pld_to_plr', Boolean)

    def __init__(self, parcel, pld, plr, send_date, reception_date, pld_to_plr: bool): # constructeur
        self.parcel = parcel
        self.pld = pld
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
        self.pld_to_plr = pld_to_plr

    def as_dict(self): # return all values in dict
        return {
            "parcel": self.parcel,
            "pld": self.pld,
            "plr": self.plr,
            "send_date": self.send_date,
            "reception_date": self.reception_date,
            "pld_to_plr": self.pld_to_plr,
        }



