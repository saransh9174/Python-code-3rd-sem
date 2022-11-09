
import numpy as np
l=[]
l1=[]
l2=[]
class bill():
    def __init__(self,product_id,product_name,product_price):
     self.product_id=product_id
     self.product_name=product_name
     self.product_price=product_price
     print(self.product_id)
     print(self.product_name)
     print(self.product_price)

for i in range(2):
 product_id=int(input('Enter product ID: '))
 product_name=input('Enter product name: ')
 product_price=int(input('Enter price: '))
 y=product_id,product_name,product_price
 x=tuple(y)
 l.append(x)
 print(l)
 

##
def printproductinfo(n):
    l3=list(l.copy())
    res=[list(ele)for ele in l3]

    for i in range(len(res)):
        for x in range(len(res[i])):
         if(res[i][x]==n):
            print(res[i])
n=int(input("Enter the product id: "))
printproductinfo(n) 


def customer_bill(id):
    l3=list(l.copy())
    res=[list(ele)for ele in l3]

    for i in range(len(res)):
        for x in range(len(res[i])):
         if(res[i][x]==id):
            print(res[i][x+1])
id=input("Enter id: ")
customer_bill(id)
