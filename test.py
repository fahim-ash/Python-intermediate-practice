class Car():
    #constructor
    def __init__ (self,make,year):
        self.make=make
        self.year=year

    #method
    def run(self):
        print(f"this {self.make} is rinning")


car1=Car("Toyota",2015)
car2=Car("BMW",2015)

car1.run()
car2.run()