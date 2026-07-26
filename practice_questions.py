#Dictionary & Set (50 Questions)
#Dictionary Basics (Q151–165)
#1. Create a dictionary representing a Student with keys name, age, and grade.
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
print(student

#2. Access and print the name of the student from the dictionary.
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
print(student["name"])

#3. Use the .get() method to safely retrieve the grade key without throwing an error.
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
print(student.get("grade"))

#4. Add a new key-value pair school: "MNC High" to your dictionary.
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
student["school"] = "MNC High"
print(student)

#5. Update the value of the age key in the student dictionary.
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
student["age"] = 87
print(student)

#6. Remove a key-value pair from the dictionary using del.
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
del student["age"]
print(student)

#7. Remove a key-value pair and return its value using .pop().
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
removed_age = student.pop("age")
print("updated Dictionary: ", student)
print("Removed Value: ",removed_age )

#8. Print all the keys of a dictionary using .keys().
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
print(student.keys())

#9. Print all the values of a dictionary using .values().
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
print(student.values())

#10. Print all key-value pairs as a list of tuples using .items().
student = {
    "name" :"Anamika",
    "age" :12,
    "grade" :"A"
}
pairs_list = list(student.items())
print(pairs_list)

#11. Check if the key "salary" exists inside an employee dictionary.
employee_dict = {
    "name": "Anamika",
    "salary": "30000", 
    "working_days": "28"
}
if "salary" in employee_dict:
    print("salary exits")
else:
    print("salary not exits")

#12. Find the total number of key-value pairs in a dictionary.
employee_dict = {
    "name": "Anamika",
    "salary": "30000", 
    "working_days": "28"
}
print(len(employee_dict))

#13. Clear all items from a dictionary to make it empty.
employee_dict = {
    "name": "Anamika",
    "salary": "30000", 
    "working_days": "28"
}
print(employee_dict.clear())
print(employee_dict)

#14. Create a dictionary with integer keys and print their values.
int_dict = {
    1 : "anamika",
    2 : "shreya", 
    3 : "aayushi"
}
print(int_dict)

#15. Merge two separate dictionaries dict1 and dict2 together.
int_dict = {
    1 : "anamika",
    2 : "shreya", 
    3 : "aayushi"
}

employee_dict = {
    "name": "Anamika",
    "salary": "30000", 
    "working_days": "28"
}
sum = int_dict | employee_dict
print(sum)