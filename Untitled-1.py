file=open(r"C:/Users/91965/Documents/PYTHON/Myfile.txt","a")

for i in range(10):
    st=input("Enter string: ")
    file.writelines(st)
    file.writelines("\n")
file.close()
