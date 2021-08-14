class Config(object): 
    pass 
 
class ProdConfig(Config): 
    pass 
 
class DevConfig(Config): 
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fQ3S83t56DGW@queshi-db:3306/queshi'

class Dev2Config(Config): 
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fQ3S83t56DGW@localhost:3307/queshi'
