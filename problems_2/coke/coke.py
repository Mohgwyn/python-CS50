def main(price):
    change = machine(price)
    print(f"Change owed: {change}")
     

def enter_coin():
    while True:
        n = int(input("Enter a coin: "))
        if n == 25 or n == 10 or n == 5:
            return n
        else:
            print("That's not a valid coin.")

def machine(price):
    paid = 0
    while paid < price:
        coin = enter_coin()
        paid += coin
        print(f"Amount due: {paid}")
    return paid - price

if __name__ == "__main__":
    main()