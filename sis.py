#conditional statements

light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")


age = 24

if(age > 18):
    print("can vote") #indentation
else:
    print("cannot vote")

age = 41
if(age >= 18):
    if(age >= 40):
        print("cannot drive")
    else: 
            print("can drive")
else:
    print("cannot drive")           
    
