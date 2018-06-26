from src.common.database import Database
Database.initialize()

import uuid
from datetime import datetime
class Book(object):
    def __init__(self,title,category_id,author,year,link,description="",updated_time=None,_id=None):
        self.title=title
        self.author=author
        self.year=year
        self.category_id=category_id
        self.updated_time =datetime.utcnow() if updated_time is None else updated_time
        self.description=description
        self.link=link
        self._id=uuid.uuid4().hex if _id is None else _id
    @classmethod
    def find_by_author(cls,author):
        return [cls(**i) for i in Database.find('books',{"author":author})]
    def json(self):
        return {"category_id":self.category_id,"link":self.link,"title":self.title, "author":self.author,"year":self.year,"_id":self._id,"updated_time":self.updated_time,"description":self.description}
    def save(self):
        Database.insert('books',self.json())
    @classmethod
    def find_by_id(cls,id):
        return cls(**Database.find_one('books',{"_id":id}))
    @classmethod
    def find(cls):
        return [cls(**i) for i in Database.find('books',{})]
    @classmethod
    def savfav(cls,id):
        Database.insert('favourite',Book.find_by_id(id).json())
    @classmethod
    def query(cls):
        return [cls(**i) for i in Database.find('favourite',{})]
    @classmethod
    def by_category_id(cls,id):
        return [cls(**i) for i in Database.find('books',{"category_id":id})]
