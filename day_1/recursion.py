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
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

l = largest(20, 25, 15)
print(l)
#25-08-2026

#1. Write a function called welcome that:takes name as a parameter, has "Guest" as the default value, prints Welcome followed by the name. 
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Aayushi")

#def calculate(a, b=10):The function should add a and b and print the result.Then call it:calculate(5), calculate(5, 20).
def calculate(a, b=10):
    return a+b

total = calculate(5)
print(total)

add = calculate(5,20)
print(add)

#def order(item, quantity=1, price=100):It should return the total cost:quantity × price, Then test these three calls:order("Book"), order("Book", 3), order("Book", 3, 150) Print each result.
def order(item, quantity=1, price=100):
    return quantity*price

i=order("book")
print(i)

q=order("book", 3)
print(q)

p=order("book", 3, 150)
print(p)

#
def calculate_bill(item, price, quantity=1, discount=0):
    total = price*quantity
    dis = total-discount
    return dis

p= calculate_bill("Book", 200)
print(p)

a= calculate_bill("Book", 200, 3)
print(a)

b= calculate_bill("Book", 200, 3, 50)
print(b)

#
def profile(name, age=18, city="Delhi"):
    print(name, age, city)
   
profile(city="Mumbai", name="Aayushi")

#
def laptop(brand, price=50000, ram=8):
    print(brand, price, ram)

laptop(ram=16, brand="Dell")
#laptop(brand="Dell", 50000, ram=16)

def total(*args):

    add=0

    for i in args:
        add=add+i

    return add

r=total(10,20)
print(r)

t=total(10,20,30)
print(t)

s=total(5,10,15,20,25)
print(s)

#
#def largest(*args):It should find and return the largest number given to the function. largest(10, 25, 15), largest(50, 12, 80, 35).
    
def largest(*args):
    largest_num=None
    for i in args:
        if largest_num is None or i>largest_num:
            largest_num=i
    return largest_num

t=largest(10,25,15)
print(t)

p=largest(50,12,80,35)
print(p)

#def count_even(*args):It should count how many even numbers were given.count_even(10, 15, 20, 25, 30)
def count_even(*args):

    count=0

    for i in args:
        if i%2==0:
            count+=1
    return count

c = count_even(2, 5, 9, 8, 9, 4)
print(c)

#26-8-2026
#def student_info(**kwargs):Inside the function, simply print kwargs.student_info(name="Aayushi", age=18, course="Python")
def student_info(**kwargs):
    print(kwargs)

student_info(name="Aayushi", age=18, course="python")

#def show_info(**kwargs):Inside the function, use a for loop to print each key and value like:name : Aayushi age : 18 course : Python
def show_info(**kwargs):
    for key,value in kwargs.items():
        print(key, ":", value)

show_info(name="Aayushi", age=18, course="Python")

#You can use both in the same function:def show(*args, **kwargs):print(args) print(kwargs).Now call:show(10, 20, 30, name="Aayushi", age=18)
def show(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

show("aayushi", 10, 20, 30, age=18, course="Python")

#
name="aayushi"
def greet():
    name="Aayushi"
    print(name)

greet()
print(name)

count = 5

def increase():
    global count
    count+=1

increase()
print(count)

#write a function: def square(n): it should return the square of n. then call it with:square(5)
def square(n):
    return n**2

s=square(5)
print(s)

#write a function:def power(n, exponent=2):it should return n raised to exponent. test it with: power(5) and power(5,3)
def power(n, exponent=2):
    return n**exponent

s=power(5)
print(s)
p=power(5,3)
print(p)

#write a fucntion:def check_even(n):it should return "even" if n is even. return "odd" is n is odd. 
def check_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

n = check_even(5)
print(n)

def largest(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b 
    else:
        return c

n = largest(25, 25, 15)
print(n)

#write def sum_numbers(*args): it should return the sum of any number of numbers.
def sum_numbers(*args):
    add=0
    for i in args:
        add+=i
    return add
s=sum_numbers(10,20)
print(s)

#write a function:def get_age(**kwargs): it should return tthe value of "age" form the keyword arguments. 
def get_age(**kwargs):
    return kwargs["age"]
    
s=get_age(name="aayushi", age=18, i=29)
print(s)


