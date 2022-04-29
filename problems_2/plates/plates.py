def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start_2_letters(s[0:1]) and valid_tam(s) and no_mid_nums(s) and no_special_chars(s): #to do no_mid_nums and no_special_chars
        return True
    else:
        return False

def start_2_letters(s):
    count = 0
    for c in s:
        if c.isalpha():
            count += 1
    if count == 2:
        return True
    else:
        return False

def valid_tam(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def no_mid_nums(s):
    #todo
    print()

def no_special_chars(s):
    #todo
    print()

if __name__ == "__main__":
    main()