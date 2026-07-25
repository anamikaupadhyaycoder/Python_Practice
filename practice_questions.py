#List Slicing & Built-ins (Q116–130)
#1.Print the first 3 elements of a list using slicing.
list1 = [4, 2, 6, 8, 9, 0]
print(list1[0:3])

#2. Print every second element of a list using steps in slicing.
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
print(list1[::2])

#3. Reverse a list using slicing ([::-1]).
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
print(list1[::-1])

#4. Find the maximum value in a list of integers using max().
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
max = max(list1)
print(max)

#5. Find the minimum value in a list of integers using min().
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
min = min(list1)
print(min)

#6. Calculate the sum of all numbers in a numeric list using sum().
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
sum = sum(list1)
print(sum)

#7. Sort a list of numbers in ascending order using .sort().
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
list1.sort()
print(list1)

#8. Sort a list of numbers in descending order using sorted()
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
descending_order = sorted(list1, reverse=True)

print("Original list:", list1)          # Output: 
print("New sorted list:", descending_order) 

#9. Duplicate a list's content three times using the multiplication operator *.
list1 = [4, 2, 6, 8, 9, 0, 7, 8]
d = list1*3
print(d)

#10. Split a list of 6 items into two equal halves.
list1 = [4, 2, 6, 8, 9, 0]
print(list1[0:3])
print(list1[3:6])

#11. Find the second largest number in a list of unique numbers.
list1 = [4, 2, 6, 9, 0, 7, 8]
list1.sort()
print(list1)
print(list1[-2])

#12. Replace all negative numbers in a list with $0$.
list1 = [4, -2, 6, -9, 0, 7, -8]
list1 = [num if num >= 0 else 0 for num in list1]

print(f"final list : {list1}")

#13. Create a nested list (a list inside a list) and access an item inside the inner list.
list1 = [2, 4, 5, 16, 8, 20, [3, 2, 5, 9], 9]
item = list1[6][2]
print(item)

#14. Check if a list is empty.
l = []

if not l:
    print("the list is empty")
else:
    print("the list is not empty")

#15. Convert a list of characters ['P', 'y', 't', 'h', 'o', 'n'] into a single string.
chara = ['Python']
single_string = "".join(chara)
print(single_string)
























