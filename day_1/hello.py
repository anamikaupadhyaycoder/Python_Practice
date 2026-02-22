# name = input("enter your name: ")
# age = int(input("enter age: "))
# marks = input("enter marks: ")

# print("Welcome", name)
# print("age = ", age)
# print("marks = ", marks)
# print(type(age), age)



a = "Pythonprogramming"
b = "Datascience"
c = [5, 10, 15, 20, 25]
d = (2, 4, 6, 8, 10)

x = a[0] + a[-1]
y = b[4:11]
z = c[1] + d[2]

m = c[-1]*2
n = d[1] + c[2]

p = str(z) + str(m)
q = int(c[3] / d[0])

r = a[6:13] + b[-3:]
s = c[::2]
t = d[::-1]

u = str(s[1]) + str(t[2])

final = x + y + p + r + u + str(q)

print(x, y, z, m, n, p, q, r, s, t, u)
print(final)