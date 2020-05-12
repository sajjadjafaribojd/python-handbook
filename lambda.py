x= lambda a: a + 10
print(x(10))

z= lambda a,b: a+b
print(z(10,12))

def lamdafunc(n):
    return lambda a: a * n 

mylambad_arg=lamdafunc(2)
print(mylambad_arg(11))