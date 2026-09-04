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
print(result)

#Question 5-
from functools import reduce
numbers=[1,2,3,4,5,6,7,8]
result=reduce(lambda a,b:a+b, map(lambda n:n**2, filter(lambda n:n%2==0, numbers)))
print(result)'''


#3-9-2026
#
'''def tuple_stats(numbers):
    total=0
    largest_num=None
    smallest_num=None
    for num in numbers:
        total+=num
        if largest_num is None or num>largest_num:
            largest_num=num
        if smallest_num is None or num<smallest_num:
            smallest_num=num
    return largest_num, smallest_num, total
result=tuple_stats((12,5,8,20,3))
print(result)

#
def count_even_odd(numbers):
    count_even=0
    count_odd=0
    for num in numbers:
        if num%2==0:
            count_even+=1
        else:
            count_odd+=1
    return count_even, count_odd
result=count_even_odd((4,7,10,13,20,21))
print(result)

#
def analyze_text(text):
    count_upper=0
    count_lower=0
    count_digit=0

    for char in text:

        if char.isupper():
            count_upper+=1
        elif char.islower():
            count_lower+=1
        elif char.isdigit():
            count_digit+=1
            
    return  count_upper, count_lower, count_digit
result=analyze_text(("PyThOn123"))
print(result)

def number_analysis(numbers):
    sum_even=0
    sum_odd=0
    largest_even=None
    for num in numbers:
        if num%2==0:
            sum_even+=num
        elif num%2!=0:
            sum_odd+=num
        if num%2==0:
            if largest_even is None or num>largest_even:
                largest_even=num
    return sum_even, sum_odd, largest_even
result=number_analysis((12,5,8,15,20,7,30))
print(result)

#
def analyze_numbers(numbers):
    postitive_count=0
    negative_count=0
    zero_count=0
    positive_sum=0
    for num in numbers:
        if num>0:
            postitive_count+=1
        elif num<0:
            negative_count+=1
        else:
            zero_count+=1
        if num>0:
            positive_sum+=num
    return postitive_count, negative_count, zero_count, positive_sum
result=analyze_numbers((12,-5,8,-10,15,0,7,-3))
print(result)

#
def filter_numbers(numbers):
    even_numbers=[]
    number_greater_15=[]
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
        if num>15:
            number_greater_15.append(num)
       
    return tuple(even_numbers), tuple(number_greater_15)
result=filter_numbers((4,15,8,21,10,33,6,17))
print(result)

#
def analyze_words(words):
    num_words=len(words)
    num_words_more_than_4=0
    num_uppercase=0
    longest_word=None
    for char in words:
       
        if len(char)>4:
            num_words_more_than_4+=1

        if char.isupper():
            num_uppercase+=1

        if longest_word is None or len(char)>len(longest_word):
            longest_word=char

    return num_words, num_words_more_than_4, num_uppercase, longest_word
result=analyze_words(("python", "JAVA", "Code", "developer", "AI"))
print(result)

#
def porcess_tuple(numbers):
    even_list=[]
    greater_than_8=[]
    total=0
    for num  in numbers:
        total+=num
        if num%2==0:
            even_list.append(num)
        if num>8:
            greater_than_8.append(num)
    return total, tuple(even_list), tuple(greater_than_8)
result=porcess_tuple((4,7,2,9,12,15,6))
print(result)

#

def modify_tuple(numbers):
    seen=[]
    unique=[]
    duplicates=[]
    duplicate_count=0
    for num in numbers:
        if num not in seen:
            seen.append(num)
            unique.append(num)
        else:
            duplicate_count+=1

            if num not in duplicates:
                duplicates.append(num)
               
    return tuple(unique), tuple(duplicates), duplicate_count
result=modify_tuple((3,8,3,12,5,8,15,3))
print(result)

#remove duplicate characters

def remove_duplicats(text):
    seen=[]
    
    for char in text:
        if char not in seen:
            seen.append(char)
       
    return "".join(seen)
result=remove_duplicats("programming")
print(result)

#
def separate_characters(text):
    only_letters=""
    only_digits=""
    for char in text:
        if char.isdigit():
            only_digits+=char
        else:
            only_letters+=char
    return only_letters, only_digits
results=separate_characters("PyThOn123")
print(results)

#
def process_words(words):
    upper_more_3=[]
    lower_less_3=[]
    for char in words:
        if len(char)>3:
            upper_more_3.append(char.upper())
        if len(char)<=3:
            lower_less_3.append(char.lower())
    return upper_more_3, lower_less_3
result=process_words(["python", "JAVA", "code", "AI", "developer"])
print(result)

#
def word_lenghts(words):
    empty_list=[]

    for char in words:
        w=len(char)
        empty_list.append(w)
    return empty_list
result=word_lenghts(["cat", "python", "AI", "developer"])
print(result)

#
def find_words(words, target):
    empty_list=[]
    for index,item in enumerate(words):
        if item==target:
            empty_list.append(index)
    return empty_list
result=find_words(["python", "java", "javascript", "html", "python"], "html")
print(result)

#
def categorize_words(words):
    words_5=[]
    words_3_to_5=[]
    words_2=[]
    for char in words:
        if len(char)>5:
            words_5.append(char)
        elif 3<=len(char)<=5:
            words_3_to_5.append(char)
        elif len(char)<=2:
            words_2.append(char)
    return words_5, words_3_to_5, words_2
result=categorize_words(["cat", "elephant", "AI", "python", "sun"])
print(result)'''

#
def process_numbers(numbers):
    sum_3=0
    sum_5=0
    count_3_5=0
    for num in numbers:
        if num%3==0:
            sum_3+=num
        if num%5==0:
            sum_5+=num
        if num%3==0 and num%5==0:
            count_3_5+=1
    return sum_3, sum_5, count_3_5
result=process_numbers((4,7,12,15,20,9,30))
print(result)
    






    

        


