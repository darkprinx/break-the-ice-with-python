
# Question 90

### **Question**

>***Please write a program which count and print the numbers of each character in a string input by console.***

>***Example:
If the following string is given as input to the program:***
```
abcdefgabc
```
>***Then, the output of the program should be:***
```
a,2
c,2
b,2
e,1
d,1
g,1
f,1
```
### Hints 
> ***Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.***

----------------------

**Main author's Solution: Python 2**
```python
dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 91

### **Question**

>***Please write a program which accepts a string from console and print it in reverse order.***

>**Example:
If the following string is given as input to the program:***
```
rise to vote sir
```
>***Then, the output of the program should be:***
```
ris etov ot esir
```
### Hints 
> ***Use list[::-1] to iterate a list in a reverse order.***

----------------------

**Main author's Solution: Python 2**
```python
s=raw_input()
s = s[::-1]
print s
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------

# Question 92

### **Question**

>***Please write a program which accepts a string from console and print the characters that have even indexes.***

>***Example:
If the following string is given as input to the program:***
```
H1e2l3l4o5w6o7r8l9d
```
>***Then, the output of the program should be:***
```
Helloworld
```
### Hints 
>***Use list[::2] to iterate a list by step 2.***

----------------------

**Main author's Solution: Python 2**
```python
s=raw_input()
s = s[::2]
print s
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


# Question 93

### **Question**

>***Please write a program which prints all permutations of [1,2,3]***

----------------------
### Hints 
> ***Use itertools.permutations() to get permutations of list.***

----------------------

**Main author's Solution: Python 2**
```python

import itertools
print list(itertools.permutations([1,2,3]))
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 94

### **Question**

>***Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?***


----------------------
### Hints 
> ***Use for loop to iterate all possible solutions.***

----------------------

**Main author's Solution: Python 2**
```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print solutions
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


