#used instead of return ...it doesnt end the function as return 
# generator -> basically a function with yeild

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        if my_str[i]=="l":
            yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)