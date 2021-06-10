from datetime import date

from sqlalchemy import Column, ForeignKey, Date

from api import Base
from api import PLR
from api import Parcel


class Transmit(Base):
    __tablename__ = 'transmit'
    plr = Column('id_plr', ForeignKey(PLR.id_plr), primary_key=True)
    dest_plr = Column('dest_plr', ForeignKey(PLR.id_plr), primary_key=True)
    parcel = Column('parcel', ForeignKey(Parcel.id_parcel), primary_key=True)
    send_date = Column('send_date', Date)
    reception_date = Column('reception_date', Date)

    def __init__(self, parcel, plr, dest_plr, send_date: date, reception_date: date):
        self.parcel = parcel
        self.dest_plr = dest_plr
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
