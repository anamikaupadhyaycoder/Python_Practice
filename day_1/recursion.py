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
print(cube(3))'''
#2. create a lambda that adds two numbers. 
total=lambda a, b:a+b
print(total(10,20))






    






    

        




    






    

        


