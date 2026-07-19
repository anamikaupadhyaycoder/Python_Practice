#Topic 2 (strings and conditional statements)
#string Manipulation(Q51-65)
#1. Merge two string variables str1 = "Hello" and str2 = "World" into one string with a space.
str1 = "Hello"
str2 = "World"
string = str1 + " " + str2
print(string)

#2. Print the first character of the string "Database".
word = "Database"
print(word[0])

#3. Print the last character of "Database" using negative indexing.
wor = "Database"
print(wor[-1])

#4. Slice the word "Code" out of "PythonCode".
wo = "Pythoncode"
print(wo[-4:])

#5. Slice and reverse the string "computer".
st = "computer"
print(st[::-1])

#6. Find the total length of the string "Artificial Intelligence"
w = "Artificial Intelligence"
print(len(w))

#7. Convert "learning is fun" to Title Case.
ti = "learning is fun"
print(ti.title())

#8. Convert "PYTHON PROGRAMMING" to lower case.
name = "PYTHON PROGRAMMING"
print(name.lower())

#9. Remove the leading and trailing spaces from "   clean me   "
na = "   clean me   "
print(na.strip())

#10. Replace all occurrences of "s" with "$" in "successful".
w = "successful"
remove = w.replace("s", "$")
print(remove)

#11. Check if the string "Automation" starts with "Auto".
word = "Automation"
ch = word.startswith("Auto")
print(ch)

#12. Check if a string ends with the extension ".py".
str1 = "anamiika.py"
print(str1.endswith(".py"))

#13. Find the index of the first occurrence of the word "great" in "Python is great".
text = "Python is great."
ind = text.find("great")
print(ind)

#14. Count how many times the character "o" appears in "school pool".
text = "school pool"
print(text.count("o"))

#15. Split the string "red,green,blue" into a list of colors.
strq = "red,green,blue"
print(strq.split(" , "))



