import mymodule as jabj #Re-naming a Module
from mymodule2 import personal_info2 #Import From Module

#print(mymodule.txtinfo("sajjad"))
print(jabj.txtinfo("sajjad"))
#x= mymodule.personal_info["age"]
x= jabj.personal_info["age"]
print(x)

print(dir(jabj))

print(personal_info2["age"]) #Import From Module