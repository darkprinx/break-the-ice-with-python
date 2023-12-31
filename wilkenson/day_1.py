# solution by wilkensoncode
# Q1
def find_number_divisible(start: int, end: int) -> int:
    for num in range(start, end + 1):
        if num % 7 == 0 and not num % 5 == 0:
            print(num, end=",")
    print()


find_number_divisible(2000, 3200)

# using while loop
# Q2
number = (int)(input("Enter a number to get its factorial: "))


def factorial():
    factorial = 1
    incre = 1
    while incre <= number:
        factorial = factorial * incre
        incre += 1


factorial(number)

# using recursion


def r_factorial(num: int):
    if num == 1:
        return num
    if num <= 0:
        return
    return num * factorial(num - 1)


number = (int)(input("Enter a number to get its factorial: "))
r_factorial(number)

# using for loop


def for_factorial():
    fact = 1
    for i in range(1, 1 + int(input('Enter a number to get factorial: '))):
        fact = fact * i
    fact


for_factorial()


# lambda soluion
def factorial(x): return 1 if x == 0 else x * factorial(x - 1)


factorial(5)

m = (int)(input("enter number get factorial: "))
factorial(m)

#  Q3 solution
n = (int)(input())

book = {}

for i in range(1, n + 1):
    book[i] = i*i

book


#  dict comprehension
{x: x * x for x in range(1, 1 + int(input()))}
