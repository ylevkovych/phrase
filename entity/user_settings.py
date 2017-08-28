
class UserSettings():
    
    ''' User settings representation '''

    def __init__(self, _id=-1, userId=-1, roleId=-1, language1Id=-1, language2Id=-1):
        self._id = _id
        self.userId = userId
        self.roleId = roleId
        self.language1Id = language1Id
        self.language2Id = language2Id

    