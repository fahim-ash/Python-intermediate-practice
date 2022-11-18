
# Magic or dunder methods: starts and ends with __middle__
# it isnt invoked by user ,it auto invokdes in the background when we do some task 
# suppose __add__ auto invokes when + is used.
# print(dir(int)) --> prints all the magic or dunder methods
# 


class Person:
    def __init__(self,a):
        self.a=a
    def __mul__(self,b):
        self.a=self.a*b
    def __call__(self,y):
        print("you called",y)
yo=Person("ash")
yo()

