from datetime import date
from sqlite3.dbapi2 import Date

from sqlalchemy import ForeignKey, Column, Boolean

from data.Parcel import Parcel
from data.platforms.PLD import PLD
from handlers.Handler import Base


class Send(Base):
    __tablename__ = 'send'
    parcel = Column('parcel', ForeignKey(Parcel.id_parcel), primary_key=True)
    pld = Column('pld', ForeignKey(PLD.id_pld), primary_key=True)
    plr = Column('plr', ForeignKey(PLD.id_plr), primary_key=True)
    send_date = Column('send_date', Date)
    reception_date = Column('reception_date', Date)
    pld_to_plr = Column('pld_to_plr', Boolean)

    def __init__(self, parcel, pld, plr, send_date: date, reception_date: date, pld_to_plr: bool):
        self.parcel = parcel
        self.pld = pld
        self.plr = plr
        self.send_date = send_date
        self.reception_date = reception_date
        self.pld_to_plr = pld_to_plr
