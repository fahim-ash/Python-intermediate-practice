"""
dic methods -> clear ()-empty dic
            ->  copy() - return copy of the dic
            ->  fromkeys() - return dic with specified keys and value
            ->  get() - value of specified key -> dicdoc.get("a")
            ->  items() - key,value
            ->  values() - values
            ->  keys() - keys
            ->  pop() - pops specified key
            ->  popitem() - pops last key value pair
            ->  setdefault()- Returns the value of the specified key. 
                If the key does not exist: insert the key, with the specified value
            -> update() - update specified key value pair

"""

dicdoc={1:1,"b":5,"c":3}
# print(dicdoc.pop("a"))
dicdoc.pop(1)
# print(dicdoc.get("c"))

# dicdoc.setdefault("d",10) -> important
# dicdoc.update({"a":77})
#dictionary comprehension
import string
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
new_list={}
res={chr(i): i-97 for i in range(97,123)}
new_res={k: v*2 for (k,v) in res.items()}
again_res={k:("even" if v%2==0 else "odd") for (k,v) in res.items()}
print(again_res)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

# we can also use regular "and"
dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}

print(dict1_tripleCond)