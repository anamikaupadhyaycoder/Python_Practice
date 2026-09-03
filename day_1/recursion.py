#Functions+lists
#1. Find the largest number 
'''def find_largest(numbers):
    largest_num=None

    for num in numbers:
        if largest_num is None or num>largest_num:
            largest_num=num
    return largest_num
result=find_largest([10, 25, 8, 42, 18])
print(result)
    
#get even number and build a new list
def get_even_num(numbers):
    empty_list= []
    for num in numbers:
        if num%2==0:
            empty_list.append(num)
    return empty_list
result=get_even_num([10, 3, 8, 7, 12, 5])
print(result)

#square numbers in list
def square_numbers(numbers):
    empty_list=[]
    for num in numbers:
        num=num**2
        empty_list.append(num)
    return empty_list
result=square_numbers([2,4,5,7])
print(result)

#functions calling other functions. 
#1.
def calculate_square(n):
    return n**2

def calculate_cube(n):
    square=calculate_square(n)
    return square*n
result=calculate_cube(4)
print(result)

#2. 
def square(n):
    return n**2

def double_square(n):
    s=square(n)
    return s*2
result=double_square(5)
print(result)

#3. square+cube
def square(n):
    return n**2

def cube(n):
    c=square(n)
    return c*n
result=cube(4)
print(result)

#4. Double+add
def double(n):
    return n*2

def sum(n,x):
    s=double(n)
    return s+x
result=sum(4,2)
print(result)

#5. 
def difference(a=4, b=2):#default parameter
    return a-b

def calculate_difference(a=4, b=2):
    diff = difference(a=6, b=2)#keyword argument replace default paramter 
    return diff*2
result=calculate_difference()
print(result)

#Final functon - calling challenge
def square(n):
    return n**2

def sum(a, b):
    return a+b

def square_sum(a, b):
    s=square(a)
    t=square(b)
    return sum(s, t)
result=square_sum(3,4)
print(result)

#Lambda functions:
#1
cube=lambda n: n**3
print(cube(3))
#2. create a lambda that adds two numbers. 
total=lambda a, b:a+b
print(total(10,20))

#02-09-2026
#write a lambda function for larger number. 
larger=lambda a, b: a if a>b else b
print(larger(10,15))

#write a lambda function called check_number: for positive and negative or zero.
check_number=lambda n: "positive" if n>0 else "negative" if n<0 else "zero"
print(check_number(8))

#we want to crete a new list containing the squares.
numbers=[1,2,3,4,5]
result=list(map(lambda n:n**2, numbers))
print(result)

#use map() + lambda to add 5 to every numbers. 
numbers=[10,20,30,40,50]
result=list(map(lambda n: n+5, numbers))
print(result)

#use map()+lambda to turn every number into :"even" if it's even and "odd" if it's odd. 
numbers=[1,2,3,4,5,6]
result=list(map(lambda n:"Even" if n%2==0 else "odd", numbers))
print(result)

#use map()+lambda to produce:even number, square and odd number, cube
numbers=[1,2,3,4,5,6,7,8]
result=list(map(lambda n: n**2 if n%2==0 else n**3,numbers))
print(result)

#use filter()+lambda to get only the numbers that are greater than 30. 
numbers=[10,15,22,31,40,53,60]
result=list(filter(lambda n: n>30, numbers))
print(result)

#use filter()+lambda to keep only numbers that are: even and greater than 10. 
numbers=[3,7,12,15,20,27,30,41]
result=list(filter(lambda n: n%2==0 and n>10, numbers))
print(result)

#use filter()+lambda to keep numbers that are:divisible by 5 or divisible by 3. 
numbers=[5,12,20,25,30,33,40,45]
result=list(filter(lambda n:n%5==0 or n%3==0, numbers))
print(result)

#first keep only the even numbers, then square them. 
numbers=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda n:n**2, filter(lambda n:n%2==0, numbers)))

print(result)

#use reduce()+lambda to multiply all the numbers together. 
from functools import reduce
numbers=[2,3,4,5]
result=reduce(lambda a,b: a*b, numbers)
print(result)

#use reduce()+lambda to find the largest number. 
from functools import reduce
numbers=[10,20,30,40]
result=reduce(lambda a,b: a if a>b else b, numbers)
print(result)

#question 1-use map()+lambda to divide every number by 2. 
numbers=[2,4,6,8,10]
result=list(map(lambda n: n/2,numbers))
print(result)

#Question 2-use filter()+lambda to keep only numbers that are: greater than 20 and even. 
numbers=[5,12,18,21,30,35,42]
reuslt=list(filter(lambda n:n%2==0 and n>20,numbers ))
print(reuslt)

#Question 3-use reduce()+lambda to find the sum of all numbers. 
from functools import reduce
numbers=[5,10,15,20]
result=reduce(lambda a,b:a+b, numbers)
print(result)

#Question 4-use filter() to keep only numbers divisible by 3 and greater than 10. use map() to multiply those numbers by 2. 

numbres=[3,6,9,12,15,18,21]
result=list(map(lambda n:n*2, filter(lambda n: n%3==0 and n>10, numbres)))
print(result)'''

#Question 5-
from functools import reduce
numbers=[1,2,3,4,5,6,7,8]
result=reduce(lambda a,b:a+b, map(lambda n:n**2, filter(lambda n:n%2==0, numbers)))
print(result)






    

        




    






    

        


