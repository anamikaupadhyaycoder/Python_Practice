# Basic Arithmetic & Operations(Q31-50)
#11. Round the decimal number 7.8945 to exactly two decimal places.
x = 7.8945
round_x = round(x, 2)
print(round_x)

#12. Calculate the absolute value of $-15$ using a built-in function.
num = -15
absolute_value = abs(num)
print(f"original: num = {num}")
print(f"Absolute value: absolut_value = {absolute_value}")

#13. Find the square root of $144$ using the math module or exponentiation.
x = 144
squ_root = x**0.5
print("square root: ",squ_root)

#14. Compute the final price of an item after applying a $15\%$ discount.
item = 1000 
dis = 1000 * 15/100
print(dis)

#15. Ask for a 2-digit number and print the sum of its individual digits.
two_dig = input("Ask for a two digit number:")
fir_dig = int(two_dig[0])
sec_dig = int(two_dig[1])
sum = fir_dig + sec_dig
print(sum)

#16. Calculate Body Mass Index (BMI) using weight (kg) and height (meters).
wei = 22
hei = 5.5
bmi = wei/hei**2
print("Body mass index: ", bmi)

#17. Convert kilometers to miles ($1 \text{ km} \approx 0.621371 \text{ miles}$).
km_1 = 0.621371
n = 4# conversion of 4km into miles
km_4 = n * km_1
print(km_4)

#18. Calculate the compound interest given principal, rate, and time.
p = 100000
r = 10/100
n = 2#semi annual: interest is added every 6 months
t = 1
A = p*(1+(r/n))**(n*t)
ci = A - p
print("compound : ", ci)

#19. Find the perimeter of a square given its side length.
len = 4
side = 4*len
print("perimeter of square:", side)

#20. Write a program that calculates the volume of a sphere ($V = \frac{4}{3} \pi r^3$).
r = 2
pie = 3.14
volume = 4/3*pie*r**3
print("volume of sphere:", volume)





























