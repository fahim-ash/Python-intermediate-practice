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
    # def show(self):
    #     print(self.property) -> will be problem for multiple inheritance
    def __init__(self,property):
        super().__init__(property)
        self.property=property
        
    def show(self):
        print(self.property)

a=Son(".......................")
a.show()
a.grandfather("kashem")

"""
main reason to use super()
The reason we use super is so that child classes that may be using cooperative 
multiple inheritance will call the correct next parent class function
in the Method Resolution Order (MRO). Without super, 
you are limited in your ability to use multiple inheritance 
because you hard-wire the next parent's call: Base.

"""

