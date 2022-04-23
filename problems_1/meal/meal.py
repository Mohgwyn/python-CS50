def main():
    x = input("What time is it? ")
    time = convert(x)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()