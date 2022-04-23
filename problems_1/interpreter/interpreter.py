x = input("Expression: ")

x, y, z = x.split(" ")

#we have to use floats to get the appropriate result
x = float(x)
z = float(z)

if y == "+":
    r = x + z
elif y == "-":
    r = x - z
elif y == "*":
    r = x * z
else:
    r = x / z

print(r)