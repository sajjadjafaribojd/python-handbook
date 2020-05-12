print(10 > 9)#False
print(10 == 9)#True
print(10 < 9)#False

x="Hello"
y=""
z=0
t=12
print(bool(x))#True
print(bool(y))#False
print(bool(z))#False
print(bool(t))#True

#Functions can Return a Boolean
def myfun():
    return False
    #return 0
print(bool(myfun()))   
 
#isinstance() function, which can be used to determine if an object is of a certain data type:
x = "sajjad"
print(isinstance(x, int))


 