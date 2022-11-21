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