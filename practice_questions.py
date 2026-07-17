# User Input & Conversions(Q16-30)
#1. Take a user's name as input and print a welcome message.
name = input("enter name:")
print("Welcome")

#2. Take a number as input from the user, convert it to an integer, and print its square.
num = int(input('enter a number:'))
print(num**2)

#3. Ask the user for a float number, convert it to an integer, and print the result.
num_1 = float(input("enter a number:"))
num_2 = int(num_1)
print(type(num_2))

#4. Take an integer input and convert it to a float.
i = int(input("anamika"))
i_i = float(i)
print(type(i_i))

#5. Convert the boolean True to an integer and print the resulting value.
con = True
con1 = int(con)
print(type(con1))

#6. Convert the integer 0 to a boolean and print the resulting value.
num = 0 
num1 = bool(num)
print(type(num1))
print(num1)

#7. Take two string inputs from the user, concatenate them with a space, and print the result.
st = input("Enter a word:")
st_1 = input("Enter a word:")
st2 = st + " " + st_1
print(st2)

#8. Read two integers from the user, add them together, and print the sum.
num1 = int(input('enter a number:'))
num2 = int(input('enter a number:'))
sum = num1 + num2
print(sum)

#9. Ask the user for their birth year and calculate their age dynamically.
person = int(input('enter your birth year:'))
age = 2026 - person 
print(age)

#10. Ask a user for a float value representing a price and print "The price is: [price]".
pri = float(input('enter price of the commodity:'))
print(f"The price is: {pri}")

#11. Take a single-character input from a user and check its type.
inp = input("enter a single-character:")
print(type(inp))

#12. Convert the string "250" to an integer and add 50 to it.
inp1 = "250"
integer_inp1 = int(inp1)
print(type(integer_inp1))
sum = integer_inp1 + 50
print(sum)

#13. Attempt to convert "hello" to an integer inside a try-except block to see how Python handles conversion errors.
num = int("hello")
print(type(num))

#14. Take a user's weight in kilograms (as float) and print it.
weight = float(input("enter weight in kilograms:"))
print(weight)
print(type(weight))

#15. Read a boolean input from a user by evaluating input() == "True".
user_input = input("enter True or False:")
is_active = user_input == True
print(f'th boolena value is: {is_active}')
print(type(is_active))






