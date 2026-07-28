#Advanced Dictionary Logic (Q166–180)
#1. Create a nested dictionary representing a classroom of 3 students.
nes_dic = {
    "student 1" : {
        "name" : "anamika",
        "age" : 12, 
        "grade" : "A"
    },
    "student 2" : {
        "name" : "aayushi",
        "age" : 13, 
        "grade" : "C"
    },
    "student 3" : {
        "name" : "shreya", 
        "age" : 14,
        "grade" : "B"
    }
}
print(nes_dic)

#2. Access the grade of the second student inside the nested dictionary.
classroom = {
    "student 1" : {
        "name" : "anamika",
        "age" : 12, 
        "grade" : "A"
    },
    "student 2" : {
        "name" : "aayushi",
        "age" : 13, 
        "grade" : "C"
    },
    "student 3" : {
        "name" : "shreya", 
        "age" : 14,
        "grade" : "B"
    }
}

print(classroom['student 2']['name'])

#3. Use the .get() method to safely retrieve the grade key without throwing an error.
classroom = {
    "student 1" : {
        "name" : "anamika",
        "age" : 12, 
        "grade" : "A"
    },
    "student 2" : {
        "name" : "aayushi",
        "age" : 13, 
        "grade" : "C"
    },
    "student 3" : {
        "name" : "shreya", 
        "age" : 14,
        "grade" : "B"
    }
}
grade = classroom.get('student 2', {}).get('grade', 'Grade not found')
print(grade)

#4. Map two lists (one of names, one of scores) into a single dictionary.
names = ['anamika', 'aayushi', 'shreya']
scores = [94, 74, 86]

classroom_scores = dict(zip(names, scores))
print(classroom_scores)

#5. Create a dictionary where the keys are numbers 1 to 5, and values are their squares.
num = {
    1 : 1**2,
    2 : 2**2,
    3 : 3**2,
    4 : 4**2,
    5 : 5**2
}
print(num)

#6. Remove all keys with None values from a dictionary.
num = {
    1 : 1**2,
    2 : 2**2,
    3 : 3**2,
    4 : 4**2,
    5 : 5**2
}

s = num.clear()
print(s)
print(num)

"""
7. Extract a subset of a dictionary (keys a and b only) into a new dictionary.
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_extract = {'a', 'b'}
subset_dict = {key: original_dict[key] for key in keys_to_extract if key in original_dict}
print(subset_dict)
"""

#8. Find the key with the highest value in a dictionary.
num_dict = {
    'num1' : 24,
    'num2' : 45,
    'num3' : 73,
    'num4' : 12
}
highest_value = max(num_dict, key=num_dict.get)
print(highest_value)

#9. Check if all values in a dictionary are identical.
num_dict = {
    'num1' : 10,
    'num2' : 10,
    'num3' : 10,
    'num4' : 10
}

all_same_1 = len(set(num_dict.values())) == 1
print(f"Are all values in num_dict identical? {all_same_1}")

#10. Reverse a dictionary (swap keys and values, assuming values are unique).
num_dict = {
    'num1' : 22,
    'num2' : 11,
    'num3' : 70,
    'num4' : 19
}
reversed_dict = {value: key for key, value in num_dict.items()}
print(reversed_dict)

#11. Create a dictionary of words and their lengths from a list of words.
lis = ["apple", "banana", "mango", "kiwi"]
word_len = {word: len(word) for word in lis}
print(word_len)

#12. Use a dictionary to map weekdays (1 -> "Monday", 2 -> "Tuesday", etc.).
week_dict = {
    1 : "monday",
    2 : "Tuesday", 
    3 : "wednesday", 
    4 : "thursday", 
    5 : "friday",
    6: "Saturday",
    7: "Sunday"
}

print("weekdays 3:", week_dict[3])
print("weekdays 7:", week_dict.get(7, "Invalid day"))
print(week_dict) 

#13. Sort a dictionary by its keys in alphabetical order.
dict_to_sort = {
    'banana': 3,
    'apple': 4,
    'pear': 1,
    'orange': 2
}

sorted_dict = dict(sorted(dict_to_sort.items()))
print(sorted_dict)

#14. Sort a dictionary by its values in ascending order.
dict_to_sort = {
    'banana': 3,
    'apple': 4,
    'pear': 1,
    'orange': 2
}

sorted_dict_by_values = dict(sorted(dict_to_sort.items(), key=lambda item: item[1]))
print(sorted_dict_by_values)


# 15. Combine two dictionaries by adding values for common keys.
from typing import Counter
dict1 = {"a" : 100, "b" : 200, "c" : 300}
dict2 = {"a" : 500, "b" : 400, "c" : 350}
result = dict(Counter(dict1)+ Counter(dict2))
print(result)








































































































































