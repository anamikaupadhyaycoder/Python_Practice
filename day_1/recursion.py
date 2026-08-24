#function 
def greet(name):
    print("hello", name)

greet("Aayushi")
greet("Isha")

#1. Write a function called square that takes a number and prints its square.
def square(a):
    return a**2

r = square(2)
print(r)

#2. Create a function called add that:takes two numbers, adds them, returns the result. Then call it with 10 and 20 and print the result.
def add(a, b):
    add = a+b
    print(add)
    return add

add(10,20)

#3. Write a function called multiply that:Takes two numbers a and b, Multiplies them, Returns the result, Outside the function, store the returned result in a variable called result, Print result. 
def multiply(a,b):
    multiply=a*b
    return multiply

result=multiply(6,7)
print(result)

#4. Write a function called greet that takes one parameter called name and prints:
def greet(name):
    return "aayushi"

n = greet("a")
print(n)

#5. Write a function:take a number n, if the number is even, return "Even", otherwise, return "Odd".
def check_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

check = check_even(7)
print(check)

#6. Create a function called largest that takes three numbers:and returns the largest number.
def largest(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

l = largest(20, 25, 15)
print(l)