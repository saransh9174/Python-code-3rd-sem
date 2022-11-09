import ast
import numpy as np
l=list()

l5=[]
l6=[]
def F1(l):
 for i in range(3):
  try:
   user_input = input('Enter space-separated integers: ')

   my_tuple = tuple(int(item) for item in user_input.split())
   l.append(my_tuple)
   
  except ValueError:
    print('The provided value is not a tuple')
    return(0)

F1(l) 
#print("The list is: ")
#print(l)
l4=np.array(l.copy())
print(l4)
for i in l:
    for x in i:
        l5.append(x)
 
for i in range(len(l5)):
    if(l5[i]%2==0):
        l6.append(l5[i])
print("Answer: ",l6
)

def prime(l5):
    prime_list = []
    for i in range(len(l5)):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

a=prime(l5)
print(a)