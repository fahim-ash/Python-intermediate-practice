#lambda :anonymus function 
# use for single line statements 
# need better code example

#basic
count=lambda x: x+5
# print(count(15))

#with filter and map
word=[15,2,1,0,9,10]
smaller=list(filter(lambda x:x<5,word))
adder=list(map(lambda x:x+5,word))


# lambda to sort list
sorted_list = sorted(word, key=lambda x: x) # works


#dict sort
hash = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

sorter=sorted(hash, key=lambda x: x["name"])

print(sorter)