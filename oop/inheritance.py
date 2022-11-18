#clear 
class Father:
    def __init__(self,property):
        self.property=property

    def grandfather(self,name):
        print(f"{name} its your shompotti")
    
class Son(Father):
    pass



Bokdul=Son("half property")
print(Bokdul.property)
Bokdul.grandfather("bokdul")


