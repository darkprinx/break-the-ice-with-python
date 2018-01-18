
# Question 26
## Level 1
-----------------

**Question:**

***Define a function which can compute the sum of two numbers.***

----------------------
### Hints:
#### Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

-------------------

**Main author's Solution: Python 2**
```
def SumFunction(number1, number2):
	return number1 + number2

print SumFunction(1,2)
```
----------------
**My Solution: Python 3**
```
sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
print(sum(1,2))
```
----------------------------
# Question 27
## Level 1
-----------------

**Question:**

***Define a function that can convert a integer into a string and print it in console.***

----------------------
### Hints: Use str() to convert a number to string.
-------------------

**Main author's Solution: Python 2**
```
def printValue(n):
	print str(n)

printValue(3)
```
----------------

**My Solution: Python 3**
```
conv = lambda x : str(x)
n = conv(10)
print(n)
print(type(n))            # checks the type of the variable
```
---------------------
