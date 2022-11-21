# unlimited regx -> cant remember all
# find matchs,characters and numbers
# common operations -> findall(), search(), sub() ,split()
# ^ = starts with 
# $ = ends with 
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
z = re.sub("\s", "9", txt)
p = re.split("\s", txt)
print(x)
print(z)
print(p)

#unicode 

z="hello world"
res=z.encode("utf-16")
print(res.decode("utf-16"))

# utf-8 -> 1,2,3,4 bytes
# utf-16 -> 2 or 4 bytes