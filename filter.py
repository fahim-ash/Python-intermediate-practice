# filter() => filter(function,iterable)
#it will return a list with the elements that passed the conditions
# we can use filter along with map
# filter returns a iterator
# it checks mainly true or false 

word=(1,2,3,4,5,6,7,8,9,10)

def add(x):
    return x+10
def check(y):
    return y%2
#can use list,tuple,set...ect
z=tuple(map(add,filter(check,word)))
print(type(z))
def smaller(x):

    return x>5
res=filter(smaller,word)
print(type(res))


