
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
**OR**
```
word=input()
upper=sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
lower=sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
```
----------------------
# Question 15
### Level 2
--------------------

**Question:**

***Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.***

***Suppose the following input is supplied to the program:***

```9```

***Then, the output should be:***
```
11106
```
---------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.

-------------------
**Main author's Solution: Python 2**
```
a = raw_input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print n1+n2+n3+n4
```
----------------
**My Solution: Python 3**
```
```
