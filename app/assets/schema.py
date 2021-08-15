from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from .model import Asset



class AssetSchema(SQLAlchemySchema):
    class Meta:
        model = Asset
        include_relationships = True
    id          = auto_field(attribute="id")
    operation   = auto_field(attribute="operation")
    ticker      = auto_field(attribute="ticker")
    ticker_type = auto_field(attribute="ticker_type")
    strategy    = auto_field(attribute="strategy")
    amount      = auto_field(attribute="amount")
    entry_price = auto_field(attribute="entry_price")
    entry_date  = auto_field(attribute="entry_date")
    currency    = auto_field(attribute="currency")
    exchange    = auto_field(attribute="exchange")
    house       = auto_field(attribute="house")