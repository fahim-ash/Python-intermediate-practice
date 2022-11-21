# higher order function -> adds additional functioanlity

def smart_divide(func):
    def inner(a, b):
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(abs(a/b))

x=int(input())
y=int(input())
divide(x,y)

#example 
"""
def validity(func):
    def check(x):
        if x=="fahim":
            print("found")
            return func(True)
        return False
    return check

@validity
def divide(x):
    print("running")

x=input()
divide(x)
"""