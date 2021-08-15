from sqlalchemy import Integer, Column, String, Enum
from app import db
import enum
import datetime

from .interface import AssetInterface


#Enums
class Operation(enum.Enum):
    comprar=1
    vender=2
class TickerType(enum.Enum):
    stock=1
    cripto=2
    fii=3
    renda_fixa=4
    fundos=5

class Strategy(enum.Enum):
    DIVIDENDO=1
    FII=2
    VALUE=3
    SMALLCAPS=4
    ESPECULACAO=5
    DOLAR=6
    RESERVA=7
    CRYPTO=8
    EMERGENCIA=9

class Exchange(enum.Enum):
    INTER=1
    CLEAR=2
    MODAL_MAIS=3
    LOCALBITCOIN=4
    NUBANK=5
    BINANCE=6

class House(enum.Enum):
    VG=1
    SUNO=2
    EMPIRICUS=3
    MODAL_MAIS=4
    PESSOAL=5


class Asset(db.Model):
    
    __tablename__ = "assets"

    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(255))
    ticker = db.Column(db.String(255))
    ticker_type = db.Column(db.String(255))
    strategy = db.Column(db.String(255))
    amount = db.Column(db.Float)
    entry_price = db.Column(db.Float)
    entry_date = db.Column(db.DateTime, default=datetime.datetime.now)
    currency = db.Column(db.String(20))
    exchange = db.Column(db.String(255))
    house = db.Column(db.String(255))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, changes: AssetInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        db.session.commit()
        return self
    
    def __repr__(self):
        return f"{self.ticker}"

    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)
 
