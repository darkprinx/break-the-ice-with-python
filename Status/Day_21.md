
# Question 85

### **Question**

>***By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].***


----------------------
### Hints 
> ***Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.***

----------------------

**Main author's Solution: Python 2**
```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print li
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 86

### **Question**

>***By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].***

----------------------
### Hints 
> ***Use list's remove method to delete a value.***

----------------------

**Main author's Solution: Python 2**
```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print li
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------

# Question 87

### **Question**

>***With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.***

----------------------
### Hints 
>***Use set() and "&=" to do set intersection operation.***

----------------------

**Main author's Solution: Python 2**
```python

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print li
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


# Question 88

### **Question**

>***With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.***

----------------------
### Hints 
> ***Use set() to store a number of values without duplicate.***

----------------------

**Main author's Solution: Python 2**
```python
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print removeDuplicate(li)

```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------



# Question 89

### **Question**

>***Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.***


----------------------
### Hints 
> ***Use Subclass(Parentclass) to define a child class.***

----------------------

**Main author's Solution: Python 2**
```python
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print aMale.getGender()
print aFemale.getGender()
```
----------------
**My Solution: Python 3**
```python
#to be written

```
---------------------


