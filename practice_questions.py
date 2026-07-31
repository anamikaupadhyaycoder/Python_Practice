#Topic 5: Loops in Python (50 Questions)
#For Loops (Q201–215)
#1. Print numbers from $1$ to $10$ using a for loop.

'''for i in range(1,11,1):
    print(i)


#2. Print all even numbers between $1$ and $30$ using a for loop with a step.

for i in range(2,31,2):
    print(i)

#3. Print all odd numbers between $1$ and $30$ using a for loop.
for i in range(1, 31, 2):
    print(i)

#4. Sum all numbers from $1$ to $50$ using a loop and print the total.
total = 0

for i in range(1, 51):
    total+=i
print(total)

#5. Print the multiplication table of a user-inputted number.
num = int(input("enter a number:"))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#6. Print each character of the string "DEVELOPER" on a separate line.
word = "DEVELOPER"

for ch in word:
    print(ch)

#7.iterate over a list of names and print a greeting for each.
names = ["vanshika","misha","ishqi","mihir"]

for name in names:
    print(f"Hello: , {name}! Hope you have a great day.")

#8. Print numbers from $10$ down to $1$ using a for loop and range().

for i in range(10,0,-1):
    print(i)

#9. Print the squares of all numbers from $1$ to $10$.

for i in range(1,11,1):
    product  = i**2
    print(product)

#10. Count the total number of vowels in a string using a loop.
string = input("Enter a word: ").lower()

count = 0

for ch in string:
    if ch in "aeiou":
        count+=1
print("Total numbers:", count)

#11. Calculate the product of all numbers in a list.
nums = [1, 5, 3, 6]

product = 1

for num in nums:
    product *=num
    print(f"product of all numbers: {product}")

#12. print a horizontal row of 10 asterisks (*) using a loop

for i in range(10):
    print("*", end= " ")

#13. Print elements of a list along with their index using enumerate().

nums = [3,2,5,8,7,1]

for index, item in enumerate(nums):
    print(index, item)

#14. Print all numbers between $100$ and $200$ that are divisible by $7$.

for i in range(100, 200):
    if i%7 == 0:
        print(i)'''

#15. Print the elements of a tuple in reverse order using a loop.
    
nums = (3, 5 ,8, 2, 9)


for i in range(len(nums) - 1, -1, -1):
    print(nums[i])

































