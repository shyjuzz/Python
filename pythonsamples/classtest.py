from types import SimpleNamespace as Obj

class ApplicationNameAnnotatorSvc:
    def __init__(self):
        self.model = Obj()
        self.model.word_list = []
        self.__dict__.update(self.model.__dict__)
    def api_add_words(self):
        self.word_list.append(Obj(word='account', datatype='entity', id='2635'))

    def tag(self):
        print(self.word_list)

def new_instance():
    return ApplicationNameAnnotatorSvc()
