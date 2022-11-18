# dekhanor jnno. shb e over ride kora jay
#protected,private
# protected start with one _ ,private with two __
#only child class should be over ride the protected class

class Car():
    def __init__(self,year,make):
        self.__year=year
        self.__make=make
class Rickshaw(Car):
    def __init__(self,year,make):
        super().__init__(year,make)



Car1=Car(2019,"toyota")

print(Car1.__make)