print("Welcome to the Caesar Cipher Hacker")
sentance = input("Please enter your encrypted message: ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decrypt(key, sentance):
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
        return returnMessage
print("Brute forcing")

for i in range(0, alphabet.__len__()):
    print(decrypt(i, sentance))