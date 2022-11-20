#---- multiple parents
#---- MRO (method resoulation order), need when multiple superclass
#----MRO -DLR algorithm- Use DFS when not super()
#---- __mro__()
#---- kalke practice kora lagbe -> with the diamond kanye west trick


#testing multiple inheritance
class Jayz:
    def __init__(self,song): 
        self.song=song

class Eminem(Jayz):
    def __init__(self,song): 
        super().__init__(song)

    def sing(self):
        print("its emninms")

    def album(self):
        print("8 mile")

class Kanye(Jayz):
    def __init__(self,song):
        super().__init__(song)

    def sing(self):
        print("its kanyes")

class Drake(Eminem,Kanye): #always get the 1st one
    def __init__(self,song):
        super().__init__(song)

r=Drake("idk")
# print(Drake.__mro__)
r.album()
r.sing()



