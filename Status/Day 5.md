# Question 16

### **Question:**

>***Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.***
>***Suppose the following input is supplied to the program:***

```
1,2,3,4,5,6,7,8,9
```

>***Then, the output should be:***

```
1,9,25,49,81
```

----------------------

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
## The solution by the author is incorrect.Thus it's not included here.
```
----------------
**My Solution: Python 3**
```python
lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))
```

***There were a mistake in the the test case and the solution's whice were notified and fixed with the help of @dwedigital. My warm thanks to him.*** 

------------------------

# Question 17

### **Question:**

>***Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:***
```
D 100
W 200
```
* D means deposit while W means withdrawal.

>***Suppose the following input is supplied to the program:***
```
D 300
D 300
W 200
D 100
```
>***Then, the output should be:***
```
500
```
----------------------

### Hints:
>***In case of input data being supplied to the question, it should be assumed to be a console input.***

-------------------
**Main author's Solution: Python 2**
```python
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
```python
total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)
```
-----------------

```python
'''Solution by: leonedott'''

lst = []
while True:
  x = input()
  if len(x)==0:
    break
  lst.append(x)

balance = 0
for item in lst:
  if 'D' in item:
    balance += int(item.strip('D '))
  if 'W' in item:
    balance -= int(item.strip('W '))
print(balance)
```
------------------------
```python
'''Solution by: AlexanderSro'''

account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = input("How much would you like to deposit? ")
        account = account + int(deposit)
    elif action == "w":
        withdrow = input("How much would you like to withdrow? ")
        account = account - int(withdrow)
    elif action == "b":
        print(account)
    else:
        quit()
```
-----------------

[***go to previous day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%204.md "Day 4")

[***go to next day***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day%206.md "Day 6")

[***Discussion***](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
