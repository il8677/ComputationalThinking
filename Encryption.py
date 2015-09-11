alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptions = []
class var:
        def __init__(self, obj): self.obj = obj;
        def get(self):    return self.obj
        def set(self, obj):      self.obj = obj
class reverse:
    name = "reverse"
    def start(self, encrypt, sentance):
        done = False;
        if encrypt == False:
            self.decrypt(sentance)
        else:
            self.encrypt(sentance)
    def encrypt(sentence):
        final = ""
        i = len(sentence) -1
        while(i != -1):
            final+= sentence[i];
            i -= 1
        return  final;
    def decrypt(sentence):
        final = ""
        i = len(sentence) -1
        while(i != -1):
            final+= sentence[i];
            i -= 1
        return  final;

class caesar:
    name = "caesar"
    def start(self, encrypt, sentance):
        done = False;
        while (not done):
            try:
                key = int(input("Whats the key? "))
                done=True
            except TypeError:
                print("ERROR, NON-INT INPUTED")
                done = False
        if encrypt == False:
            self.decrypt(key, sentance)
        else:
            self.encrypt(key, sentance)

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

encryptions.append(var(caesar()))
encryptions.append(var(reverse()))

encryptionType = input("What cipher do you want to use? Reverse/Caesar: ").lower()
sentance = input("What sentance do yo want to encrypt/decrypt? " ).upper()
done = False;

while (not done):
    endy = input("Encrypt or decrypt? ").upper()
    if endy == "ENCRYPT" or "DECRYPT":
        done = True;
    else:
        print("ANSWER NOT ENCRYPT OR DECRYPT")


for encryption in encryptions:
    if encryption.get().name == encryptionType:
        if endy == "ENCRYPT":
            print("Encrypting")
            print(encryption.get().start(True, sentance))
        else:
            print(encryption.get().start(False, sentance))
            print("Decrypting")
    else:
        print("FATAL ERROR, NON ENCRYPTION TYPE INPUTED")