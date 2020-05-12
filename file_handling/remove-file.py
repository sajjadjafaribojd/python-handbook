import os

if os.path.exists("test.txt"):
    os.remove("txt.txt")
else:
    print("File not exist")    