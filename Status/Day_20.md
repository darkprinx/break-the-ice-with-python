
# Question 80

### **Question**

>***Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].***


----------------------
### Hints 
> ***Use list comprehension to delete a bunch of element from a list.***

----------------------

**Main author's Solution: Python 2**
```python
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print li
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 81

### **Question**

>***By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].***

----------------------
### Hints 
> ***Use list comprehension to delete a bunch of element from a list.***

----------------------

**Main author's Solution: Python 2**
```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print li
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------

# Question 82

### **Question**

>***By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].***

----------------------
### Hints 
>***Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.***

----------------------

**Main author's Solution: Python 2**
```python

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print li
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


# Question 83

### **Question**

>***By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].***

----------------------
### Hints 
> ***Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.***

----------------------

**Main author's Solution: Python 2**
```python

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print li

```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 84

### **Question**

>***By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.***


----------------------
### Hints 
> ***Use list comprehension to make an array.***

----------------------

**Main author's Solution: Python 2**
```python

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print array
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


