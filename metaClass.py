"""
in python classes are actually object ...everything is object
supporse we create a class Car :it sends info to the meta class
and meta class creates a class object for it

"""

# creating class in weird way with type()
# type(name,base,attrs) -> name:name of class
#                       -> base: tuple of class(mainly for inheritance)
#                       -> attrs: dictionary containing attributes names and values
def show(self):
    self.z=100
    # print(self.z)


Test=type('Test',(),{"name":"kashem","show":show})

t=Test()
print(t.name)
t.name="moksed"
t.show()
print(t.z)

# creatng own meta class
# __new__ dunder method is called when something (object) is created
# by manupulating meta class we can create classes in our own way 
# (like with certain attributes)


class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        return type(class_name,bases,attrs)

class Dog(metaclass=Meta):
    x=5
    y=8 
    def hello(self):
        print("hello")

"""
As class is also an object: so it has object behaviors like:-

    you can assign it to a variable
    you can copy it
    you can add attributes to it
    you can pass it as a function parameter
"""