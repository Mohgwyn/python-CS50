def main(price):
    change = machine(price)
    print(f"Change owed: {change}")
     

def enter_coin(price, paid):
    while True:
        n = int(input("Enter a coin: "))
        if n == 25 or n == 10 or n == 5:
            return n
        else:
            print(f"That's not a valid coin. Amount due: {price-paid}")

def machine(price):
    paid = 0
    while paid < price:
        print(f"Amount due: {price-paid}")
        coin = enter_coin(price, paid)
        paid += coin
    return paid - price

if __name__ == "__main__":
    main()