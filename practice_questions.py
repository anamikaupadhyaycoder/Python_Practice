#Sets & Set Operations (Q181–200)
#1. Create a set of 5 prime numbers and print it.
set1 = {1, 5, 3, 7, 9}
print(set1)

#2. Try adding a duplicate number to a set and observe that duplicates are ignored.
set1 = {2, 6, 3, 2}
print(set1)

#3. Add a new element to a set using .add().
set1 = {2, 6, 3, 2}
set1.add(4)
print(set1)

#4. Remove an element from a set using .remove() (raises error if element not found).
set1 = {2, 6, 3, 7}
set1.remove(3)
print(set1)

#5. Safely remove an element from a set using .discard() (does not raise error).
set1 = {2, 6, 3, 7}
set1.discard(3)
print(set1)

#6. Find the union of two sets of numbers.

set1 = {2, 6, 3, 7}
set2 = {3, 5, 8, 7}
result = set1.union(set2)
print(result)

#7. Find the intersection of two sets of numbers.
set1 = {2, 6, 3, 7}
set2 = {3, 5, 8, 7}
result = set1.intersection(set2)
print(result)

#8. Find the difference between two sets (elements in A but not in B).
a = {2, 6, 3, 7}
b = {3, 5, 8, 7}
result = a-b
print(result)

#9. Find the symmetric difference between two sets.
a = {2, 6, 3, 7}
b = {3, 5, 8, 7}
result = a.symmetric_difference(b)
print(result)

#10. Check if a set is a subset of another set.
a = {2, 6}
b = {1, 2, 6, 7}
print(a.issubset(b))

#11. Check if two sets have no elements in common (disjoint).
a = {12, 4}
b = {1, 2, 6, 7}
print(a.isdisjoint(b))

#12. Convert a list of duplicate numbers into a set to find unique values.
list1 = (2, 5, 6, 8, 2, 3, 6, 5)
result = set(list1)
print(result)

#13. Find the length of a set.
b = {1, 2, 6, 7}
print(len(b))

#14. Clear all elements from a set.
b = {1, 2, 6, 7}
result = b.clear()
print(result)

#15. Remove and return an arbitrary element from a set using .pop().
b = {1, 2, 6, 7}
result = b.pop()
print(result)
print(b)

#16.Convert a set into a sorted list.
b = {8, 3, 5, 7}
result = sorted(b)
print(result)

#17. Check if an item exists inside a set.
b = {1, 2, 6, 7}
if 6 in b:
    print('element exits in set b')
else:
    print("element not exits")

#18. Update a set with elements from a list.
b = {1, 2, 6, 7}
list1 = [5, 8, 3]
b.update(list1)
print(b)

#19. Write a program to find common elements from three different sets.
a = {2, 5, 3, 7}
b = {3, 5, 8, 7}
c = {2, 3, 7, 5}
result = a.intersection(b,c)
print(result)


#20. Create a set of vowels and find how many vowels are present in a user's name.
vowels = {"a", "e", "i", "o" "u"}
name = input("enter user's name:").lower()
count = 0

for letter in name:
    if letter in vowels:
        count += 1

print("number of vowels:", count)

b = {3, 5, 2}
print(b)













































































