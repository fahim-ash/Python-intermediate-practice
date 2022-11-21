# * for packing tuple
# ** for packing dict
def summ(*args):
    return sum(args)

print(summ(2,1,5,0,9))

def fun(a, b, c):
    print(a, b, c)
 
# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)