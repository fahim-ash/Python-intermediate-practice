# need a lot more code 
try:
    f=open("test.text")
    print("it opened")
except:
    print("cant open")
finally:
    print(f.read())
