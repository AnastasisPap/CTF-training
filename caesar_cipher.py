code = input("Enter text to decipher: ")
code = code.split()
letters = [chr(i+ord('a')) for i in range(26)]


for i in range(1, 27):
    s = ''
    for item in code:
        for char in item:
            idx = letters.index(char)
            s += letters[(idx+i)%26]
        s += ' '
    print(f"Key {i}: {s}")
    
