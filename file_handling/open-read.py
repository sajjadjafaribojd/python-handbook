f=open("prodevops.txt","r")
#print(f) #The open() function returns a file object,
#print(f.read())

#Read Only Parts of the File
#print(f.read(5))

#Read one Lines
#print(f.readline())
#print(f.readline()) #output print 2 line beacuse use twois f.readline()


for line in f:
    print(line)
f.close() #Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
     