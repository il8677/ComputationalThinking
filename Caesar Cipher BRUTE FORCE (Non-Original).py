print("Welcome to the Caesar Cipher Hacker")
sentance = input("Please enter your encrypted message: ").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Brute forcing")

for key in range(0, alphabet.__len__()):
    returnMessage = ""
    for char in sentance:
        pos = alphabet.find(char)
        if char not in alphabet:
            returnMessage += char
        else:
            if pos - key < 0:
                returnMessage+= alphabet[pos - key + 26]
            else:
                returnMessage += alphabet[pos - key]
    print(str(key) + ": "+str(returnMessage))
