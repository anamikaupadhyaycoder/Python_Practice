# WAP to find the sum of first n numbers. (using while)

'''n = 5

sum = 0
for i in range(1, n+1):# range(1, n+1(6)) it means range starts from 1 and ends just before 6 
    sum+=i

print("total number of sum:", sum)'''


#WAP to find the factorial fo first n numbers. (using for)

n = 5

factorial = 1
'''for i in range(1, n+1):
    factorial*=i
    # factorial*i
    print("factorial:", factorial)'''


'''n = 8

fact = 1
for i in range(1, n+1):
    fact *= i
    print("factorial:", fact)'''










# Assignment - Write a program that takes a sentence and prints:
# total characters
# uppercase version
# lowercase version

pr = input("enter a sentence:")
print(len(pr))
pr_1 = pr.upper()
pr_2 = pr.lower()

print(pr_1)
print(pr_2)


#Assignment - write a phython program that takes any wotd or sentence as input and prints:
#The first character 
#The last character
#The toatal number of characters

pro = input("enter a sentence")
print(pro[0])
print(pro[-1])
print(len(pro))









