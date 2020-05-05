# Question 4

### **Question:**

>***Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:***

```
34,67,55,33,12,98
```


>***Then, the output should be:***
```
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple***

-----------------------

**Main author's Solution: Python 2**
```python
values = raw_input()
l = values.split(",")
t = tuple(l)
print l
print t
```
-------------------------

**My Solution: Python 3**
```python
lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
                          # method name split. ',' inside split function does split where it finds any ','
                          # and save the input as list in lst variable

tpl = tuple(lst)          # tuple method converts list to tuple

print(lst)
print(tpl)
```
--------------------------
# Question 5

### **Question:**

>***Define a class which has at least two methods:***
>* ***getString: to get a string from console input*** 
>* ***printString: to print the string in upper case.*** 

>***Also please include simple test function to test the class methods.***

### Hints:
>***Use __init__ method to construct some parameters***

----------------------------------
**Main author's Solution: Python 2**
```python
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
```
----------------------------------------
**My Solution: Python 3**
```python
class IOstring():
    def __init__(self):
        pass

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

xx = IOstring()
xx.getString()
xx.printString()
```
--------------------------
# Question 6

### **Question:**

>***Write a program that calculates and prints the value according to the given formula:***

>***Q = Square root of [(2 * C * D)/H]***

>***Following are the fixed values of C and H:***

>***C is 50. H is 30.***

>***D is the variable whose values should be input to your program in a comma-separated sequence.For example
Let us assume the following comma separated input sequence is given to the program:***
```
100,150,180
```
>***The output of the program should be:***
```
18,22,24
```
--------------------------

### Hints:
>***If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it should be assumed to be a console input.***

----------------------------

**Main author's Solution: Python 2**
```python
#!/usr/bin/env python
import math
c = 50
h = 30
value = []
items = [x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
```
--------------------------------

**My Solution: Python 3**
```python
from math import * # importing all math functions

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')    # splits in comma position and set up in list
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

print(",".join(D))
```
**OR**
```python
from math import * # importing all math functions

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')                     # splits in comma position and set up in list
D = [str(round(calc(int(i)))) for i in D]  # using comprehension method. It works in order of the previous code
print(",".join(D))
```
**OR**
```python
from math import *
C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)
    
print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))
```
**OR**
```python
from math import * # importing all math functions
C,H = 50,30

def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input().split(',')
D = list(map(calc,D))   # applying calc function on D and storing as a list
print(",".join(D))
```
---------------------
# Question 7

### **Question:**

>***Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.***

>***Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5***

>***Then, the output of the program should be:***
```
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```

-------------------------------

### Hints:
>***Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.***

------------------
**Main author's Solution: Python 2**
```python
input_str = raw_input()
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

print multilist
```
-----------------------
**My Solution: Python 3**
```python
x,y = map(int,input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):     
        tmp.append(i*j)
    lst.append(tmp)
    
print(lst)
```
**OR**
```python
x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]  
print(lst)
```
---------------------------
# Question 8

### **Question:**

>***Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.***

>***Suppose the following input is supplied to the program:***
```
without,hello,bag,world
```
>***Then, the output should be:***
```
bag,hello,without,world
```

----------------------
### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
items = [x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
```
----------------
**My Solution: Python 3**
```python
lst = input().split(',')
lst.sort()
print(",".join(lst))
```
-------------------------------
# Question 9

### **Question:**

>***Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.***

>***Suppose the following input is supplied to the program:***
```
Hello world
Practice makes perfect
```
>***Then, the output should be:***
```
HELLO WORLD
PRACTICE MAKES PERFECT
```

----------------------
### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence
```
----------------
**My Solution: Python 3**
```python
lst = []

while True:
    x = input()
    if len(x)==0:
        break;
    lst.append(x.upper())

for line in lst:
    print(line)
```
--------------------

[***go to previous day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%201.md "Day 1")

[***go to next day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%203.md "Day 3")

[***Discussion***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
