
# Question 47
### Level 1

**Question:**

***Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. ***

----------------------
### Hints: Use def methodName(self) to define a method.
-------------------

**Main author's Solution: Python 2**
```
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()
```
----------------
**My Solution: Python 3**
```
```
----------------

# Question 48
### Level 1

**Question:**

***Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. ***

----------------------
### Hints: Use def methodName(self) to define a method.
-------------------

**Main author's Solution: Python 2**
```
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print aRectangle.area()

```
----------------
**My Solution: Python 3**
```
```
----------------

