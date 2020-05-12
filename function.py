#Arbitrary Arguments, *args
def myfunc(*arg):
    print(arg[2])
    
myfunc("Emil", "Tobias", "Linus")    


#Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def myfunc2(arge):
    for i in arge:
        print(i)

mylist=["BMW","Benz","MVM110"]
myfunc2(mylist)        

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively(houses):
    for house in houses:
        print("Delivering presents to", house)
deliver_presents_iteratively(houses)  



#
      