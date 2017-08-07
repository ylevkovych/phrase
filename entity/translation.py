class Translation():

    ''' Translation representation '''

    def __init__(self, _id=-1, user=-1, folder=-1, language_1=-1, language_2=-1, phrase_1="", phrase_2=""):
        self._id=_id
        self.user=user
        self.folder=folder
        self.language_1=language_1
        self.language_2=language_2
        self.phrase_1=phrase_1
        self.phrase_2=phrase_2