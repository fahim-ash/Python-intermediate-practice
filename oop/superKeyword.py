#self represents the instance of the class. 
# By using the “self” we can access the attributes and methods of the class in python. 
# It binds the attributes with the given arguments. 
# The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.


#amra self use kori object er attributes,mehtod access korar jnno 
class Father(object):
    def __init__(self,property):
        self.property=property

    def grandfather(self,name):
        print(f"{name} its your shompotti")
    
class Son(Father):
    def __init__(self):
        super().__init__('yoo')
        print("super is working")


a=Son()
print(a.property)
a.grandfather("Bokdul")


