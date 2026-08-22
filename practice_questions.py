#while loops
#1. Print numbers from $1$ to $10$ using a while loop.
i=1

while i<=10:
    print(i)
    i+=1

#2. Print numbers from $10$ down to $1$ using a while loop.

i=10

while i>=1:
    print(i)
    i-=1

#3. Keep asking the user for input until they type "exit".

while True:
    user = input("enter a input:")
    if user.lower() == "exit":
        print("Goodbye")
        break

#4. Keep adding user inputs to a sum until the user enters $0$.
total=0

while True:
    user=int(input("Enter a number:"))
    if user==0:
        print(total)
        print("exit")
        break
    total+=user

#5. (Number Guessing): Let a user guess a secret number until they get it correct.
secret_num=25

while True:
    user=int(input("enter a number:"))
    if user==secret_num:
        print("you have guessed the number.")
        break
    
#6. Find the sum of digits of a given integer using a while loop.
num=int(input("enter a number:"))

total=0

while num>0:
    digit=num%10
    total+=digit
    num//=10
print(total)

#7. Reverse a given integer using arithmetic operations in a while loop.

num=int(input("Enter a number:"))

reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print(reverse)

#8. Print the first $N$ terms of the Fibonacci sequence using a loop.
n=int(input("enter a number:"))

a=0
b=1
while a<=n:
    a,b=b,a+b
    print(a)

#9. count the number of digits in an integer by repeatedly dividing by 10 in a loop.

num=int(input("enter a number:"))

count=0

while num>0:
    digit=num%10
    count+=1
    num//=10
print(count)

#10. Find the factorial of a number using a while loop.

num=int(input('enter a number:'))
fact=1
i=1

while i<=num:
    fact*=i
    i+=1
print(fact)

#11. Write a program that acts like a simple ATM, prompting for a PIN until correct.

pin_number=1234

while True:
    pin=int(input("enter a pin number:"))
    if pin==pin_number:
        print("Money is withdrawing")
        break
    else:
        print("wrong pin number")

#12. Find the greatest common divisor (GCD) of two numbers using a loop.

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))

HCF=0

i=1
while i<=min(num1,num2)+1:
    if num1%i==0 and num2%i==0:
        HCF=i
    i+=1
print(HCF)

#13. Print a series where each term is double the previous term ($1, 2, 4, 8, \dots$) up to $100$.
i=1

while i<=100:
    print(i, end=" ")
    i=i*2

#14. implement a countdown timer that prints numbers from $5$ down to $1$ with a delay.
import time

num=5

while num>=1:
    print(num)
    time.sleep(1)
    num-=1

#15. Keep shifting elements of a list to the left using a loop.
numbers = [1, 2, 3, 4, 5]

count = 0

while count < len(numbers):
    first = numbers[0]

    j = 0
    while j < len(numbers) - 1:
        numbers[j] = numbers[j + 1]
        j += 1

    numbers[-1] = first

    print(numbers)

    count += 1

