letters = [chr(i + ord('a')) for i in range(26)]


def get_formatted_key(n, key):
    formatted_kw = key * ( n // len(key) )
    for i in range(n%len(key)):
        formatted_kw += key[i]
    return formatted_kw


def encode():
    code = input("Enter text to encode: ").lower()
    keyword = input("Enter keyword: ").lower()
    formatted_kw = get_formatted_key(len(code), keyword)
    
    encoded = ''
    
    for i in range(len(code)):
        idx = (letters.index(code[i]) + letters.index(formatted_kw[i])) % 26
        encoded += letters[idx]

    print("Encoded text:", encoded)


def decode():
    code = input("Enter text to decode: ").lower()
    keyword = input("Enter the keyword: ").lower()
    formatted_kw = get_formatted_key(len(code), keyword)

    decoded = ''
    for i in range(len(code)):
        idx = (letters.index(code[i]) - letters.index(formatted_kw[i]) + 26) % 26
        decoded += letters[idx]

    print("Decoded text:", decoded)



def main():
    choice = int(input("Choose 1 to encode or 2 to decode: "))

    if choice == 1:
        encode()
    else:
        decode()


if __name__ == '__main__':
    main()
