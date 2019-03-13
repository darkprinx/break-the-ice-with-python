# Question 10

### **Question**

>***Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.***

>***Suppose the following input is supplied to the program:***
```
hello world and practice makes perfect and hello world again
```
>***Then, the output should be:***
```
again and hello makes perfect practice world
```

----------------------

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.***

-------------------
**Main author's Solution: Python 2**
```python
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
```
----------------
**My Solution: Python 3**
```python
word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))
```
**OR**
```python
word = input().split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))
```
**OR**
```python
word = sorted(list(set(input().split())))              #  input string splits -> converting into set() to store unique
                                                       #  element -> converting into list to be able to apply sort 
print(" ".join(word))
```
---------------------------

# Question 11

### **Question**

>***Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.***

>***Example:***
```
0100,0011,1010,1001
```
>***Then the output should be:***
```
1010
```
>***Notes: Assume the data is input by console.***

----------------------

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p,2)
    if not intp % 5:
        value.append(p)

print ','.join(value)
```
----------------
**My Solution: Python 3**
```python
def check(x):                       # converts binary to integer & returns zero if divisible by 5
    total,pw = 0,1
    reversed(x)

    for i in x:
        total+=pw * (ord(i) - 48)   # ord() function returns ASCII value
        pw*=2
    return total % 5

data = input().split(",")           # inputs taken here and splited in ',' position
lst = []

for i in data:
    if check(i) == 0:               # if zero found it means divisible by zero and added to the list
        lst.append(i)

print(",".join(lst))
```
**OR**
```python
def check(x):                   # check function returns true if divisible by 5
    return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
                                # it will be converted to decimal
data = input().split(',')

data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))
```
**OR**
```python
data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))    # lambda is an operator that helps to write function of one line
print(",".join(data))
```
-------------------------

# Question 12

### **Question:**

>***Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.***

----------------------

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0) and (int(s[3])%2 == 0):
        values.append(s)
print ",".join(values)
```
----------------
**My Solution: Python 3**
```python
lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))        
```
**OR**
```python
def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))
```
**OR**
```python
lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i),lst ))   # using lambda to define function inside filter function
print(",".join(lst))
```
-------------------------

# Question 13

### **Question:**

>***Write a program that accepts a sentence and calculate the number of letters and digits.***

>***Suppose the following input is supplied to the program:***

```
hello world! 123
```

>***Then, the output should be:***
```
LETTERS 10
DIGITS 3
```
----------------------

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
s = raw_input()
d = {"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
```
----------------
**My Solution: Python 3**
```python
word = input()
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))
```
**OR**
```python
word = input()
letter,digit = 0,0

for i in word:
    letter+=i.isalpha()         # returns True if alphabet
    digit+=i.isnumeric()        # returns True if numeric

print("LETTERS %d\nDIGITS %d"%(letter,digit))       # two different types of formating method is shown in both solution
```
-----------------
## Conclusion
***All the above problems are mostly string related problems. Major parts of the solution includes string releted functions and comprehension method to write down the code in more shorter form.***

[***go to previous day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%202.md "Day 2")

[***go to next day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%204.md "Day 4")

[***Discussion***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)