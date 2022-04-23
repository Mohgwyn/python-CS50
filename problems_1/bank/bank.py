x = input("Greetings: ")
x = x.lower().lstrip()

if x.find("hello") == 0:
    print("$0")
elif x.find("h") == 0:
    print("$20")
else:
    print("$100")