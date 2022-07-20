Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============== RESTART: C:/Users/mpstme.student/Desktop/trial.py ==============
a="saransh"
len(a0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len(a0)
NameError: name 'a0' is not defined. Did you mean: 'a'?
len(a)
7
"S" in a
False
"s"
's'
"s" in a
True
a[08]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a[0:8]
'saransh'
a[0:7]
'saransh'
a[0:5]
'saran'
b="h i"
len(b)
3
b(len(b))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b(len(b))
TypeError: 'str' object is not callable
a.split()
['saransh']
a.split('s')
['', 'aran', 'h']
b="hi"
c=a+b
c.split
<built-in method split of str object at 0x000001EC89E563F0>
a="hello"
b="world"
c=a+b
c.split()
['helloworld']
['helloworld']
['helloworld']
txt="hi {}"
name="saransh"
txt.format(name)
'hi saransh'
a
'hello'
b
'world'
c=a+b
c.spilt()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
c.split
<built-in method split of str object at 0x000001EC8830A770>
c.split()
['helloworld']
c
'helloworld'
c=a+" " +b
c
'hello world'
c.split()
['hello', 'world']
c.replace('h','s')
'sello world'
c.split('o')
['hell', ' w', 'rld']
