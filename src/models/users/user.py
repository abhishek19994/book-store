import uuid

from src.common.database import Database
import  src.models.users.errors as UserError

from src.common.Utils import Utils


Database.initialize()
class User(object):
    def __init__(self,email,password,_id=None):
        self.email=email
        self.password=password
        self._id=uuid.uuid4().hex if _id is None else _id
    def __repr__(self):
        return "<User {}>".format(self.email)
    @staticmethod
    def login_valid(email,password):
        data=Database.find_one("users",{"email":email})
        if data is  None:
            raise UserError.UserNotExistsError("User not exist")
        elif Utils.check_hashed_password(password,data['password']) is False:
            raise UserError.IncorrectPasswordError("Password is wrong")
        return True
    @staticmethod
    def register_user(email,password):
        data=Database.find_one('users',{"email":email})
        if data is not None:
            raise UserError.UserAlreadyExist("This User already exist")
        elif not Utils.valid_email(email):
            raise UserError.InvalidEmail("Invalid email")
        User(email,Utils.return_hash(password)).save()
        return True
    def save(self):
        Database.insert('users',self.json())
    def json(self):
        return {"email":self.email,"_id":self._id,"password":self.password}
    @classmethod
    def get_by_email(cls,email):
        return cls(**Database.find_one('users',{"email":email}))
