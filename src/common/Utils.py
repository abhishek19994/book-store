
from passlib.hash import pbkdf2_sha512
import re

class Utils(object):
    @staticmethod
    def return_hash(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed):
        return pbkdf2_sha512.verify(password, hashed)
    @staticmethod
    def valid_email(email):
        matcher=re.compile('^[\w-]+@+([\w-]+\.)+[\w]+$')
        return True if matcher.match(email) else False