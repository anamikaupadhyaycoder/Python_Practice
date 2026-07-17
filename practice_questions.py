# Basic Arithmetic & Operations(Q31-50)
#1. Add,subtract,multiply,and divide two numbrs enterd by the user.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
sum = num1+num2
subtract = num1-num2
multiply = num1*num2
divide = num1/num2
print(sum)
print(subtract)
print(multiply)
print(divide)

#2. Find the remainder when $27$ is divided by $4$ using the modulo operator %.
remainder = 27%4
print(remainder)

#3. Calculate $3$ raised to the power of $4$ ($3^4$) using the exponentiation operator **.
power = 3**4
print(power)

#4. Find the floor division quotient when $19$ is divided by $5$ using //.
floor_division = 19//4
print(floor_division)

#5. Write a program to calculate the area of a rectangle ($length \times width$).
length = int(input("enter length:"))
breadth = int(input("enter breadth:"))
area = length*breadth
print(f"area of rectangle: {area}")

#6. Calculate the area of a circle using radius input ($Area = \pi r^2$, use $3.14159$).
radius = int(input("enter radius of circle:"))
pie = 3.14
area_of_circle = (radius**2)*pie
print(f"area of circle: {area_of_circle}")

#7. Convert a temperature from Fahrenheit to Celsius ($C = \frac{F - 32}{1.8}$).
Fahrenheit = int(input("enter value of fahrenheit:"))
conv = (Fahrenheit - 32)/1.8
print(conv)

#8. Convert a given number of minutes into hours and remaining minutes.
min = int(input("enter a minute:"))
hou = min/60 
print(hou)

#9. Calculate Simple Interest: $SI = \frac{P \times R \times T}{100}$
principle = int(input("enter the principle value:"))
rate = int(input("enter the rate:"))
time = int(input("enter the time:"))
simple_Interest = principle*rate*time/100
print(simple_Interest)

#10. Ask the user for three numbers and print their mathematical average.
num1 = int(input('enter number one:'))
num2 = int(input('enter number two:'))
num3 = int(input('enter number three:'))
average = num1+num2+num3/3
 

























