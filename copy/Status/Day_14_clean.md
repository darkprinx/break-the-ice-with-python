# Question 51

### **Question**

> **_Write a function to compute 5/0 and use try/except to catch the exceptions._**

---

### Hints

> **_Use try/except to catch exceptions._**

---

**Solutions:**

```python
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")

```

---

# Question 52

### **Question**

> **_Define a custom exception class which takes a string message as attribute._**

---

### Hints

> **_To define a custom exception, we need to define a class inherited from Exception._**

---

**Solutions:**

```python

class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)

```

---

# Question 53

### **Question**

> **_Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only._**

> **_Example:
> If the following email address is given as input to the
> program:_**

> john@google.com

> **_Then, the output of the program should be:_**

> john

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---

### Hints

> **_Use \w to match letters._**

---

**Solutions:**

```python
email = "john@google.com"
email = email.split('@')
print(email[0])
```

---

**OR**

```python
import re

email = "john@google.com elise@python.com"
pattern = "(\w+)@\w+.com"
ans = re.findall(pattern,email)
print(ans)
```

---
