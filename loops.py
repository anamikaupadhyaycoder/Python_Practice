#1. Print numbers from 1 to 10 using a while loop.
'''i = 0

while i <10:
    i+=1
    print(i)

#2. Without using range(), write a while loop to print:
i = 10

while i >=1:
    print(i)
    i-=1

#3. Using a while loop, print only the even numbers from 2 to 20.
    
i = 2

while i<=20:
    print(i)
    i+=2
 
#4. Without using range() or a list, write a while loop to print all multiples of 7 from 7 to 70.
i = 7
while i <= 70:
    print(i)
    i+=7

#5. Print the squares of the numbers from 1 to 10 using a while loop
i = 1

while i <=10:
    print(i**2)
    i+=1

#6. Print the sum of the numbers from 1 to 10 using a while loop.
total = 0
i = 1

while i <= 10:
    total+=i
    i+=1
print("sum:", total)

#7. Find the sum of all even numbers from 1 to 100.
total = 0
i = 2

while i <= 100:
    total+=i
    i+=2
print(total)

#8. Find the sum of all odd numbers from 1 to 99 using a while loop.
total = 0
i = 1

while i<=99:
    total+=i
    i+=2
print("sum:", total)

#9. Count how many numbers are divisible by 3 between 1 and 20.
count = 0 
i = 1

while i <20:
    if i%3==0:
        count+=1
    i+=1
        
print("count:", count)

#wap to perform sum of digits function

num = 345
total = 0 

while num > 0:
    digit = num%10
    total+=digit
    num//=10
print("sum of digits:", total)

n = 7 
a = 0
b = 1
count = 0

while count < n:
    print(a)
    a,b=b,a+b
    count+=1'''
#prints all Fibonacci numbers less than or equal to 100
'''a = 0
b = 1

while a<=100:
    print(a)
    a,b = b,a+b'''

fact = 1

num = int(input("enter a number:"))
i = 1
while i <=num:
    fact*=i
    i+=1

print(fact)




























































































































































