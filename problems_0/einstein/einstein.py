def einstein(mass):
    E = mass * pow(30,2)
    return E

def main():
    mass = int(input("m: "))
    E = einstein(mass)
    print(f"E: {E}")

main()