#--------@classmethod---------#
# for the @classmethod we dont need to ceate an object
# for the @classmethod we have to use cls to take the argument
# takes the whole class as an argument so it has access in everything


#-------@staticmethod---------#
# same as classmethod, we dont need to create a object
# its just a regular function, but we chose to use it inside a class :)
# can only use the parameters we are passing// cant access population 

class population(object):
    population=50

    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self): #why cant we access this -_-
        return (f"{self.name} is {self.age} years old")
  
    @classmethod #gets all the class level attributes accesss
    def getPopulation(cls): # can use anything public in the class(specially methods)
        print(cls.population)
        return cls.population
        

    @staticmethod
    def isAdult(age):
        # print((population.info()))
        return age >=18 


        
person=population("moksed",30)
print(population.getPopulation())
print(population.isAdult(200))
print(person.info())


