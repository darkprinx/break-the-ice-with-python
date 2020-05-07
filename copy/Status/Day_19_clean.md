# Question 75

### **Question**

> **_Please write a program to randomly print a integer number between 7 and 15 inclusive._**

---

### Hints

> **_Use random.randrange() to a random integer in a given range._**

---

**Solution:**

```python
import random
print random.randrange(7,16)
```

---

# Question 76

### **Question**

> **_Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"._**

---

### Hints

> **_Use zlib.compress() and zlib.decompress() to compress and decompress a string._**

---

**Solution:**

```python
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print t
print zlib.decompress(t)
```

---

# Question 77

### **Question**

> **_Please write a program to print the running time of execution of "1+1" for 100 times._**

---

### Hints

> **_Use timeit() function to measure the running time._**

---



**Solutions:**

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

---

# Question 78

### **Question**

> **_Please write a program to shuffle and print the list [3,6,7,8]._**

---

### Hints

> **_Use shuffle() function to shuffle a list._**

---



**Solutions:**

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

---

# Question 79

### **Question**

> **_Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]._**

---

### Hints

> **_Use list[index] notation to get a element from a list._**

---



**Solutions:**

```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))
```

---