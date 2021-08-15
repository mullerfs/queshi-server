import os
from typing import List, Type


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "Thanos não fez nada errado"
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+os.getenv("DB_PASSWORD")+'@localhost:3307/queshi'



class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "Star Trek é melhor que StarGate")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+os.getenv("DB_PASSWORD")+'@queshi-db:3306/queshi'
    

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    ProductionConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
