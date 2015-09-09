alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
final = ""
def reverse(sentance):

def encrypt(key, sentance):
    returnMessage = ""
    for char in sentance:
        pos = alphabet.find(char)
        if char not in alphabet:
            returnMessage += char
        else:
            if pos + key > 25:
                returnMessage+= alphabet[pos + key - 26]
            else:
                returnMessage += alphabet[pos + key]
    return returnMessage
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
sentance = input("What sentance do yo want to encrypt/decrypt? " ).upper()
done = False;
while (not done):
    try:
        key = int(input("Whats the key? "))
        done=True
    except TypeError:
        print("ERROR, NON-INT INPUTED")
done = False
while (not done):
    endy = input("Encrypt or decrypt? ").upper()
    if endy == "ENCRYPT" or "DECRYPT":
        done = True;
    else:
        print("ANSWER NOT ENCRYPT OR DECRYPT")
if endy =="ENCRYPT":
    print("Encrypting...")
    print(encrypt(key, sentance))
else:
    print("Decrypting")
    print(decrypt(key, sentance))