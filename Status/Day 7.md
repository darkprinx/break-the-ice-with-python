# Question 20
### Level 3
--------------------

**Question:**

***Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.***

----------------------
### Hints:
#### Consider use class, function and comprehension 

-------------------
**Main author's Solution: Python 2**
#### ***The solution code for this problem was not as reltive to as the problem mentioned and there was a typing mistake while calling the function.***

----------------
**My Solution: Python 3**
```

class Test:
    def generator(self,n):
        return [i for i in range(n) if i%7==0]   # returns the values as a list if an element is divisible by 7


n=int(input())
num=Test()
lst=num.generator(n)
print(lst)

```
