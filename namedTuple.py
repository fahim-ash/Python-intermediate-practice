# namedTuple is a class which returns iterables
# we can also create hashmap from the tuple
# as its a class we can add functionality with a subclass

from collections import namedtuple

testTuple=namedtuple('testTuple','x y z')
newTuple=testTuple(1, 2, 3)
# print(newTuple.x,newTuple.y,newTuple.z)

point=namedtuple("point",["a","b","c"])
pointTuple=point(1,2,3) # creating tuple like a class ..its a class :3
# print(type(pointTuple.a))
print(pointTuple[0]) # normal tuple behaviour
for i in pointTuple:
    print(i)


print(pointTuple._asdict()) # all the methods requirs _ as prefix
print(pointTuple._fields) # returns all keys

#also need to see DOC later

