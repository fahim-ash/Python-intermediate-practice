class Car():
    x=100
    def __init__(self,year,make):
        self.year=year
        self.make=make
        
    @classmethod
    def sum(cls):
      return cls.


Car1=Car(200,"toyota")

print(Car.sum)