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

    print()'''

for i in range(4):

    # spaces
    for j in range(i):
        print("", end=" ")

    # first/increasing part
    for j in range(4 - 2*i):
            print(i + j + 1, end=" ")

    # second/decreasing part
    for j in range(i):
        print(2, end=" ")

    print()
    
    
    
    























































































































































