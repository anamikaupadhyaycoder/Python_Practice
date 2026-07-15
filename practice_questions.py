# write a recursive function to calculate the sum of first n natural numbers.

'''def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n


sum = calc_sum(6)
print(sum)'''

# Write a recursive function to print all elements in a ist.
# Hint: use list and index as parameters


names = ["anamika", "aayushi", "isha", "shreya"]

def fun_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print(names)
    

