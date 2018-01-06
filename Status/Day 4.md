
# Question 14
### Level 2
--------------------

**Question:**

***Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.***

***Suppose the following input is supplied to the program:***
```
Hello world!
```
***Then, the output should be:***
```
UPPER CASE 1
LOWER CASE 9
```
---------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.

-------------------
**Main author's Solution: Python 2**
```
s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]
```
----------------
**My Solution: Python 3**
```
word=input()
upper,lower=0,0

for i in word:
    if 'a'<=i and i<='z' :
        lower+=1
    if 'A'<=i and i<='Z':
        upper+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
```
**OR**
```
word=input()
upper,lower=0,0

for i in word:
        lower+=i.islower()
        upper+=i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
```

