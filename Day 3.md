# Question 10
### Level 2
--------------------

**Question:**

***Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.***

***Suppose the following input is supplied to the program:***

```hello world and practice makes perfect and hello world again```

***Then, the output should be:***

```again and hello makes perfect practice world```

----------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.

-------------------
**Main author's Solution: Python 2**
```
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
```
----------------
**My Solution: Python 3**
```
word=input().split()

for i in word:
    if word.count(i)>1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))
```
**OR**
```
word=input().split()
[word.remove(i) for i in word if word.count(i)>1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))
```
**OR**
```
word=sorted(list(set(input().split())))   #  input string splits -> converting into set() to store unique
                                          #  element -> converting into list to be able to apply sort 
print(" ".join(word))
```
---------------------------
# Question 11
### Level 2
--------------------

**Question:**

***Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.***

***Example:***

```0100,0011,1010,1001```

***Then the output should be:***

```1010```

***Notes: Assume the data is input by console.***

----------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.

-------------------
**Main author's Solution: Python 2**
```
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)
```
----------------
```
def check(x):        # converts binary to integer & returns zero if divisible by 5
    total=0
    pw=1
    reversed(x)

    for i in x:
        total+=pw*(ord(i)-48)
        pw*=2
    return total%5

data=input().split(",")    # inputs taken here and splited in ',' position
lst=[]

for i in data:
    if check(i)==0:
        lst.append(i)

print(",".join(lst))
```
