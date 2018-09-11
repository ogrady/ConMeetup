from peewee import *

DB_NAME = "meetup.db"
UPLOAD_DIR = "uploads/"

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
    filename = CharField()
    group = ForeignKeyField(Group, related_name="floorplans")

    @property
    def filepath(self):
        return "%s/%s_%s" % (UPLOAD_DIR, self.id, self.filename)
    

class User(BaseModel):
    id = PrimaryKeyField(null = False)
    name = CharField()
    colour = CharField(max_length=6)
    group = ForeignKeyField(Group, related_name="users")
