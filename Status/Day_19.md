
# Question 75

### **Question**

>***Please write a program to randomly print a integer number between 7 and 15 inclusive.***

----------------------
### Hints 
> ***Use random.randrange() to a random integer in a given range.***

----------------------

**Solution:**
```python
import random
print random.randrange(7,16)
```
----------------

# Question 76

### **Question**

>***Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".***

----------------------
### Hints 
> ***Use zlib.compress() and zlib.decompress() to compress and decompress a string.***

----------------------

**Solution:**
```python
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print t
print zlib.decompress(t)
```
----------------

# Question 77

### **Question**

>***Please write a program to print the running time of execution of "1+1" for 100 times.***

----------------------
### Hints 
>***Use timeit() function to measure the running time.***

----------------------

**Main author's Solution: Python 2**
```python

from timeit import Timer
t = Timer("for i in range(100):1+1")
print t.timeit()
```
----------------
**My Solution: Python 3**
```python
import datetime

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)
```
**OR**
```python
import time

before = time.time()
for i in range(100):
    x = 1 + 1
after = time.time()
execution_time = after - before
print(execution_time)
```
---------------------

# Question 78

### **Question**

>***Please write a program to shuffle and print the list [3,6,7,8].***

----------------------
### Hints 
> ***Use shuffle() function to shuffle a list.***

----------------------

**Main author's Solution: Python 2**
```python

from random import shuffle
li = [3,6,7,8]
shuffle(li)
print li

```
----------------
**My Solution: Python 3**
```python
import random

lst = [3,6,7,8]
random.shuffle(lst)
print(lst)
```
**OR**
```python
import random

# shuffle with a chosen seed
lst = [3,6,7,8]
seed = 7
random.Random(seed).shuffle(lst)
print(lst)
```
---------------------

# Question 79

### **Question**

>***Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].***


----------------------
### Hints 
> ***Use list[index] notation to get a element from a list.***

----------------------

**Main author's Solution: Python 2**
```python

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print sentence
```
----------------
**My Solution: Python 3**
```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))
```
---------------------


