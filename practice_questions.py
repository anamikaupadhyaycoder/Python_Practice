#Takes 10 numbers from the user and counts how many numbers are greater than the previous number.

previous_num = int(input("enter a number:"))
count = 0

for i in range(1,10):
    num=int(input("enter a number:"))
    if num>previous_num:
        count+=1
    previous_num=num
print(count)
#Takes 10 numbers from the user and counts how many times the current number is smaller than the previous number.

previous_num=int(input("enter a numbe:"))

count=0

for i in range(1,10):
    num=int(input("enter a number:"))
    if num<previous_num:
        count+=1
    previous_num=num
print("number of decreases:", count)

#Take 10 numbers and find the largest difference between two consecutive numbers.
previous_num=int(input("enter a number:"))

diff = 0 
largest_diff=0
for i in range(1,10):
    num=int(input("enter a number:"))
    diff = num-previous_num
    diff=abs(diff)
    if diff>largest_diff:
        largest_diff=diff
    previous_num=num
print(largest_diff)

#Takes 10 numbers from the user and finds the largest number and the position at which it was entered.

largest_num=0
position=0

for i in range(1,11):
    num=int(input("enter a number:"))

    if largest_num is None or num>largest_num:
        largest_num=num
        largest_num=num
        position=i

print(largest_num)
print(position)


