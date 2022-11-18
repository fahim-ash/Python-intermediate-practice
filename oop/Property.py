#still have to clarify and write more code

class User:
    def __init__(self,name,surename):
        self.name=name
        self.surename=surename
    @property
    def fullname(self):
        return self.name+" "+self.surename



User1=User("bakdul","patoari")
User1.name="kashem"
print(User1.fullname)