#7. Iterate over a list of names and print a greeting for each.
fruits=["apple", "mango", "litchi", "kiwi"]

for i in range(1,4):
    print(fruits)

#8. Print numbers from $10$ down to $1$ using a for loop and range().
for i in range(10, 0, -1):
    print(i)

#9. Print the squares of all numbers from $1$ to $10$.
for i in range(1,11):
    print(f"{i} =", i**2)

#10. Count the total number of vowels in a string using a loop.
string = "developer".lower()

count=0
vowels="aeious"
for ch in string:
    if ch in vowels:
        count+=1
print(count)

#11. Calculate the product of all numbers in a list.
lis = [1, 4, 3, 6]

product=1
for num in lis:
    product*=num
print(product)

#12. Print a horizontal row of 10 asterisks (*) using a loop.

for i in range(1,11):
    print("*", end=" ")

#13. Print elements of a list along with their index using enumerate().
lis = ["a", "b", "c", "d"]

for index, item in enumerate(lis):
    print(index, item)

#14. Print all numbers between $100$ and $200$ that are divisible by $7$.
for i in range(100,201):
    if i%7==0:
        print(i)

#15. Print the elements of a tuple in reverse order using a loop.

tup=(3, 5, 6, 8)

for item in reversed(tup):
    print(item)



