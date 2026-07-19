#Topic 2 (strings and conditional statements)
#string Manipulation(Q66-80)
#1. Take an integer input and print "Even" or "Odd".
num = int(input("Enter a number:"))
if num%2 == 0:
    print("Even")
else:
    print("Odd")

#2. Take a number and print whether it is "Positive", "Negative", or "Zero".
num = int(input("enter a number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("Negative")
else:
    print("zero")

#3. Compare two numbers and print the larger one
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if num1 > num2:
    print("num1 is the larger one")
else:
    print("num2 is the larger one")

#4. Check if a user's age is $18$ or above to print "Eligible to Vote", otherwise "Not Eligible".
age = int(input("Enter age:"))
if age >= 18:
    print("enligible to vote")
else:
    print("not eligible")

#5. Write an if statement that checks if a user's password is exactly "admin123".
password = "admin1234"
if password == "admin123":
    print("True")
else:
    print("false")

#6. Check if a year is a leap year (divisible by 4, but not by 100 unless divisible by 400).
year = int(input('enter year:'))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0 ):
    print("year is a leap year")
else:
    print("it's not a leap year")

#7. Check if a given character is a vowel or a consonant.
char = input("Enter a character:")
lower = char.lower()
if lower in "aeiou":
    print("it's a vowel")
else:
    print("it's a consonant")

#8. Determine if a given number is a multiple of $5$.
num = int(input("enter a number:"))
if num%5 == 0:
    print("multiple of 5")
else:
    print("not multiple of 5")


#9. Create a program that takes an exam score and prints "Pass" if $\ge 50$, otherwise "Fail".
marks = int(input('enter marks of students:'))
if marks >= 50:
    print("pass")
else:
    print("fail")

#10. Take a string input and check if it contains only digits.
di = input("enter something:")
if di.isdigit():
    print("di only contains digits")
else:
    print("di not contains digits")

#11. Take two numbers and print "Equal" if they are equal, otherwise "Not Equal".
first_num = int(input("Enter first num:"))
sec_num = int(input("Enter second num:"))
if first_num == sec_num:
    print("Equal")
else:
    print("Not Equal")

#12. Check if a given temperature is below $0^\circ\text{C}$ and print "Freezing!".
temp = int(input("enter temperature:"))
if temp<0:
    print("Freezing")
else:
    print("Not Freezing")

#13. Check if a user's typed string is empty.
string = input("enter a word:")
if string == "":
    print("String is empty")
else:
    print("string is not empty")

#14. Determine if a triangle with angles $a$, $b$, and $c$ is valid ($sum == 180$).
a, b, c = input("enter three values seprated by lines: ").split()
a1 = int(a)
b1 = int(b)
c1 = int(c)

sum1 = a1 + b1 + c1
if sum1 == 180:
    print("a, b and c is valid")
else:
    print("a, b and c is not valid")

#15. Take a single digit and print its name in words (e.g., 3 -> "Three").
digit_words = {
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
}

digit = input("Enter a single digit (0-9): ")

if digit in digit_words:
    print(digit_words [digit])
else:
    print("Invalid input. Please enter a single digit between 0 and 9.")
































