#https://www.w3schools.com/python/python_howto_remove_duplicates.asp

def remove_duplicat(x):
    #Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
    return list(dict.fromkeys(x)) 
    
my_list=["a","b","c","c"]
print(remove_duplicat(my_list))    