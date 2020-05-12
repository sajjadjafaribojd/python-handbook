#Simple class
class myclass:
    x = 5
    
myobject=myclass()
print(myobject.x)    

#The __init__() Function
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
P1 = Person("sajjad",30)

print(P1.name)
print(P1.age)  

class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfunc(self):
        print("my name is " + self.name ) 
        
p2=Person2("JabJ",30)
p2.myfunc()

#Python Inheritance
class Person3:
    def __init__(self,name,family):
        self.firstname=name
        self.lastname=family
    
    def printname(self):
        print(self.firstname + " " + self.lastname)
 
#Create a Child Class 
class Student(Person3):
    #Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
     def __init__(self,name,family,year):
         #super() function that will make the child class inherit all the methods and properties from its parent
         #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
         super().__init__(name,family)
         self.graduationyear = year
         
     def welcome(self):
         print("Welcome " + self.firstname + " " + self.lastname + " to the class of " , self. graduationyear )    
 
result=Student("sajjad","jafari",2019)
result.printname()
result.welcome()
 
 

                 