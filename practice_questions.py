#1 Write a program to print "Let's learn Python!" to the console.
print("Lets's learn Pyhton!")
#2 Create an integer variable age = 20 and print it.
x = 20 
print(x)
#3 Create a float variable price = 99.99 and print it.
price = 99.99
print(price)
#4 Create a string variable language = "Python" and print it.
language = "Python"
print(language)
#5 Create a boolean variable is_fun = True and print its value.
is_fun = True
print(is_fun)
#6 Swap the values of two variables x = 5 and y = 10 using a temporary third variable.
x = 5
y = 10

print(f"Before swap: x = {x} , y = {y}")
temp = x
x = y
y = temp
print(f"After swap: x = {x} ,y = {y}")
#7 Perform a Pythonic swap on x and y in a single line without a third variable.
x = 5 
y = 10
 
print(f"before swap: x = {x}, y = {y}")

x,y = y,x
print(f"after swap: x = {x}, y = {y}")
#8 Use type() to print the data type of an integer, a float, a string, and a boolean.
x = "string"
y = 10 
z = True
w = 99.9
print(type(x))
print(type(y))
print(type(z))
print(type(w))
#9 Try to assign a value to a variable starting with a number (e.g., 1variable = 10) and observe the syntax error.
1variable = 10
print(1variable)
#10 Store three different values in three variables a, b, and c in a single line.
a, b, c = "Mango", "banana", "litchi"
print(a,b)
#11 Assign the same value 100 to variables x, y, and z simultaneously.
x = y = z = 100
print(z)
#12 Store your name in a variable and write a Python comment explaining what the variable stores.
name = "aayushi" # it is a name variable that stores the value as a name. I can store multiple names
#13 Print "Python" and "Rocks" in the same line separated by a hyphen (Python-Rocks) using a print parameter.
print("Pyhton", end="- ")
print("Rocks")
#14 Print three words on the same line with a space between them using a single print() statement.
print("Anamika", "Shreya", "Aayusi")
# Define a constant-like variable for gravity ($9.8$) using uppercase naming conventions.
GRAVITY = 10.0
print(GRAVITY)






