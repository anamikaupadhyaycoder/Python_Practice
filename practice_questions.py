#Topic 2 (strings and conditional statements)
#string Manipulation(Q81-100)
#1. Create a grading system: $90+$ is A, $80-89$ is B, $70-79$ is C, under $70$ is F.
'''marks = int(input("enter marks: "))
if marks > 90:
    print("Grade A")
elif 79 < marks < 90:
    print("Grade B")
elif 69 < marks < 80:
    print("Grade C")
else:
    print("fail")

#2. Determine if a number is positive, even, and greater than $50$.
num = int(input("enter a number:"))
if num > 0 and num%2 == 0 and num > 50:
    print("num is everything")
else:
    print("num is nothing")

#3. Take three numbers and find the largest of them using nested if.
a, b, c = input("three numbers are entered:").split()
a1 = int(a)
b1 = int(b)
c1 = int(c)
if a1 > b1:
    if a1 > c1:
       print("a1 is largest")
    else:
        print("c1 is largest")
if b1 > c1:
    print("b1 is largest")
else:
    print("c1 is largest")

#4. Write a mini-login system checking if username == "admin" AND password == "secret".
username = input("enter username:")
password = input("enter password:")
if username == "admin":
    if password == "secret":
        print("Login Successful! Welcome, Admin.")
    else:
        print("Access Denied: Incorrect Password.")
else:
    print("Access Denied: Incorrect Username.")

#5. Check if a coordinate $(x, y)$ lies in Quadrant 1 ($x > 0, y > 0$).
x = int(input("enter value of x:"))
y = int(input("enter value of y:"))
if x > 0 :
    if y > 0:
        print("x and y both lies in quadrant.")
    else:
        print("y doesn't lie in the quadrant.")
else:
    print("x doen't lie in the quadrant.")

#6. Classify a triangle as Equilateral, Isosceles, or Scalene based on three side inputs
a = int(input("enter first side of triangle:"))
b = int(input("enter second side of triangle:"))
c = int(input("enter third side of triangle:"))
if a == b == c:
    print("triangle is equivalent")
elif a == b or b == c or a == c:
    print("triangle is isosceles")
else:
    print("triangle is scalane")

#7.A shop offers a 10% discount if purchase exceeds $100 claculate final bill.
doll = 100
inr = doll * 85 
discount = inr*10/100
final_bill = inr - discount
print(final_bill)

#8.check if a string is a palindrome(reads same forward and backward).
str1 = input("enter a string:")
if str1 == str1[::-1]:
    print("yes, it is a palindrome!")
else:
    print("No, it is not a palindrome!")

#9.Categorize a person's age:kid(<13),Teen(13-19),Adult(20-59),Senior(60+).
age = int(input("Enter age:"))
if age < 13:
    print("it is a kid.")
if 12<age<20:
    print("it is a teen.")
elif 19<age<60:
    print("it is a adult.")
else:
    print("it is a senior.")

#10.Check if a month number(1-12) falls in summer, winter, spring, or autumn.
mon_num = int(input("Enter month number:"))
if mon_num in [3,4]:
    print("it is a spring")
if mon_num in [5,6,7,8]:
    print("it is a Summers")
elif mon_num in [9,10,11]:
    print("it is a Autumn")
else:
    print("it is a Winters")

#11.Build a basic text calculator taking two numbers and an operator(+,-,*,/).
num1 = float(input("Enter 1st number:"))
oper = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter 2nd number:"))

if oper == "+":
    print(num1+num2)
if oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
else:
    print(num1/num2)

#12.Tax calculation:0% if income<$15k, 12% if $15k - $50k, 22% if > $50k.
income = float(input("Enter your annual incomr ($): "))

if income <  15000:
    rate = 0.00
elif 15000 <= income <= 50000:
    rate = 0.12
else:
    rate = 0.22

tax = income*rate
print(f"Applied Tax Rate: {int(rate*100)}%")
print(f"Total Tax Owed: ${tax:,.2f}")

#13. Verify if a string starts with "A" and ends with "Z".
string = input("Enter a string: ")
if string.startswith("A") and string.endswith("Z"):
    print("string starts with A and ends with Z")
else:
    print("string is not start with A and not end with Z")

#14. Check if a speed limit of $80$ is exceeded; calculate fine of 10% percent.
limit = int(input("Enter sppeed of the vehicle: "))
if limit > 80:
    fine = 0.10
else:
    fine = 0.00

total = limit*fine
print(f"total fine owed: int{fine*100}%")
print(f"total fine charged: {total}")

#15. Check if a speed limit of $80$ is exceeded; calculate fine of $10 per unit exceeded.
sp = int(input("Enter speed of the vehicle: "))
if sp <= 80:
    fine = 0
else:
    fine = 10

total_fine = fine*(sp - 80)
print(f"fine charged per unit exceeding: {fine}")
print(f"total fine charged: {total_fine}")

#16. Check if a number is divisible by $3$ and $7$ simultaneously.
num = int(input("Enter a number: "))
if num%3 == 0 and num%7 == 0:
    print("Num is divisible by both 3 and 7")
else:
    print("Num is not divisible by both ")

#17. Determine if a year is a century year (divisible by 100).
year = int(input("Enter year:"))
if year%100==0:
    print("year is a centuray year")
else:
    print("it's not a centuray year")

#18. Determine if a user input is a valid positive integer.
num = int(input("Enter a number: "))
if num > 0 :
    print("it's a valid positive integer.")
else:
    print("it's not a valid integer")

#19. Validate a user's password: must be at least 8 characters long.
password = input("Enter user's password: ")
length = len(password)
if length>=8:
    print("Valid password.")
else:
    print("NOt valid")

#20. Determine if a point lies inside, outside, or on a circle of radius $R$ centered at $(0,0)$.
R = float(input("Enter the radius of the circle (R):"))
x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

square_x_y = (x**2)+(y**2)
square_R = R**2

if square_x_y < square_R:
    print("point lies inside the circle.")
elif square_x_y == square_R:
    print("point lies on the circle.")
else:
    print("point lies outside the circle.")'''

#21.Simulate an XOR gate using standard logic operators.
A = True
B = False

# Step 2: Simulate XOR logic using 'and', 'or', and 'not'
if (A and not B) or (not A and B):
    xor_result = True
else:
    xor_result = False

# Step 3: Print the evaluation
print(f"Input A: {A}")
print(f"Input B: {B}")
print(f"XOR Gate Output: {xor_result}")

























