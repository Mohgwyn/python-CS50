x = input("Expression: ")

x, y, z = x.split(" ")

x = int(x)
z = int(z)

if y == "+":
    r = x + z
elif y == "-":
    r = x - z
elif y == "*":
    r = x * z
else:
    r = x / z

print(r)