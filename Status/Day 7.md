# Question 20
### Level 3
--------------------

**Question:**

***Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.***

----------------------
### Hints:
#### Consider use class, function and comprehension 

-------------------
**Main author's Solution: Python 2**
#### ***The solution code for this problem was not as reltive to as the problem mentioned and there was a typing mistake while calling the function.***

----------------
**My Solution: Python 3**
```

class Test:
    def generator(self,n):
        return [i for i in range(n) if i%7==0]   # returns the values as a list if an element is divisible by 7


n=int(input())
num=Test()
lst=num.generator(n)
print(lst)

```
----------------------
# Question 21
### Level 3
--------------------

**Question:**

***A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:***
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```
----------------------
***The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.***

#### Example:
***If the following tuples are given as input to the program:***
```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```
***Then, the output of the program should be:***

```
2
```
----------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.
-----------------------
**Main author's Solution: Python 2**
```
import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))
```
----------------
**My Solution: Python 3**
```
```
------------------
