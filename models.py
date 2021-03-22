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
    network = ForeignKeyField(Network, related_name = 'pharmacy')
    name = CharField()
    address = CharField()
 
class Department(BaseModel):
    id = AutoField()
    name = CharField()
    pharmacy = ForeignKeyField(Pharmacy, related_name = 'pharmacy')

class Cashier(BaseModel):
    id = AutoField()
    name = CharField()
    department = ForeignKeyField(Department, related_name = 'Department')

class Users(BaseModel):
    id = AutoField()
    username = CharField()
    password = CharField()
    role = CharField()
    fio = CharField()
    network = ForeignKeyField(Network, related_name = 'users')
    
if __name__ == '__main__':
    Users.create_table()
    Network.create_table()
    Pharmacy.create_table()