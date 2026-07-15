
#WAF to print the length of a list. (list is the parameter)

numbers = [1, 4, 3, 6, 8, 4, 9]
names = ["anamika", "aayushi", "isha", "riva", "shreya"]

def print_len(list):
    print(len(list))

print_len(numbers)
print_len(names)

#WAF to print the elements of a list in a single line.(list is the parameter)

list1 = ["anamika", "aayushi", "isha", "riva", "shreya"]
 
def print_ele(list1):
    print(list1[0:])

print_ele(list1)


#WAF to find the factorial of n. (n is the parameter)

def find_fac(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    print(fact)

find_fac(5)


#WAF to convert USD to INR

def conv(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD=", inr_val, "INR")


conv(3)