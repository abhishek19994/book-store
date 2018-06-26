__author__ = 'jc'


class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExistsError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass

class UserAlreadyExist(UserError):
    pass

class InvalidEmail(UserError):
    pass