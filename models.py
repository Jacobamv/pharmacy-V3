from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db
        
        
        
class Network(BaseModel):
    id = AutoField()
    name = CharField()

class Pharmacy(BaseModel):
    id = AutoField()
    network = ForeignKeyField(Network, related_name = 'pharmacies')
    name = CharField()
    

class Users(BaseModel):
    id = AutoField()
    username = CharField()
    password = CharField()
    role = CharField()
    fio = CharField()
    network = ForeignKeyField(Network, related_name = 'users')

# na-sa
class Drugs(BaseModel):
    id = AutoField()
    barcode = IntegerField()
    name = CharField()
    price = FloatField()
    quantity = FloatField()
    shelf_life = TimeField()
    network = ForeignKeyField(Network, related_name= 'drugs')
    
if __name__ == '__main__':
    Users.create_table()
    Network.create_table()
    Pharmacy.create_table()
    Drugs.create_table()