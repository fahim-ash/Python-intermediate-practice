# one liner way to iterate over list

# make a list with odd numbers from 0-> 100

oddList=[i for i in range (100) if i%2==1]
allList=[i for i in range(20)]
def odd(x):
    return x if x%2==0 else "not odd"

z=[odd(i) for i in allList]
print(z)