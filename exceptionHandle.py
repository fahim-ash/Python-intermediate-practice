# need a lot more code 
# try:
#     f=open("test.text")
#     print("it opened")
# except:
#     print("cant open")
# finally:
#     print(f.read())

# custom exception
class Hablu_Error(Exception):
    def __init__(self,salary,message="onek besi"):
        self.salary=salary
        self.message=message
        # super().__init__(self.message)

try:
    print("input salary",end="")

    s=int(input())
    if s>100:
        raise Hablu_Error
except:
    print("input again",end="")
    s=int(input())
finally:
    print(f"your salary is {s}")
