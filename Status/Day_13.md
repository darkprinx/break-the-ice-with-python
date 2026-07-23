# Question 47

### **Question**

> **_Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area._**

---

### Hints

> **_Use def methodName(self) to define a method._**

---

**Main author's Solution: Python 2**

```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()
```

---

**My Solution: Python 3**

```python
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = Circle(5)
print(circle.area())
```

---

# Question 48

### **Question**

> **_Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area._**

---

### Hints

> **_Use def methodName(self) to define a method._**

---

**Main author's Solution: Python 2**

```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print aRectangle.area()

```

---

**My Solution: Python 3**

```python
class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


rect = Rectangle(2,4)
print(rect.area())

```

---

# Question 49

### **Question**

> **_Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default._**

---

### Hints

> **_To override a method in super class, we can define a method with the same name in the super class._**

---

**Main author's Solution: Python 2**

```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print aSquare.area()
```

---

**My Solution: Python 3**

* The following solution is incorrect. The parent class's area method can be accessed if the child class does not have a method by the same name. Here, because we are instantiating the child class and setting the default length value to zero, it is printing out zero and has no relation with the area of the parent class being zero. If we need to access the parent class method, the child class should not have the same name. The interpreter looks for the method in the current class before moving up the hierarchy.

```python
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area
```
```python
''' Solution by 0KvinayK0
'''
class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

sq = Square(5)
print(sq.area())  # Output: 25
print(super(Square, sq).area())  # Output: 0
```
---

# Question 50

### **Question**

> **_Please raise a RuntimeError exception._**

---

### Hints

> **_UUse raise() to raise an exception._**

---

**Solution:**

```python
raise RuntimeError('something wrong')
```

---

## Conclusion

**_Well It seems that the above problems are very much focused on basic concpets and implimantation of object oriented programming.As the concepts are not about to solve any functional problem rather design the structure , so both codes are very much similar in there implimantation part._**

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_12.md "Day 12")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_14.md "Day 14")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
