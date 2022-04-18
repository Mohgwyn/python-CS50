def main():
    str = input("Enter emoticons to be transformed into emojis: ")
    print(convert(str))

def convert(str):
    str = str.replace(":)","🙂")
    str = str.replace(":(","🙁")
    return str

main()