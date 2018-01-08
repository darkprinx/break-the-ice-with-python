# Question 16
### Level 2
--------------------

**Question:**

***Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.***
***Suppose the following input is supplied to the program:***

```1,2,3,4,5,6,7,8,9```

***Then, the output should be:***

```1,3,5,7,9```

----------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.

-------------------
**Main author's Solution: Python 2**
```
values = raw_input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print ",".join(numbers)
```
----------------
**My Solution: Python 3**
```
lst=[i for i in input().split(',') if int(i)%2]
print(",".join(lst))
```
------------------------


# Question 17
### Level 2
--------------------

**Question:**

***Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:***

```
D 100
W 200
```
* D means deposit while W means withdrawal.

***Suppose the following input is supplied to the program:***
```
D 300
D 300
W 200
D 100
```
***Then, the output should be:***
```
500
```
----------------------
### Hints:
#### In case of input data being supplied to the question, it should be assumed to be a console input.

-------------------
**Main author's Solution: Python 2**
```
import sys
netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount
```
----------------
**My Solution: Python 3**
```
```
