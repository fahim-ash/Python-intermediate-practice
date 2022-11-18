# map() => map(function,list)


#input
#a,b,c=map(int,input().split())

array=[3,1,5,0,10,100]
def add(x):
    return x if x%2==0 else "nooo"  

print((list(map(add,array))))