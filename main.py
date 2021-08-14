from gevent.pywsgi import WSGIServer
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
import enum
import datetime

class DevConfig(object): 
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fQ3S83t56DGW@queshi-db:3306/queshi'

class Dev2Config(object): 
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fQ3S83t56DGW@localhost:3307/queshi'

app = Flask(__name__) 
app.config.from_object(Dev2Config)   
db = SQLAlchemy(app)

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

# Model
class Asset(db.Model):
    __tablename__ = "assets"
    id = db.Column(db.Integer, primary_key=True)
    operation =db.Column(db.String(20))
    ticker = db.Column(db.String(20))
    ticker_type =db.Column(db.String(20))
    strategy = db.Column(db.String(20))
    amount = db.Column(db.Float)
    entry_price = db.Column(db.Float)
    entry_date = db.Column(db.DateTime, default=datetime.datetime.now)
    currency = db.Column(db.String(20))
    exchange = db.Column(db.String(20))
    house =db.Column(db.String(20))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)
 

    def __repr__(self):
        return f"{self.id}"

db.create_all()

class AssetSchema(SQLAlchemySchema):
    class Meta:
        model = Asset
        sqla_session = db.session
        include_relationships = True
    id = auto_field()
    operation =   fields.String()
    ticker = auto_field()
    ticker_type =  fields.String()
    strategy =  fields.String()
    amount = auto_field()
    entry_price = auto_field()
    entry_date =auto_field()
    currency = auto_field()
    exchange = fields.String()
    house = fields.String()
 
@app.route('/',methods=['GET']) 
def root(): 
    return jsonify({'message':'Olá mundos'})  

@app.route('/assets', methods=['POST'])
def create_asset():
    data = request.get_json()
    asset_schema = AssetSchema()
    print("SALVANDO")
    print(data)
    asset = Asset(data)
    result = asset_schema.dump(asset.create())
    return make_response(jsonify({"asset": result}), 200)

@app.route('/assets/<id>', methods=['PUT'])
def update_asset_by_id(id):
    data = request.get_json()
    get_assets = Asset.query.get(id)
    if data.get('strategy'):
        get_assets.strategy = data['strategy']

    if data.get('house'):
        get_assets.house = data['house']

    if data.get('exchange'):
        get_assets.exchange = data['exchange']
        
    db.session.add(get_assets)
    db.session.commit()
    assets_schema = AssetSchema(only=['ticker', 'strategy', 'house','exchange'])
    asset = assets_schema.dump(get_assets)
    return make_response(jsonify({"asset": asset}))

@app.route('/assets/<id>', methods=['DELETE'])
def delete_asset_by_id(id):
    get_assets = Asset.query.get(id)
    db.session.delete(get_assets)
    db.session.commit()
    return make_response("", 204)

@app.route('/assets', methods=['GET'])
def get_assets():
    get_assets = Asset.query.all()
    print(get_assets)
    asset_schema = AssetSchema(many=True)
    assets = asset_schema.dump(get_assets)
    return make_response(jsonify({"assets": assets}))
 
@app.route('/assets/<id>', methods=['GET'])
def get_asssets_by_id(id):
    get_assets = Asset.query.get(id)
    asset_schema = AssetSchema()
    asset = asset_schema.dump(get_assets)    
    return make_response(jsonify({"asset": asset}))



if __name__ == '__main__': 
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever() 