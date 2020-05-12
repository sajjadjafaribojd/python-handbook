# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]
print("banana" in x)

# returns True because a sequence with the value "pineapple" is not in the list
x = ["apple", "banana"]
print("pineapple" not in x)

thislist = ["apple", "banana", "cherry","BMW","Volvo"]
print(thislist)

#Access Items
print(thislist[1])

#Negative Indexing - access to last item.
print(thislist[-1])

#Range of Indexes
print(thislist[2:4])


#Change Item Value
thislist[3]="BMW-2020"
print(thislist)

#Loop Through a List
for i in thislist:
    print(i)

txt="sajjad jafari"
for j in txt:
    print(j)
    
    
#Check if Item Exists
if "apple" in thislist:
    print("Yes this item in this list")
else:
    print("Can not find item")

#List Length
print(len(thislist))

#Add Items
thislist.append("MVM110")
print(thislist)

#To add an item at the specified index
thislist.insert(4,"Benz")
print(thislist)

#Remove Item
thislist.remove("Benz")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop(5)
print(thislist)

#Delete list completely:
#del thislist
print(thislist)

#The clear() method empties the list:
#thislist.clear()
print(thislist)    

#Copy a List
mylist=thislist.copy()
print(mylist)

#Join Two Lists
mylist=["MVM110","405",111]
print(mylist+thislist)

#Join Two Lists
for o in mylist:
    thislist.append(o)
print(thislist)    


#List reverse
thislist.reverse()
print(thislist)

#Sort list
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
def sortfunc(e):
    return len(e)

cars.sort(key=sortfunc)
print(cars)


cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def sortfunc1(e):
    return e['year']

cars.sort(reverse=True,key=sortfunc1)
print(cars)

#Count Return the number of times
print(thislist.count("banana"))