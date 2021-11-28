from sqlalchemy import Column, Integer, VARCHAR, DateTime

from api.handlers.Handler import Base


class Transmit(Base): # ORM Transmit
    __tablename__ = 'transmit'
    id = Column('transmit_id', Integer, primary_key=True)
    plr = Column('id_plr', Integer)
    dest_plr = Column('dest_plr', Integer)
    parcel = Column('parcel', VARCHAR(50))
    send_date = Column('send_date', DateTime)
    reception_date = Column('reception_date', DateTime)

    def __init__(self, parcel, plr, dest_plr, send_date, reception_date): # constructeur
        self.parcel = parcel
        self.dest_plr = dest_plr
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date

    def as_dict(self): # return all values in dict
        return {
            "plr": self.plr,
            "dest_plr": self.dest_plr,
            "parcel": self.parcel,
            "send_date": self.send_date,
            "reception_date": self.reception_date,
        }
