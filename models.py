from peewee import *

DB_NAME = "meetup.db"

class Database(object):
    instance = SqliteDatabase(DB_NAME)
    instance.connect()

    @staticmethod
    def init():
        Database.instance.create_tables([Group,Floorplan,User])

class BaseModel(Model):
    class Meta:
        database = Database.instance

class Group(BaseModel):
    id = PrimaryKeyField(null = False)
    name = CharField()
    password = CharField()

class Floorplan(BaseModel):
    id = PrimaryKeyField(null = False)
    filename = CharField(unique = True)
    group = ForeignKeyField(Group, related_name="floorplans")

class User(BaseModel):
    id = PrimaryKeyField(null = False)
    name = CharField()
    colour = CharField(max_length=6)
    group = ForeignKeyField(Group, related_name="users")
