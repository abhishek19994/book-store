class bookerror(Exception):
    def __init__(self,message):
        self.message=message
class AlreadyExistsError(bookerror):
    pass