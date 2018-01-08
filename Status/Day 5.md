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
```
