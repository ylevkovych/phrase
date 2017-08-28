
class User():
    
    ''' User representation '''

    def __init__(self, _id=-1, username="", password="", email=""):
        self._id=_id
        self.username=username
        self.password=password
        self.email=email
        