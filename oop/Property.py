#by using property we dont need to use the object
# we can just refere to it

class User:
    def __init__(self,name,surename):
        self.name=name
        self.surename=surename
        
    @property           #its a getter
    def fullname(self):
        return self.name+" "+self.surename

    @fullname.setter
    def fullname(self,name,surename):
        self.name=name
        self.surename=surename
        return self.name+" "+self.surename



User1=User("bakdul","patoari")
print(User1.fullname)
User1.name="kashem"
User1.surename="molla"
print(User1.fullname)
