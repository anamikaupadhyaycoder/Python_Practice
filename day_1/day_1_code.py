name = {
    "key" : "Value",
    "names" : {
        "name1" : "Aayushi",
        "name2" : "Anamika",
        "name3" : "Shreya",
        "name4" : "isha",
    },
    "age" : 17,
    "hobbies" : "singing",
    "family" : "nuclear",
    "course" : "bca"
}

print(name["age"])#error
print(name.get("age1"))#None

name.update({"city" : "Delhi"})
print(name)




