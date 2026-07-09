# smart temperature converter 
''' take input in celsius and print its equivalent in fahrenheit and kelvin.
(use explicit type conversion and arithmetic operators.)
 fahreneheit = (c x 9/5) + 32
 kelvin = c + 273.15'''

cel = int(input("enter the value of celsius :"))
fah = (cel * 9/5) + 32
kel = cel + 273.15

print("equivalent in fahrenheit :", fah)
print("equivalent in kelvin :", kel)

# write a program that takes total bill amount and number of friends as input. 
# calculate how much each person will pay
# Also print the data type of each variable used.

fri = float(input("enter no of friends: "))
to_amo = float(input("enter total amount: "))

each = to_amo/fri
print("each person will pay: ", each)
print(type(fri))
print(type(to_amo))
print(type(each))






