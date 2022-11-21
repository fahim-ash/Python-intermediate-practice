#python eval() checks and evaluates legit python expression 
# and performs it

z=eval('print(100)')
# eval(expression,global,local)

# global
n=100
nn=eval("n+100",{"n":n})

# also with local
m=100
mm=eval("m+p",{"m":m},{"p":100})
print(mm)