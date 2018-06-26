import uuid

from src.common.database import Database
Database.initialize()
class category(object):
    def __init__(self, name, _id=None):
        self.name = name
        self._id = uuid.uuid4().hex if _id is None else _id

    def save(self):
        Database.insert("collection",self.json())

    def json(self):
        return {"name": self.name, "_id": self._id}

    @classmethod
    def find_by_id(cls, id):
        return cls(**Database.find_one('collection', {"_id": id}))

    @classmethod
    def query(cls):
        return [cls(**i) for i in Database.find('collection', {})]
    @classmethod
    def by_name(cls,name):
        if Database.find_one('collection',{"name":name}):
            return cls(**Database.find_one('collection',{"name":name}))