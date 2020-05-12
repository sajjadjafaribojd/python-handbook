f=open("prodevops.txt","a")
f.write("Now the file has more content!\n") # \n for enter
f.close()

f=open("prodevops.txt")
print(f.read())
f.close()

f=open("prodevops.txt","w")
f.write("Woops! I have deleted the content!")
f.close()

f=open("prodevops.txt")
print(f.read())
f.close()

