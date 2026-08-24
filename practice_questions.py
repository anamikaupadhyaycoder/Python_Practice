#While loops
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

#Nested Loops & Flow Control (Q231-250)
#1. Use a for loop with break to stop printing numbers when encountering $5$.
for i in range(1,6):
    if i==5:
        break
    print(i)

#2. Use continue to print numbers $1$ to $10$ except the number $7$.
for i in range(1,11):
    if i==7:
        continue
    print(i)

#3. Print a $3 times 3$ grid of asterisks (*) using nested loops.
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

#4. Print a right-angled triangle pattern of stars:text * ** ***
for i in range(3):
    for j in range(i):
        print("", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()

#5. Print an inverted right-angled triangle pattern of stars.
for i in range(3):
    for j in range(i):
        print("", end="")
    for j in range(3-i):
        print("*", end=" ")
    print()

#6. Print a centered pyramid pattern of stars.
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()

#7. Print the multiplication tables from $1$ to $5$ using nested loops.
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}=", i*j)
    print()

#8. Find all prime numbers between $2$ and $50$ using nested loops.
for num in range(2,51):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1

    if count==2:
        print(i, end=" ")

#Create a $2 text{D}$ matrix (list of lists) and print it row by row.
matrix=[
[2,3,4],
[1,5,8],
[7,2,1]
]
for row in matrix:
        print(row)

#Transpose a 2*3 matrix into a 3*2 matrix using loops.
matrix_a=[
    [2,2,4],
    [1,5,7]
]

transpose=[
    [0,0],
    [0,0],
    [0,0]
]

for i in range(2):
    for j in range(3):
        transpose[j][i]=matrix_a[i][j]

for row in transpose:
    print(row)