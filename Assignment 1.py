#question - Take diameter as input and calculate area of a circle
diameter_input = input("enter diameter of circle: ", )
diameter = float(diameter_input)
radius = diameter/2
pi = 3.14
area = pi*(radius ** 2)
print("the  area of the circle is : ", area)