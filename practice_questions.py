# Topic 3: Lists and Tuples(50 questions)
# List Operations (Q101–115)
#1. Create a list of 5 movies and print the full list.
movies = ["3 idiots", "pk", "narshima", "mardani", "mardani 2"]
print(movies)
print(type(movies))

#2. Access and print the 3rd element of a list.
num = [1, 2, 3, 4, 5 ]
print(num[3])

#3. Access the last element of a list using a negative index.
num = [1, 2, 3, 4, 5 ]
print(num[-1])

#4. Change the first element of a list of numbers to $99$.
lis = [1, 3, 4, 2, 6, 4 ,7]
lis[0] = 99
print(lis)

#5. Use .append() to add a new city to a list of cities.
cities = ["delhi", "mumbai", "hyderabad", "bangalore"]
cities.append("punjab")
print(cities)

#6. Insert an element at index $1$ of an existing list using .insert().
lsit = [3, 5, 2, 6, 7, 8, 0]
lsit.insert(1, 3)
print(lsit)

#7. Remove an element from a list by its exact name using .remove().
lis = [4, 7, 8, 3, 4, 1, 2]
lis.remove(7)
print(lis)

#8. Remove and return the last element of a list using .pop().
lis = [4, 6, 7, 3, 1, 9]
last_lis = lis.pop()
print(lis)
print(last_lis)

#9. Check if the value "Banana" exists in a list of fruits.
fruits = ["mango", "banana", "apple", "litchi"]
if fruits.count("banana") > 0:
    print("Banana exits")
else:
    print("Banana doesn't exist")

#10. Find the index position of a specific element in a list.
lis = [2, 4, 5, 1, 6, 7, 9]
print(lis.index(6))

#11. Count how many times the number $5$ appears in a list.
lis = [4, 2, 5, 8, 5, 0, 5, 1, 5]
print(lis.count(5))

#12. Find the total length (number of items) of a list.
lsi = ["anamika", "aayushi", "isha", "shreya"]
print(len(lsi))

#13. Concatenate (combine) two lists together.
lis1 = [1, 2, 3]
lis2 = [4, 5, 6]
lis = lis1+lis2
print(lis)

#14. Clear all elements from a list so it becomes completely empty.
list1 = [5, 6, 3, 7, 2, 7 ]
cl = list1.clear()
print(list1)

#15. Create a list of 5 elements and slice the middle 3 elements out.
list1 = [5, 6, 3, 7, 2, 7 ]
print(list1[0:3])

























































