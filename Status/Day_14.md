
# Question 51

### **Question**

> ***Write a function to compute 5/0 and use try/except to catch the exceptions.***

----------------------
### Hints 
> ***Use try/except to catch exceptions.***

----------------------

**Main author's Solution: Python 2**
```python
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print "division by zero!"
except Exception, err:
    print 'Caught an exception'
finally:
    print 'In finally block for cleanup'
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


# Question 52

### **Question**

> ***Define a custom exception class which takes a string message as attribute.***

----------------------
### Hints 
> ***To define a custom exception, we need to define a class inherited from Exception.***

----------------------

**Main author's Solution: Python 2**
```python
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")

```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


# Question 53

### **Question**

> ***Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.***

> ***Example:
If the following email address is given as input to the 
program:***
```
john@google.com
```
> ***Then, the output of the program should be:***
```
john
```
> ***In case of input data being supplied to the question, it should be assumed to be a console input.***

----------------------
### Hints 
> ***Use \w to match letters.***

----------------------

**Main author's Solution: Python 2**
```python
import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print r2.group(1)
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------
