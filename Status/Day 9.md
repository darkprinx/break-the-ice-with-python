
# Question 26

### **Question:**

>***Define a function which can compute the sum of two numbers.***

----------------------

### Hints:
>***Define a function with two numbers as arguments. You can compute the sum in the function and return the value.***

-------------------

**Main author's Solution: Python 2**
```python
def SumFunction(number1, number2):
	return number1 + number2

print SumFunction(1,2)
```
----------------
**My Solution: Python 3**
```python
sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
print(sum(1,2))	     
```

----------------------------
# Question 27

### **Question:**

>***Define a function that can convert a integer into a string and print it in console.***

----------------------
### Hints: 
>***Use str() to convert a number to string.***

-------------------

**Main author's Solution: Python 2**
```python
def printValue(n):
	print str(n)

printValue(3)
```
----------------

**My Solution: Python 3**
```python
conv = lambda x : str(x)
n = conv(10)
print(n)
print(type(n))            # checks the type of the variable
```
---------------------

# Question 28

### **Question:**

>***Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.***

----------------------
### Hints: 
>***Use int() to convert a string to integer.***

-------------------
**Main author's Solution: Python 2**
```python
def printValue(s1,s2):
	print int(s1) + int(s2)
printValue("3","4") #7
```
----------------

**My Solution: Python 3**
```python
sum = lambda s1,s2 : int(s1) + int(s2)
print(sum("10","45"))      # 55
```
-------------------

# Question 29

### **Question:**

>***Define a function that can accept two strings as input and concatenate them and then print it in console.***

----------------------

### Hints: 
>***Use + sign to concatenate the strings.***

-------------------
**Main author's Solution: Python 2**
```python
def printValue(s1,s2):
	print s1 + s2

printValue("3","4") #34
```
----------------
**My Solution: Python 3**
```python
sum = lambda s1,s2 : s1 + s2
print(sum("10","45"))        # 1045
```
------------------
# Question 30

### **Question:**

>***Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.***

----------------------
### Hints: 
>***Use len() function to get the length of a string.***

-------------------
**Main author's Solution: Python 2**
```python
def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1 > len2:
		print s1
	elif len2 > len1:
		print s2
	else:
		print s1
		print s2
		
printValue("one","three")

```
----------------
**My Solution: Python 3**
```python
def printVal(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)

s1,s2=input().split()
printVal(s1,s2)
```
------------

```python
'''Solution by: yuan1z'''
func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
```
------------


[***go to previous day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%208.md "Day 9")

[***go to next day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_10.md "Day 10")

[***Discussion***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
