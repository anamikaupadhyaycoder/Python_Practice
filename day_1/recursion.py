#part 4 Funcitons calling another functions. 
#1. create these two functions: and return the price after adding tax.

'''def calculate_total(price, tax):
    return price+tax

def calculate_discounted_total(price, tax, discount):
    s=calculate_total(price, tax)-discount
    return s
result=calculate_discounted_total(100,10,20)
print(result)

#2. Now let's make the function chain three levels deep. 
def calculate_total(price, tax):
    return price+tax

def apply_discount(total, discount):
    return total-discount

def final_price(price, tax, discount):
    s=calculate_total(price, tax)
    r=apply_discount(s, discount)
    return r
result= final_price(100,10,20)
print(result)

#3. 
def is_valid_number(n):
    if n>0:
        return True
    else:
        return False

def process_number(n):
    if is_valid_number(n):
        return n*2
    else:
        return 0 
result=process_number(2)
print(result)

#4. 
def get_square(n):
    return n**2

def is_even(n):
    return n%2==0

def process_number(n):
    s=get_square(n)
    if is_even(s):
        return s
result=process_number(4)
print(result)

#5. function chain

def add_bonus(score):
    return score+10

def is_pass(score):
    if score>=40:
        return True
    else:
        return False

def final_result(score):
    s=add_bonus(score)
    if is_pass(s):
        return "Pass"
    else:
        return "Fail"
result=final_result(35)
print(result)

#question 6 
def get_largest(numbers):
    largest_num=None
    for num in numbers:
        if largest_num is None or num >largest_num:
            largest_num=num
    return largest_num

def double_number(n):
    return n*2

def process_number(numbers):
    s=get_largest(numbers)
    r=double_number(s)
    return r
result=process_number([4, 9, 2, 7])
print(result)

#7. 
def count_even(numbers):
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    return count

def calculate_average(numbers):
    total=0
    count=0
    for num in numbers:
        total+=num
        count+=1
    avg=total/count
    return avg

def analyze_numbers(numbers):
    r=count_even(numbers)
    s=calculate_average(numbers)
    return r, s
result=analyze_numbers([10,15,20,25,30])
print(result)


#6-09-2026
#
def find_sum(numbers):
    total=0
    for num in numbers:
        total+=num
    return total

def find_average(numbers):
    count=0
    s=find_sum(numbers)
    for num in numbers:
        count+=1
    avg=s/count
    return avg

def analyze_numbers(numbers):
    s=find_sum(numbers)
    r=find_average(numbers)
    return s,r
result=analyze_numbers([2,3,4])
print(result)

#
def count_vowels(text):
    count_v=0
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            count_v+=1
    return count_v

def count_consonats(text):
    count_c=0
    vowels="aeiouAEIOU"
    for char in text:
        if char.isalpha() and char not in vowels:
            count_c+=1
    return count_c

def analyze_text(text):
    call_1=count_vowels(text)
    call_2=count_consonats(text)
    return call_1, call_2
result=analyze_text("Hello chatgpt")
print(result)

#
def count_vowels(text):
    count_v=0
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            count_v+=1
    return count_v

def count_digits(text):
    count_d=0
    for char in text:
        if char.isdigit():
            count_d+=1
    return count_d

def analyze_text(text):
    s=count_vowels(text)
    e=count_digits(text)
    return s, e
result=analyze_text("hello123")
print(result)

#1. *args/**kwargs
def calculate_sum(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
result=calculate_sum(10,20,30)
print(result)

#2. 
def count_even(*numbers):
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    return count
result=count_even(2,4,1,5,8,3)
print(result)

#3. student Result Analyzer
def analyze_students(*marks, **details):
    total=0
    count=0
    highest_mark=None
    lowest_mark=None
    count_70_or_above=0

    for num in marks:
        total+=num
        count+=1
    avg=total/count
    

    for num in marks:
        if highest_mark is None or num>highest_mark:
            highest_mark=num
        if lowest_mark is None or num<lowest_mark:
            lowest_mark=num
        if num>=70:
            count_70_or_above+=1
    
    return total, avg, highest_mark, lowest_mark, count_70_or_above
result=analyze_students(78,65,91,84,55, name="aayushi", course="python", session=3)
print(result)

#now we'll combine *args+**kwargs+fucntion calling +strings
def count_even(*numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

def process_user(*numbers, **info):
    name=info["name"]
    city=info["city"]
    role=info["role"]

    total=0
    total_10=0
    count_10=0

    s=count_even(*numbers)
    total+=s

    for num in numbers:
        if num>10:
            count_10+=1
            total_10+=num

    username=name.lower()+ "_" +role.lower()
    return name, city, username, total_10, count_10 

result=process_user(12,7,20,15,9,30, name="Aayushi", city="Delhi", role="student", )
print(result)

#smart number analyzer
def analyze(*numbers, **options):
    operation=options["operation"]
    limit=options["limit"]

    count_even=0
    total=0
    for num in numbers:
        if operation=="even":
            if num%2==0:
                count_even+=1

        if num>limit:
            total+=num
    return operation, count_even, total
result=analyze(12, 5, 8, 21, 30, 17, operation="even", limit=15)
print(result)

#
def analyze_student(name, *marks, **details):
    total=0
    count=0
    for num in marks:
        total+=num
        count+=1
    avg=total/count
    return name, total, avg, details
result=analyze_student("Aayushi", 2, 5, 3, 6, 2, info="student", course="python")
print(result)


def analyze_numbers(*numbers, **options):

    total=0
    largest_num=None
    smallest_num=None
    count_even=0
    count_odd=0

    for num in numbers:
        total+=num
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
        if options.get("even", False) and num%2==0:
            count_even+=1
        if options.get("odd", False) and num%2!=0:
            count_odd+=1
            
    return total, largest_num, smallest_num, count_even, count_odd
result=analyze_numbers(10,15,22,7,8,31, even=True, odd=False)
print(result)

#
def analyze_numbers(*numbers, **options):

    greater_than=options["greater_than"]

    total=0
    largest_num=None
    smallest_num=None
    count_even=0
    count_odd=0
    count_num_greater_than_value=0

    for num in numbers:
        total+=num
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
        if options.get("even", False) and num%2==0:
            count_even+=1
        if options.get("odd", False) and num%2!=0:
            count_odd+=1
        if num>greater_than:
            count_num_greater_than_value+=1
        
    return total, largest_num, smallest_num, count_even, count_odd, count_num_greater_than_value
result=analyze_numbers(10,20,5,18,25,7, even=True, odd=True, greater_than=15)
print(result)

#
def analyze_numbers(*numbers, **options):
    total=0
    largest_num=None
    smallest_num=None
    count_even=0
    count_odd=0
    count_greater=0
    count_less=0
    greater_than= options.get("greater", 0) 
    less_than=options.get("less", 0)

    for num in numbers:
        total+=num
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
        if options.get("even", False) and num%2==0:
            count_even+=1
        if options.get("odd", False) and num%2!=0:
            count_odd+=1
        if num>greater_than:
            count_greater+=1
        if num<less_than:
            count_less+=1 
    return total, largest_num, smallest_num, count_even, count_odd, count_greater, count_less
result=analyze_numbers(10,20,5,18,25,7, even=True, odd=False, greater=15, less=10)
print(result)

#Part 6 Lambda+Functions:
#1. create a lambda function that takes a number and returns its square. 
square=lambda n:n**2
print(square(5))

#create a lambda function called add that takes two numbers and returns their sum. 
total=lambda a, b:a+b
print(total(10,20))

#create a lambda function to check : if number is even or if number is odd. 
check_even=lambda n: "Even" if n%2==0 else "Odd"
print(check_even(7))

#create a lambda function that use map() to create a new list of the squares of all number. 
numbers=[1,2,3,4,5]

check=map(lambda num:num**2, numbers)
print(list(check))

#create a lambda function that use map() and a lambda to add 5 to every number. 
numbers=[2,4,6,8,10]
total=map(lambda num:num+5, numbers)
print(list(total))

#create a function that use filter() and a lambda to get only the even numbers. 
numbers=[3,8,11,14,17,20,25]
even_num=filter(lambda n:n%2==0 , numbers)
print(list(even_num))

#use filter() and lambda to get only numbers greater than 4. 
numbers=[1,2,3,4,5,6,7,8,9]
grea=filter(lambda num:num>4, numbers)
print(list(grea))

#use filter()+lambda+map() to select only even num and then square of those num. 
number=[1,2,3,4,5,6,7,8,9,10]
check=map(lambda num: num**2,  filter(lambda num:num%2==0, number))
print(list(check))

#use filter()+map()+lambda to get num greater than 5 and multiply them by 3. 
numbers=[1,2,3,4,5,6,7,8,9,10]
check=map(lambda num:num*3, filter(lambda num:num>5, numbers))
print(list(check))

#use filter()+map()+condition to keep only num divisible by 3 and then square. 
numbers=[3,7,10,12,15,18,21,24]
to_keep=map(lambda num:num**2, filter(lambda num: num%3==0, numbers))
print(list(to_keep))

#use filter()+map()+lambda to: keep only num greater than 10 and then multiply them by 2. 
numbers=[2,5,8,11,14,17,20,23]
lam=map(lambda num:num*2, filter(lambda num: num>10, numbers))
print(list(lam))

#use filter()+map()+condition 
numbers=[1,4,7,10,13,16,19,22]
result=map(lambda num:num+10, filter(lambda num: num%2==0, numbers))
print(list(result))

#use filter()+map()+lambda to:keep numbers divisible by 5 and greater than 15 then divide each num by 5. 
numbers=[5,10,15,20,25,30,35]
result=map(lambda n: n/5, filter(lambda n: n%5==0 and n>15, numbers))
print(list(result))

#use reduce()+lambda
from functools import reduce
numbers=[1,2,3,4,5]
result=reduce(lambda a, b:a*b, numbers)
print(result)'''

#use filter()+map()+reduce()+lambda
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]
result=reduce(lambda a,b:a+b, map(lambda n:n**2, filter(lambda n:n%2==0, numbers)))
print(result)