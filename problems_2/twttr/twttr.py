def main():
    twttr = input("String to shorten: ")
    for char in twttr:
        if not is_vowel(char):
            print(char, end="")

def is_vowel(c):
    c = c.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return True
    else:
        return False

if __name__ == "__main__":
    main()