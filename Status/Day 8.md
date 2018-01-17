# Question 22
### Level 3
--------------------

**Question:**

***Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.***

***Suppose the following input is supplied to the program:***

```New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.```

***Then, the output should be:***
```
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
```

----------------------
#### Hints
##### In case of input data being supplied to the question, it should be assumed to be a console input.

-------------------
**Main author's Solution: Python 2**
```
freq = {}   # frequency of words in text
line = raw_input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print "%s:%d" % (w,freq[w])
```
----------------
**My Solution: Python 3**
```
ss = input().split()
word = sorted(set(ss))     # split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))
```
**OR**
```
ss = input().split()
dict = {}
for i in ss:
    i = dict.setdefault(i,ss.count(i))    # setdefault() function takes key & value to set it as dictionary.

dict = sorted(dict.items())               # items() function returns both key & value of dictionary as a list
                                          # and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d"%(i[0],i[1]))
```
**OR**
```
ss = input().split()
dict = {i:ss.count(i) for i in ss}     # sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
dict = sorted(dict.items())            # items() function returns both key & value of dictionary as a list
                                       # and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d"%(i[0],i[1]))       
```
**OR**
```
from collections import Counter

ss = input().split()
ss = Counter(ss)         # returns key & frequency as a dictionary
ss = sorted(ss.items())  # returns as a tuple list

for i in ss:
    print("%s:%d"%(i[0],i[1]))
```
---------------
# Question 23
### level 1

**Question:**

***Write a method which can calculate square value of number***

----------------------
### Hints: Using the ** operator which can be written as n**p where means n^p

-------------------
**Main author's Solution: Python 2**
```
def square(num):
    return num ** 2

print square(2)
print square(3)
```
----------------
**My Solution: Python 3**
```
n=int(input())
print(n**2)
```
---------------------
