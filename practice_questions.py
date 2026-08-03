#Loops in Python (50 Questions)
#While Loops (Q216–230)
#1. Print numbers from $1$ to $10$ using a while loop.

'''i = 0

while i<=10:
    i+=1
    print(i)

#2. Print numbers from $10$ down to $1$ using a while loop.

i = 10
while i >=1:
    print(i)
    i-=1

#3. Keep asking the user for input until they type "exit".

while True:
    user_input = input("Enter something (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Program terminated.")
        break

    print("You entered:", user_input)

#4. Keep adding user inputs to a sum until the user enters $0$.

total = 0

while True:
    user_input = int(input("enter input(type '0' to exit ): "))

    if user_input == 0:
        break
    

    total+=user_input

print("sum=", total)

#5. (Number Guessing): Let a user guess a secret number until they get it correct.
secret_number = 25

while True:
    guess = int(input("Guess the secret number: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again!")

#6. Find the sum of digits of a given integer using a while loop.

number = int(input("Enter an integer: "))

sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

print("Sum of digits =", sum_of_digits)

#7. Reverse a given integer using arithmetic operations in a while loop.

number = int(input("enter an integer: "))

reverse = 0 

while number > 0:
    digit = number % 10  
    reverse = reverse*10+digit
    number = number//10

print("Reversed number =", reverse)

#8. Print the first $N$ terms of the Fibonacci sequence using a loop.
n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Sequence:")

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

#9. Count the number of digits in an integer by repeatedly dividing by 10 in a loop.
num = int(input("Enter an integer: "))

count = 0

while num != 0:
    num = num // 10
    count = count + 1

print("Number of digits =", count)'''

#Print numbers from 50 to 10 in reverse with a step of 5.

for i in range(50,5,-5):
    print(i)










