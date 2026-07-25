#Tuples & Transformations (Q131–50)
#1. Create a tuple containing 5 items and print it.
tuple = (1, 3, 2, 5, 6, 7)
print(tuple)

#2. Try to change the first element of a tuple and observe the TypeError (immutability).
Tuples = (49, 66, 39,93, 94, 20, 0)
Tuples[0] = 43

#3. Access the 2nd and 4th element of a tuple.
Tuple = (3, 5, 9, 7, 8, 2)
print(Tuple[2])
print(Tuple[4])

#4. Convert a tuple to a list, change an element, and convert it back to a tuple.
Tuple = (3, 5, 29, 9, 0)
List = list(Tuple)
List[0] = 2
Tuple1 = tuple(List)
print(Tuple1)

#5. Find the length of a tuple.
Tuple = (3, 5, 29, 9, 0)
print(len(Tuple))

#6. Check if an item exists inside a tuple.
item = ("mango", "banana", "apple", "litchi")
if "mango" in item:
    print("This item exits in a tuple")
else:
    print("This item doesn't exits in a tuple")

#7. Unpack a tuple of 3 elements into variables x, y, and z.
Tuple = (2, 4, 5)
x, y, z = Tuple
print("x:", x)
print("y:", y)
print("z:", z)

#8. Concatenate two tuples together.
my_tuple1 = (2, 4, 5)
my_tuple2 = (3, 5, 29, 9, 0)
sum = my_tuple1+my_tuple2
print(sum)

#9. Find the index of an item inside a tuple.
my_tuple = (2, 4, 5)
print(my_tuple.index(4))

#10. Create a single-element tuple (make sure it includes the trailing comma)
my_tuple = ('Python',)
print(my_tuple)
print(type(my_tuple))

#11. Convert a list into a tuple using tuple().
my_list = [2, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

#12. Convert a tuple of digits into a single integer.
my_tuple = (2, 4, 5)
string_tuple = "".join(str(d) for d in my_tuple)
single_int = int(string_tuple)
print(single_int)

#13. Create a tuple of tuples and access an element from the nested structure.Create a tuple of tuples and access an element from the nested structure.
my_tuple = (2, (4, 1, 5), (6, 8, 9, 0),2)
print(my_tuple[2][2])

#14. Find the sum of all elements in a numeric tuple.
my_tuple = (2, 5, 5)
s = sum(my_tuple)
print(s)

#15. Check if two tuples contain the exact same elements.
my_tuple1 = (2, 7, 5)
my_tuple2 = (5, 2, 1)
if set(my_tuple1) == set(my_tuple2):
    print("both tuples contain the same element")
else:
    print("both tuples doesn't contain the same element")

#16. Slice a tuple to extract all elements except the first and last.
my_tuple = (2, 4, 1, 5, 6, 8, 9, 0, 2)
print(my_tuple[1:8])

#17. Repeat a tuple 4 times.
my_tuple = (2, 7, 5)
Repeat = my_tuple*4
print(Repeat)

#18. Use tuple unpacking with the * operator to capture remaining elements into a list.
my_tuple = ("Admin", "Editor", "Viewer", "Guest", "Anonymous")
x, y, *others = my_tuple
print("x:", x)
print("y:", y)
print("z:", others)

#19. Swap the values of two variables using tuple unpacking.
my_tuple = (2, 7)
x, y = my_tuple
x, y = y, x
print("x:", x)
print("y:", y)

#20. Find the maximum and minimum value in a tuple of floats.
my_tuple = (2.8, 7.65, 8.9 , 3.0)
m = max(my_tuple)
n = min(my_tuple)
print(m)
print(n)

#21. find the maximum and minimum values inside a nested tuple (e.g., ((1.2, 3.4), (5.6, 0.7)))
my_tuple = ((1.2, 3.4), (5.6, 0.7))
m = max(item for sublist in my_tuple for item in sublist)

n = min(item for sublist in my_tuple for item in sublist)
print(m)
print(n)









































