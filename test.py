#testing abstraction
#testing new change
from abc import ABC,abstractmethod,abstractproperty
class Car(ABC):
    def __init__(self,year,make):
        self.year=year
        self.make=make
    @abstractproperty # also @abstractmehtod 
    def drive(self):
        pass

class Vehicle(Car):
    @property
    def drive(self):
        return (f"{self.make} is running since {self.year}")
        

car_1=Vehicle("1996","BMW")
print(car_1.drive)
