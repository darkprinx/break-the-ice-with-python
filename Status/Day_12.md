# Question 44
### Level 1

**Question:**
***Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).***

---------------

### Hints: Use map() to generate a list. Use lambda to define anonymous functions.
---------------

**Main Author's Solution: Python 2**
```
squaredNumbers = map(lambda x: x**2, range(1,21))
print squaredNumbers
```
**My Solution: Python 3**
```
```
----------------------------------------

# Question 45
### Level 1

**Question:**
***Define a class named American which has a static method called printNationality.***

---------------------
### Hints: Use @staticmethod decorator to define class static method.
---------------------
**Main Author's Solution: Python 2**
```
class American(object):
    @staticmethod
    def printNationality():
        print "America"

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```
**My Solution: Python 3**
```
```
----------------------------------------

7.2

Question:
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

Solution:

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print anAmerican
print aNewYorker


