#prints all Fibonacci numbers less than or equal to 100
'''a = 0
b = 1

while a<=100:
    print(a)
    a,b = b,a+b

fact = 1

num = int(input("enter a number:"))
i = 1
while i <=num:
    fact*=i
    i+=1

print(fact)

n = int(input("enter a number:"))
fact = 1

for i in range(n):
    fact *= (i+1)
print(fact)

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(4-1-i):
        print(" ", end=" ")
        for z in range(i+1):
            print("*", end=" ")
    print()

num = 1

for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()

for i in range(4):
    for j in range(i):
        print("", end=" ")
    
    if i==0:
        for x in range(1,5):
            print(x, end=" ")
    
    elif i == 1:
        print(2, end=" ")
        print(3, end=" ")
        print(2, end=" ")

    elif i == 2:
        print(3, end=" ")
        print(2, end=" ")

    else:
        print(4, end=" ")

    print()

for i in range(5):
    for j in range(4-i):
        print(" ", end=" ")
    
    for x in range(i+1):
        print(x+1, end=" ")
    print()


for i in range(4):
    for j in range(i+1):
        print(j+1, end=" ")

    for x in range(i, 0, -1):
        print(x, end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(65+i+j), end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(68-j), end=" ")
    print()

for i in range(4):
    for j in range(i+1, 0, -1):
        print(chr(64+j), end=" ")
    print()'''

''' 1
2 2 
3 3 3 
4 4 4 4 
3 3 3
2 2
1 for this code'''
'''for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(3, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

#write a program to print all factors of a number entered by the user. 
num = int(input("enter a number: "))
for i in range(1, num+1):
    if num%i==0:
        print(i, end=" ")

#write a program to find factorial of number entered by user. 
num = int(input("enter a number: "))

fact = 1

for i in range(1, num+1):
    fact*=i
print("Factorial: ", fact)

#write a program to count how many factors a number has. 

num = int(input("enter a number:"))

count = 0 

for i in range(1, num + 1):
    if num%i==0:
        count+=1
print("number of factors:", count)

#write a program to check whether a nmber is prime or not.
num = int(input("enter a number:"))

count = 0

for i in range(1, num+1):
    if num%i == 0:
        count+=1
if count == 2:
    print("prime number")
           
else:
    print("not prime")'''



for num in range(1, 51):
    count = 0 

    for i in range(1, num+1):
        if num%i== 0:
            count+=1
    if count == 2:
       print(num, end=" ")



    


























































































































































