import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    database = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.database = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def find(collection, data):
        return Database.database[collection].find(data)

    @staticmethod
    def find_one(collection, data):
        return Database.database[collection].find_one(data)

    @staticmethod
    def update(collection, data1, data2):
        return Database.database[collection].update(data1, data2, upsert=True)
    @staticmethod
    def remove(collection,data):
        Database.database[collection].remove(data)