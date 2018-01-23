# Question 31
### level 1

**Question:**

***Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.***

----------------------
### Hints: Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.
-------------------
**Main Author's Solution: Python 2**
```
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print d
		
printDict()
```
----------------
**My Solution: Python 3**
```
def printDict():
    dict={i:i**2 for i in range(1,21)}   # Using comprehension method and
    print(dict)

printDict()
```
----------------

# Question 32
### level 1

**Question:**

***Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.***

----------------------
### Hints:
#### Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

-------------------
**Main Author's Solution: Python 2**
```
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print k
printDict()
```
----------------
**My Solution: Python 3**
```
def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()
```
---------------------

# Question 33
### level 1

**Question:**

***Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).***

----------------------
### Hints:
#### Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

-------------------
**Main Author's Solution: Python 2**
```
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li
		
printList()
```
----------------
**My Solution: Python 3**
```
def printDict():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printDict()
```
-------------------
