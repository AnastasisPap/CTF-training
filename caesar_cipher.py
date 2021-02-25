letters = [chr(i+ord('a')) for i in range(26)]
def decode():
    code = input("Enter text to decipher: ").split()


    for i in range(1, 27):
        s = ''
        for item in code:
            for char in item:
                idx = letters.index(char)
                s += letters[(idx+i)%26]
            s += ' '
        print(f"Key {i}: {s}")
    



def encode():
    code = input("Enter text to encode: ").split()
    shifts = int(input("Enter amount of shifts 1-26: "))
    
    s = ''
    for item in code:
        for char in item:
            idx = letters.index(char)
            s += letters[(idx-shifts+26)%26]
        s += ' '
    print(f"Encoded text: {s}")


def main():
    choice = int(input("Type 1 to encode or 2 to decode: "))
    if choice == 1:
        encode()
    else:
        decode()


if __name__ == '__main__':
    main()
