def main():
    camel = input("Enter camelcase: ")
    camel2snake(camel)
    
def camel2snake(camel):
    for char in camel:
        if char.isupper():
            print(f"_{char.lower()}", end="")
        else:
            print(char, end="")
    
if __name__ == "__main__":
    main()