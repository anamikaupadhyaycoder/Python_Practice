'''#prints all Fibonacci numbers less than or equal to 100
a = 0
b = 1

while a<=100:
    print(a)
    a,b = b,a+b

fact = 1

num = int(input("enter a number:"))
i = 1
while i <=num:
    fact*=i
    i+=1

print(fact)

n = int(input("enter a number:"))
fact = 1

for i in range(n):
    fact *= (i+1)
print(fact)

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(4-1-i):
        print(" ", end=" ")
        for z in range(i+1):
            print("*", end=" ")
    print()

num = 1

for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()

for i in range(4):
    for j in range(i):
        print("", end=" ")
    
    if i==0:
        for x in range(1,5):
            print(x, end=" ")
    
    elif i == 1:
        print(2, end=" ")
        print(3, end=" ")
        print(2, end=" ")

    elif i == 2:
        print(3, end=" ")
        print(2, end=" ")

    else:
        print(4, end=" ")

    print()

for i in range(5):
    for j in range(4-i):
        print(" ", end=" ")
    
    for x in range(i+1):
        print(x+1, end=" ")
    print()


for i in range(4):
    for j in range(i+1):
        print(j+1, end=" ")

    for x in range(i, 0, -1):
        print(x, end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(65+i+j), end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(68-j), end=" ")
    print()

for i in range(4):
    for j in range(i+1, 0, -1):
        print(chr(64+j), end=" ")
    print()

1
2 2 
3 3 3 
4 4 4 4 
3 3 3
2 2
1
for this code
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(3, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

#write a program to print all factors of a number entered by the user. 
num = int(input("enter a number: "))
for i in range(1, num+1):
    if num%i==0:
        print(i, end=" ")

#write a program to find factorial of number entered by user. 
num = int(input("enter a number: "))

fact = 1

for i in range(1, num+1):
    fact*=i
print("Factorial: ", fact)

#write a program to count how many factors a number has. 

num = int(input("enter a number:"))

count = 0 

for i in range(1, num + 1):
    if num%i==0:
        count+=1
print("number of factors:", count)

#write a program to check whether a nmber is prime or not.
num = int(input("enter a number:"))

count = 0

for i in range(1, num+1):
    if num%i == 0:
        count+=1
if count == 2:
    print("prime number")
           
else:
    print("not prime")


#write a program to print all prime numbers between 1 an 50. 
for num in range(1, 51):
    count = 0 

    for i in range(1, num+1):
        if num%i== 0:
            count+=1
    if count == 2:
       print(num, end=" ")

space = 0

for i in range(9, 0, -2):

    for j in range(space):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

    space += 1
#for a hollow square
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#for a hollow triangle
for i in range(5):
    for j in range(i + 1):

        if j == 0 or j == i or i == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#Palindrome Pattern 
for i in range(5):
    for j in range(i+1):
        print(j+1, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#Number pyramid
for i in range(5):
    for j in range(4-i):
        print("", end=" ")

    for j in range(i+1):
        print(j+1, end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()

#Write a program that:Prints all factors of 24

num = 24

for i in range(1, num+1):
    if num%i == 0:
      print( i, end=" ")

#Instead of printing the factors, let's count how many factors a number has.
num = int(input("enter a number: "))

count = 0 

for i in range(1, num+1):
    if num%i == 0:
        count+=1
print(count)

#Write a program that takes a number from the user and calculates the sum of all its factors.
num = int(input("enter a number:"))

sum = 0 

for i in range(1, num+1):
    if num%i == 0:
        sum+=i
print(sum)

#write a program to find the factorial of number entered by user. 
num = int(input("enter a number:"))

fact = 1

for i in range(1, num+1):
    fact*=i
print(fact)

#write a program to find whether the number is prime or not. 

num = int(input("enter a number:"))

count = 0 

for i in range (1, num+1):
    if num%i == 0:
        count+=1
if count == 2:
    print("it's a prime", num)
else:
    print("it's not a prime", num)

#Next challenge: Prime Numbers in a Range 🔥

for num in range(1, 21):
    count = 0 

    for i in range(1, num+1):
        if num%i == 0:
            count+=1
    if count == 2:
        print(num, end=" ")

#write a program for perfect numbers. 
num = int(input("enter a number:"))

total = 0 

for i in range(1, num):
    if num%i==0:
        total+=i

if total == num:
    print("it's a perfect number")
else:
    print("it's not a perfect number")

#write a program to perform a armstrong number. 
num = int(input("Enter a number:"))

original = num

total = 0 

while num>0:
    digit = num%10
    total+=digit**3
    num//=10
if total == original:
    print("number is a armstrong number")
else:
    print("number is not a armstrong number")

#Write a program for a strong number
num = int(input("enter a number:"))

original = num

total = 0 

while num>0:
    digit = num%10
    fact = 1

    for i in range(1, digit+1):
        fact*=i
    
    total+=fact
    num//=10
if total == original:
    print("it's a strong number")
else:
    print("it's not a strong number")

#write a program that finds the HCF of 12 and 18 using a for loop. 
num1 = 12
num2 = 18

HCF = 0 

for i in range(1, 20):
    if num1%i==0 and num2%i==0:
        HCF=i
print(HCF)

#write a program that finds the LCM of 4 and 6 using a for loop. 
num1 = 4
num2 = 6



for i in range(1, num1*num2+1):
    if i%num1==0 and i%num2==0:
        print(i)
        break

#write a program that takes a number from the user and counts its digits using a while loop. 
num = int(input("enter a number:"))
    
count = 0

while num>0:
    digits = num%10
    count+=1
    num//=10
print(count)

#write a program that takes a number from ther user and perform sum of digits using a while loop. 
num = int(input("enter a number:"))

total = 0 

while num>0:
    digits = num%10
    total+=digits
    num//=10
print(total)

#write a program that takes a number from the user and find the product of its digits.
num = int(input("enter a number:"))

product = 1

while num>0:
    digits = num%10
    product*=digits
    num//=10
print(product)

#write a program that takes a number and print reverse of the number using while loop. 
num = 1234

reverse = 0 

while num>0:
    digit = num%10
    reverse = reverse*10+digit
    num//=10
print(reverse)

#write a program to find whether the number is palindrome or not. 

num = int(input("enter a number:"))

original = num

reverse = 0 

while num>0:
    digit = num%10
    reverse = reverse*10+digit
    num//=10

if reverse == original:
    print("Number is a palindrome number.")
else:
    print("Number is not a palindrome number.")

#write a program that takes a number from the user and prints:First digit and Last digit.
num = int(input("enter a number:"))


First_digit = 0
Last_digit = 0

Last_digit = num%10

while num>10:
    num//=10
    First_digit = num
print(First_digit)
print(Last_digit)

#Take a number form the user and remove its last digit repeatedly, printing the number each time. 
num = int(input("enter a number:"))

while num>0:
    print(num)
    num//=10

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} * {j} =", i*j)
    print()

for i in range(1, 4):
    for j in range(1, 4):
        print(i,j)
#Write a Python program using nested for loops to generate all pairs (i, j) where:i ranges from 1 to 3
#j ranges from 1 to 3
#Print the pair only when i + j is even


for i in range(1, 4):
    for j in range(1, 4):
        if (i+j)%2==0:
           print(f"{i}, {j}=", i+j)


#Write a program using nested for loops to print all pairs (i, j) where:

#Write a program using nested for loops to print all pairs (i, j) where:i goes from 1 to 5
#j goes from 1 to 5
#Print the pair only if i x j is divisible by 3
    
for i in range(1, 6):
    for j in range(1, 6):
        if (i*j)%3==0:
            print(i,j)

13-08-2026
#write a program that prints the larger number between each paira: (5,3) (2,8)(7,7)(10,10)
pairs = [(5,3), (2,8), (7,7), (10,4)]
for a, b in pairs:
    if a>=b:
        print(a)
    else:
        print(b)

#Try writing this yourself without looking at my complete code:

pairs = [(4, 9), (12, 6), (3, 3), (15, 20)]

for a, b in pairs:
    if a>=b:
        print(a)
    else:
        print(b)

#Write a program that prints the even numbers from 1 to 5 for each row:
for i in range(1,6):
    for j in range(1, i+1):
        if (j*2)%2==0:
           print(j*2 ,end=" ")
    print( )'''

for i in range(1,6):
    for j in range(1,2*i, 2):
        if j%2!=0:
           print(j ,end=" ")
    print( )
















































































































































