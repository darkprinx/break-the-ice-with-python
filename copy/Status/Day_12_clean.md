# Question 44

### **Question:**

> **_Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)._**

---

### Hints:

> **_Use map() to generate a list. Use lambda to define anonymous functions._**

---



**Solutions:**

```python
def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1,21)))
print (squaredNumbers)
```

---

# Question 45

### **Question:**

> **_Define a class named American which has a static method called printNationality._**

---

### Hints:

> **_Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this [link](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/)._**

---



**Solutions:**

```python
class American():
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()
```

---

# Question 46

### **Question:**

> **_Define a class named American and its subclass NewYorker._**

---

### Hints:

> **Use class Subclass(ParentClass) to define a subclass.\***

---



**Solutions:**

```python
class American():
    pass

class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)
```

---