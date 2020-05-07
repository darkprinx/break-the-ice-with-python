# Question 70

### **Question**

> **_Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension._**

---

### Hints

> **_Use random.choice() to a random element from a list._**

---



**Solutions: **

```python
import random
resp = [i for i in range(0,11,2)]
print(random.choice(resp))
```

---

# Question 71

### **Question**

> **_Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension._**

---

### Hints

> **_Use random.choice() to a random element from a list._**

---



**Solutions: **

```python
import random
resp = [i for i in range(10,151) if i % 35 == 0 ]
print(random.choice(resp))
```

---

# Question 72

### **Question**

> **_Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive._**

---

### Hints

> **_Use random.sample() to generate a list of random values._**

---



**Solutions: **

```python
import random
resp = random.sample(range(100,201),5)
print(resp)
```

---

# Question 73

### **Question**

> **_Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive._**

---

### Hints

> **_Use random.sample() to generate a list of random values._**

---



**Solutions: **

```python
import random
resp = random.sample(range(100,201,2),5)
print(resp)
```

---

# Question 74

### **Question**

> **_Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive._**

---

### Hints

> **_Use random.sample() to generate a list of random values._**

---



**Solutions: **

```python
import random
lst = [i for i in range(1,1001) if i%35 == 0]
resp = random.sample(lst,5)
print(resp)
```

---

[**_go to previous day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_17.md "Day 17")

[**_go to next day_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/blob/master/Status/Day_19.md "Day 19")

[**_Discussion_**](https://github.com/darkprinx/100-plus-Python-programming-exercises-extended/issues/3)
