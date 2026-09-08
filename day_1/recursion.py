
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

#part 7 Final Functions Test
#Q1. 
def analyze_numbers(*numbers): 
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
        if num%2==0:
            count_even+=1
        else:
            count_odd+=1
    return total, largest_num, smallest_num, count_even, count_odd
result=analyze_numbers(10,5,8,3,12,7)
print(result)

#Q2. 
def analyze_even_num(*numbers):
    total_even=0
    largest_even=None
    smallest_even=None
    count_even=0
    

    for num in numbers:
        if num%2==0:
            if largest_even is None or num>largest_even:
                largest_even=num
            if smallest_even is None or num<smallest_even:
                smallest_even=num
        if num%2==0:
            total_even+=num
            count_even+=1
    return total_even, largest_even, smallest_even, count_even, 
result=analyze_even_num(7, 12, 5, 8, 3, 20, 11, 4)
print(result)


#Q3. 
def analyze_num(*numbers):
    total_positive=0
    total_negative=0
    count_positive=0
    count_negative=0
    count_zero=0

    for num in numbers:
        if num>0:
            total_positive+=num
            count_positive+=1
        elif num<0:
            total_negative+=num
            count_negative+=1
        elif num==0:
            count_zero+=1
    return total_positive, total_negative, count_positive, count_negative, count_zero
result=analyze_num(10,-5,0,8,-3,0,12,-7)
print(result)

#Q4. 
def student_results(*marks, **details):
    name=details["name"]
    course=details["course"]

    total=0
    count=0
    highest_mark=None
    lowest_mark=None

    for num in marks:
        total+=num
        count+=1
    avg=total/count

    for num in marks:
        if highest_mark is None or num>highest_mark:
            highest_mark=num
        if lowest_mark is None or num<lowest_mark:
            lowest_mark=num
        
    return name, course, total, avg, highest_mark, lowest_mark
result=student_results(85,72,91,68,88, name="Aayushi", course="python", sessio=3)
print(result)

#Q5
def calculate_bill(*prices, discount=0, tax=5):
    sub_total=0
    for num in prices:
        sub_total+=num

    discount=sub_total*discount/100
    total_after_discount=sub_total-discount

    tax=total_after_discount*tax/100
    total_after_tax=total_after_discount+tax

    return sub_total, discount, tax, total_after_tax
result=calculate_bill(100,200,300,discount=10,tax=5)
print(result)

#Q6
def analyze_student(**details):
    name=details["name"]
    age=details["age"]
    marks=details["marks"]

    total=0
    count=0
    highest_mark=None
    smallest_mark=None

    for num in marks:
        total+=num
        count+=1
    avg=total/count

    for num in marks:
        if highest_mark is None or num>highest_mark:
            highest_mark=num
        if smallest_mark is None or num<smallest_mark:
            smallest_mark=num
    if avg>=40:
        status="Pass"
    else:
        status="Fail"

    return name, age, total, avg, highest_mark, smallest_mark, status

result=analyze_student(name="anshika", age="40", marks=[85,72,91,68,88])
print(result)

#Q7. 
def analyze_list(numbers):
    count_even=0
    count_odd=0
    sum_even=0
    sum_odd=0
    largest_num=None
    smallest_num=None

    for num in numbers:
        if num%2==0:
            count_even+=1
            sum_even+=num
        else:
            count_odd+=1
            sum_odd+=num
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
    return count_even, count_odd, sum_even, sum_odd, largest_num, smallest_num
result=analyze_list([12,7,4,9,20,3,15,8])
print(result)

#Q8
def analyze_string(text):
    vowels="aeiouAEIOU"
    count_vowels=0
    count_consonants=0
    count_digits=0
    count_spaces=0

    for char in text:
        if char in vowels:
            count_vowels+=1
        if char.isalpha() and char not in vowels:
            count_consonants+=1
        if char.isdigit():
            count_digits+=1
        if char in " ":
            count_spaces+=1

    return count_vowels, count_consonants, count_digits, count_spaces
result=analyze_string("Python 123 is Great")
print(result)

#Q9
def filter_number(numbers):
    empty_list_even=[]
    empty_list_great_10=[]
    empty_list_3_5=[]
    count_negative=0

    for num in numbers:
        if num<0:
            count_negative+=1
        if num%2==0:
            empty_list_even.append(num)
        if num>10:
            empty_list_great_10.append(num)
        if num%3==0 and num%5==0:
            empty_list_3_5.append(num)
    return empty_list_even,empty_list_great_10,empty_list_3_5,count_negative
result=filter_number([5, 12, -15, 20, 30, -7, 8, 15, 3])
print(result)

#Q10
def calculate_sum(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total

def calculate_avg(*numbers):
    count=0
    for num in numbers:
        count+=1
    sum=calculate_sum(*numbers)
    avg=sum/count
    return avg


def analyze_numbers(*numbers):
    add=calculate_sum(*numbers)
    average=calculate_avg(*numbers)
    return add, average

result=analyze_numbers(10,20,30,40,50)
print(result)

#Q11
def check_numbers(*numbers):
    count_positive_even=0
    count_positive_odd=0
    count_negative_even=0
    count_negative_odd=0
    count_0=0

    for num in numbers:
        if num>0 and num%2==0:
            count_positive_even+=1
        elif num>0 and num%2!=0:
                count_positive_odd+=1
        elif num<0 and num%2==0:
            count_negative_even+=1
        elif num<0 and num%2!=0:
                count_negative_odd+=1
        else:
            count_0+=1
    return count_positive_even ,count_positive_odd, count_negative_even, count_negative_odd, count_0

result=check_numbers(10, -5, 8, -3, 0, 12, -7, -4, 9)
print(result)

#Q12. 
from functools import reduce
numbers=[1,2,3,4,5,6]
lam=reduce(lambda a,b:a+b, map(lambda n: n**2, filter(lambda n:n%2==0, numbers)))
print(lam)

#Q13. 
def analyze_num(*numbers):
    count_posi=0
    count_neg=0
    count_0=0
    largest_num=None
    smallest_num=None
    total=0

    for num in numbers:
        total+=num
        if num>0:
            count_posi+=1
        elif num<0:
            count_neg+=1
        else:
            count_0+=1
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
    return count_posi, count_neg, count_0, largest_num, smallest_num, total
result=analyze_num(10, -5, 8, 0, -3, 12, -7, 4)
print(result)

#Q14. 

from functools import reduce

def student_result(*marks, **options):
    empty_list=[]
    
    for num in marks:
        if options.get("even", False):
            if num%2==0:
                empty_list.append(num)
        else:
            empty_list.append(num)

    if options.get("square", False):
        squaring=map(lambda n:n**2, empty_list)
    else:
        squaring=empty_list
    total=reduce(lambda a,b:a+b, squaring)
    return total
result=student_result(1,2,3,4,5,6, even=True, square=True)
print(result)

#15. 
from functools import reduce
def analyze_data(*numbers, **options):
    number=[]
    count=0
    largest_num=None
    smallest_num=None

    for num in numbers:
        if options.get("even", False):
            if num%2==0:
                number.append(num)
        else:
            number.append(num)
    if options.get("square", False):
        squaring=list(map(lambda n:n**2, number))
    else:
        squaring=number
    total=reduce(lambda a,b:a+b, squaring)

    for num in squaring:
        count+=1
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
    avg=total/count

    return total, count, avg, largest_num, smallest_num
result=analyze_data(1,2,3,4,5,6,even=True, square=True)
print(result)
    


