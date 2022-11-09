file=open(r"C:/Users/91965/Documents/PYTHON/Myfile.txt","w+")
t="Hi"
file.writelines(t)
file.close()
#checking
file=open(r"C:/Users/91965/Documents/PYTHON/Myfile.txt","r")
lines=file.readlines()
for row in lines:
    w="YO"
    if row.find(w)!=-1:
        print("String exists")
    else:
        print("String does not exists")
##EXtracting

file=open(r"C:/Users/91965/Documents/PYTHON/Myfile.txt","r")
text=input("Enter string: ")
for line in file:
        line = line.rstrip()
        if (line.startswith(text)):
            print (line)
else:
 print("na")


 ##Writing extracted lines in a new file
with open("C:/Users/91965/Documents/PYTHON/Myfile.txt") as f:
 with open("C:/Users/91965/Documents/PYTHON/test.txt", "w") as f1:
     for line in f:
      f1.write(line)