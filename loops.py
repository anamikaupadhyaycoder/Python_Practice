# print the elements of the following list using a loop:
'''li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in li:
    print(val)
else:
    print("End of loop")'''

#Search for a number x in this tupel using loop:

tu = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1)

x = 1

idx = 0

for val in tu:
    if(val == x):
        print("number x is found at idx", idx)
    idx += 1
        
        
    







