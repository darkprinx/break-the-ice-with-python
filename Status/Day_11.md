# Question 38
### Level 1

**Question:**

***With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.***

----------------------
### Hints: Use [n1:n2] notation to get a slice from a tuple.

-------------------

**Main Author's Solution: Python 2**
```
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print tp1
print tp2
```
----------------
**My Solution: Python 3**
```
tpl = (1,2,3,4,5,6,7,8,9,10)
lst1,lst2 = [],[]

for i in range(0,5):
    lst1.append(i)

for i in range(5,10):
    lst2.append(i)

print(lst1)
print(lst2)
```
------------------
