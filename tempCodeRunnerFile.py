#3. Keep asking the user for input until they type "exit".


while True:
    user = input("enter a input:")
    if user.strip().lower() == "exit":
        print("Goodbye")
        break
    print(user)