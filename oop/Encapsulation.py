# dekhanor jnno. shb e over ride kora jay
# protected,private
# protected start with one _ ,private with two __
# only child class should be over ride the protected class

class Car():
    __taka="money"
    def __init__(self,year,make):
        self._year=year
        self.__make=make

    def hello(self):
        return ("hello" +" "+  Car.__taka)
        
class Rickshaw(Car):
    def __init__(self,year,make):
        super().__init__(year,make)

    def call_pirvate(self):
        print(self.__make)


Car1=Car(2019,"toyota")

print(Car1.hello())


