"""x="first global variabe"

def myfunc():
    x="local variable"
    print(x)

myfunc()"""

x="first global variabe"

def myfunc():
    global x
    x="local variable"
   
myfunc()
print (x)


