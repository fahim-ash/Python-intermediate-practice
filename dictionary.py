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
            ->setdefault()	- Returns the value of the specified key. 
            If the key does not exist: insert the key, with the specified value
            -> update() - update specified key value pair

"""

dicdoc={1:1,"b":5,"c":3}
# print(dicdoc.pop("a"))
dicdoc.pop(1)
# print(dicdoc.get("c"))

# dicdoc.setdefault("d",10) -> important
# dicdoc.update({"a":77})
print(dicdoc)