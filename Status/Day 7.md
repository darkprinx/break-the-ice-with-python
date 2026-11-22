<!-- Day page sponsor slot: empty, so nothing is shown. When sold, add the line below
     right under this comment. Logo 120x40 px (send 240x80), text up to 60 characters:
     <p align="right"><sub>Sponsored</sub><br><a href="URL?ref=github-day-07"><img src="../assets/sponsors/NAME.png" height="40" align="middle" alt="NAME"></a>&nbsp; <a href="URL?ref=github-day-07">One-line message →</a></p> -->

<!-- day-nav:top -->
<p align="center"><a href="Day%206.md">← Day 6</a> &nbsp;·&nbsp; <a href="../README.md#days">All 24 days</a> &nbsp;·&nbsp; <a href="Day%208.md">Day 8 →</a></p>
<!-- /day-nav:top -->

# Question 20

### **Question:**

> **_Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n._**

> **_Suppose the following input is supplied to the program:_**

```
7
```

> **_Then, the output should be:_**

```
0
7
14
```
---

### Hints:

> **_Consider use class, function and comprehension._**

---

<details markdown="1">
<summary><b>💡 Show solutions</b> (try it yourself first!)</summary>

**Main author's Solution: Python 2**

#### **_The solution code for this problem was not as reltive to as the problem mentioned and there was a typing mistake while calling the function._**

---

**Solution: Python 3**

```python
'''Solution by: ShalomPrinz
'''
class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            yield i * 7

for i in MyGen().by_seven( int(input('Please enter a number... ')) ):
    print(i)
```

---

```python
'''Solution by: Seawolf159
'''
class Divisible:

    def by_seven(self, n):
        for number in range(1,n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)

```
```python
'''Solution by: Viktor
'''
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 7
            return num
        raise StopIteration


for i in MyGen(0, 100):
    print(i)

```
---

```python
'''Solution by: AmirhosseinEnayat
'''
class DivisibleBySeven:
    def by_seven(self, n):
        for number in range(0, n + 1):
            if number % 7 == 0:
                yield number

d = DivisibleBySeven()
for number in d.by_seven(int(input("please enter the number : "))):
    print(number)
```

</details>

---

# Question 21

### **Question:**

> **_A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:_**

```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

> **_The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer._**
> **_Example:_**
> **_If the following tuples are given as input to the program:_**

```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

> **_Then, the output of the program should be:_**

```
2
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function._**

---

<details markdown="1">
<summary><b>💡 Show solutions</b> (try it yourself first!)</summary>

**Main author's Solution: Python 2**

```python
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

---

**My Solution: Python 3**

```python
import  math

x,y = 0,0
while True:
    s = input().split()
    if not s:
        break
    if s[0]=='UP':                  # s[0] indicates command
        x-=int(s[1])                # s[1] indicates unit of move
    if s[0]=='DOWN':
        x+=int(s[1])
    if s[0]=='LEFT':
        y-=int(s[1])
    if s[0]=='RIGHT':
        y+=int(s[1])
                                    # N**P means N^P
dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)
```
---
```python
'''Solution by: pratikb0501
'''

from math import sqrt
lst = []
position = [0,0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))
```

```python
'''Solution by: Naveen675
'''

from math import sqrt
x,y=0,0
while True:
    s = input()
    if not(s):
        break
    if 'UP' in s:
        print("UP")
        y = y+int(s.strip('UP '))
    elif 'DOWN' in s:
        y = y-int(s.strip('DOWN '))
        print("down")
    elif 'LEFT' in s:
        x = x+int(s.strip('LEFT '))
        print("left")
    elif 'RIGHT' in s:
        x = x-int(s.strip('RIGHT '))
print(round(math.sqrt(x**2 + y**2)))
```

</details>

---

<!-- day-nav:bottom -->
<p align="center">
<sub><b>UP NEXT</b></sub><br>
<a href="Day%208.md"><img src="../assets/days/day-08.svg" width="240" alt="Day 8, questions 22 to 25: Word frequency &amp; docs"></a><br>
<a href="Day%206.md">← Day 6</a> &nbsp;·&nbsp; <a href="../README.md#days">All 24 days</a>
</p>
<!-- /day-nav:bottom -->

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
