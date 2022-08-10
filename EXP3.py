Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
mylist=[1,2,3,'a','b','c']
tuple(mylist)
(1, 2, 3, 'a', 'b', 'c')
list1[0]*5
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list1[0]*5
NameError: name 'list1' is not defined. Did you mean: 'list'?
list[0]*5
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list[0]*5
TypeError: unsupported operand type(s) for *: 'types.GenericAlias' and 'int'
mylist[0]slice
SyntaxError: invalid syntax
mylist[0] slice
SyntaxError: invalid syntax
mylist[0]
1
`mylist.insert(6,'q')
SyntaxError: invalid syntax
mylist.insert(6,'q')
mylist
[1, 2, 3, 'a', 'b', 'c', 'q']
mylist.insert(7,1)
mylist
[1, 2, 3, 'a', 'b', 'c', 'q', 1]
mylist.count(1)
2
2 in mylist
True
2 notin mylist
SyntaxError: invalid syntax
2 not in mylist
False
test=[1,2,3,3,4,5,6,6,7,8]
output=[]
for x in test
SyntaxError: expected ':'
for x in test:
    if x not in output:
        output.append(x)
        print(output)

        
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
