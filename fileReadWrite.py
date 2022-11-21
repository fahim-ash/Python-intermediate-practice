f=open("./test.text","r") # returns a iterable of the file
print(f.read())
# for i in f:
#     print(i)

#f = open("test.txt", "w")
# f.write("Woops! I have deleted the content!")
#f.close()


with open('test.text', 'r') as f:
   data = f.read()
   print(data)