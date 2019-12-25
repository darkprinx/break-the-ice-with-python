
# Question 1

### **Question:**

> ***Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.***

--------------------------------------
### Hints: 
> ***Consider use range(#begin, #end) method.***

---------------------------------------

**Main author's Solution: Python 2**
```python
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)
```
----------------------------------------

**My Solution: Python 3**
```python
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")
```
-------------------------------

# Question 2

### **Question:**

> ***Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
Then, the output should be:40320***

--------------------
### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

---------------
**Main author's Solution: Python 2**
```python
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(raw_input())
print fact(x)
```
------------
**My Solution: Python 3**

* **Using While Loop**
    ```python
    n = int(raw_input()) #input() function takes input as string type
                         #int() converts it to integer type
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i;
        i = i + 1
    print(fact)
    ```
 * **Using For Loop**
    ```python
    n = int(input()) #input() function takes input as string type
                    #int() converts it to integer type
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
    ```
 * **Using Lambda Function**
    ```python
    # Solution by:  harshraj22
    
    n = int(input())
    def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
    print(shortFact(n))

    ```
-------------------

# Question 3

### **Question:**

>***With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8***

>***Then, the output should be:***
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```
------------------

### Hints: 
>***In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()***

-----------------

**Main author's Solution: Python 2**
```python
n = int(raw_input())
d = dict()
for i in range(1,n+1):
    d[i] = i * i
print d
```

**My Solution: Python 3:**
```python
n = int(input())
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)
```
**OR**
```python
# This is done with dictionary comprehension method
n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)
```
----------------------------------

## Conclusion
***These was the solved problems of day 1. The above problems are very easy for the basic syntex learners.I have shown some easy ways of coding in my solutions. Lets see how to face and attack new problems in the next day.***

[***go to next day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%202.md "Next Day")



[***Discussion***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
