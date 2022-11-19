# Magic or dunder methods: starts and ends with __middle__
# it isnt invoked by user ,it auto invokes in the background when we do some task 
# suppose __add__ auto invokes when + is used.
# print(dir(int)) --> prints all the magic or dunder methods
# 


class Person:
    def __init__(self,name,number):
        self.name=name
        self.number=number

    # def __repr__(self):
    #     return self.name
    def __call__(self,times):
        print(times)
        self.number*=times
        print(self.number)
    def __add__(self,n):
        print(self.number+n)
      
P=Person("moksed",2441139)
P(100) #automatically use __calls__ when detects 
P+100  #adds