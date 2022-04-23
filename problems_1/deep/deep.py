def main():
    x = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    x = x.lower().lstrip().rstrip()

    if is_answer(x):
        print("yes")
    else:
        print("no")

def is_answer(str):
    if str == "42" or str == "forty-two" or str == "forty two":
        return True
    else:
        return False

main()