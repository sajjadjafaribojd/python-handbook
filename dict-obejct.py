#Accessing Items Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(thisdict.get("brand"))

#Change Values
thisdict["year"]="2020"
print(thisdict)

#Loop Through a Dictionary
for i in thisdict:
    print(i) #show key
    print(thisdict[i]) #Print all values 
    
    
for i in thisdict.values():
    print(i)    
    
for x, y in thisdict.items(): #*********************
  print(x, y)    

#Add 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
  
#Removing Items
thisdict.pop("model")
print(thisdict)  

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"]) #*********************************
for x,y in myfamily.items():
     print(x, y)
     for z,j in y.items():
         print(z,j) 
         
#Dictionary update() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)       

#Dictionary values() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

