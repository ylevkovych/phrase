
class User():
    
    ''' User representation '''

    def __init__(self, _id=-1, username="", password="", email=""):
        self._id=_id
        self.username=username
        self.password=password
        self.email=email

    def __str__(self):
        return "id: "+str(self._id)+"; username: "+self.username+"; password: "+self.password+"; email: "+self.email

    def serialize(self):
        return {"id": str(self._id)}