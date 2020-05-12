#Strings are Arrays
a="Hello world!"
b=" Hello word "
print(a[0])

#Slicing
print(a[2:5])

#Negative Indexing
print(a[-5:-2])

#String Length
print(len(a))

#The strip() method removes any whitespace from the beginning or the end
print(b.strip())

#The replace() method replaces a string with another string
c = "Hello, World!"
print(c.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator
d = "Hello, World!"
print(c.split(",")) # returns ['Hello', ' World!']

#Check String
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 

#String Format
age= 30
txt="I am "
print(txt+str(age))

info="I am {}"
print(info.format(age))

age=30
car=2
moblie=3
info2="I am {1}  and {2} car and {0} moblie"
print(info2.format(age,car,moblie))

#String join() Method
myDict = {"name": "John", "country": "Norway"}
mySeparator = "-"

x = mySeparator.join(myDict)
print(x)
