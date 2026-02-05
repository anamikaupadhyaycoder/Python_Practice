a = int(input("weight: ")) #Q3
if a > 25: 
  print("warning: luggage exceeds the allowed limit of 25 kg.")

pi = float(input("pi: "))
r = float(input("radius: "))
Volume = (4/3) * pi * r**3
print("volume of the sphere =", Volume)

a = float(input("marks: "))
if a >= 80:
    print("Excellent")
b = float(input("marks: "))    
if b >= 65 <80:
  print("Good")
c = float(input("marks: ")) 
if c >= 50 <65:
   print("Pass")
d = float(input("marks: "))   
if d < 50:
   print("Fail")