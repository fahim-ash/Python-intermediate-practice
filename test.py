# import itertools
# z=list(itertools.permutations([1, 2, 3]))
# print(z)
# z=[1,3,1,2,4]
# s={}
# for i in range(len(z)):
#     s[i]=z[i]
    
# print(s)
from itertools import permutations
arr=[4,4,2,4,3]
z=[str(i) for i in arr]

res=[]

for i in range(len(z)):
    tmp=[str(z[i])]
     
    for j in range(i+1,len(z)):
        if (z[i]!=z[j]):
            mm=(tmp+z[j:j+2])
            if len(mm)==3:

                word="".join(mm)
                res.append(word)


        # if (z[j] not in tmp):
        #     tmp.append(str(z[j]))

        #     if len(tmp)==3:
        #         word="".join(tmp)
        #         res.append(res)
        #         tmp.pop()
    
        
print(res)
        


