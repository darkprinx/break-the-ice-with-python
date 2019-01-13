
# Question 70

### **Question**

>***Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.***


----------------------
### Hints 
> ***Use random.choice() to a random element from a list.***

----------------------

**Main author's Solution: Python 2**
```python
li = [2,4,6,8]
import random
print random.choice([i for i in range(11) if i%2==0])
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 71

### **Question**

>***Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.***

----------------------
### Hints 
> ***Use random.choice() to a random element from a list.***

----------------------

**Main author's Solution: Python 2**
```python
import random
print random.choice([i for i in range(201) if i%5==0 and i%7==0])
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------

# Question 72

### **Question**

>***Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.***

----------------------
### Hints 
>***Use random.sample() to generate a list of random values.***

----------------------

**Main author's Solution: Python 2**
```python

import random
print random.sample(range(100), 5)

```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


# Question 73

### **Question**

>***Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.***

----------------------
### Hints 
> ***Use random.sample() to generate a list of random values.***

----------------------

**Main author's Solution: Python 2**
```python

import random
print random.sample([i for i in range(100,201) if i%2==0], 5)

```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 74

### **Question**

>***Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.***


----------------------
### Hints 
> ***Use random.sample() to generate a list of random values.***

----------------------

**Main author's Solution: Python 2**
```python

import random
print random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5)
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


