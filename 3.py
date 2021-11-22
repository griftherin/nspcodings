userName = input("Please type in your name: ")
Age_str = int(input("Hello " + userName + "," + " how old are you?"))
if type(Age_str) == int:
    print("So " + userName + ", you mean you are just", Age_str, "years old?")
else:
    print("Your age should be a number")