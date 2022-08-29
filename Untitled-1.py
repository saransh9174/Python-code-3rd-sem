######################tuples################
lis1=[1,2,3]
v=[(val,pow(val,3)) for val in lis1]
print(v)
###################dictionary#################
students = dict()
n = int(input("Enter number of students :"))
for i in range(n):
        sname = input("Enter names of student :")
        marks= []
        for j in range(5):
           mark = float(input("Enter marks :"))
           marks.append(mark)
        students[sname] = sorted(marks)
print("Dictionary of student created :")
print(students)
####################LIST
l=[]
n=int(input("Enter number of elements"))
for i in range(1,n+1):
    e=int(input("Enter element"))
    l.append(e)
    print(l)
   
 ######################################
 EVEN/ODD LIST
l=[]
n=int(input("Enter number of elements"))
for i in range(1,n+1):
    e=int(input("Enter element"))
    l.append(e)
    print(l)
even=[]
odd=[]
for j in l:
    if(j%2==0):
     even.append(j)
    else:
        odd.append(j)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
##################################HALF PYRAMID#########################3

for i in range(4):
    for j in range(i): #########TO REVERSE PUT RANGE(4-i)##############
        print("#",end= "")
    print()
    
  ##################HOLLOW DIAMOND USING AA,BB,CC,DD##########
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
# Diamond array
diamond = []

rows = -1
# Prompt user to enter number of rows
while rows < 1 or rows > 26:
    rows = int(input("Enter number of rows N: "))
for i in range(0, rows):
    # Add letters to the diamond
    diamond.append("")
    for j in range(0, rows - i):
        diamond[i] += " "
    diamond[i] += alphabets[i];
    if alphabets[i] != 'A':
        # Put spaces between letters
        for j in range(0, 2 * i - 1):
            diamond[i] += " "
        diamond[i] += alphabets[i]
    # Print the first part of the diamond
    print(diamond[i])
# Print the second part of the diamond
for i in reversed(range(0, rows - 1)):
    print(diamond[i])
###########MATRIX########
# importing numpy as np
import numpy as np


# creating first matrix
A = np.array([[1, 2], [3, 4]])

# creating second matrix
B = np.array([[4, 5], [6, 7]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))
