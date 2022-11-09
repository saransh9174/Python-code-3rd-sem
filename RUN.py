
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
 
