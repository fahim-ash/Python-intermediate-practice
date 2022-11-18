#testing abstraction
from abc import ABC,abstractmethod,abstractproperty
class Car(ABC):
    def __init__(self,year,make):
        self.year=year
        self.make=make
    @abstractmethod
    def drive(self):
        return (f"{self.make} is running since {self.year}")

class Vehicle(Car):
    
    def drive(self):
        pass

        
car_1=Vehicle("1996","BMW")
print(car_1.make)
