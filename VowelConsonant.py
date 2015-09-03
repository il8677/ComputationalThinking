vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyz"
consonants+=consonants.upper()
fvowels = ""
fcon=""
fother=""
userInput = input("Please input sentance to split: ")
print ("Splitting sentance: " + userInput)
for char in userInput:
    if char in vowels:
        fvowels += char
    elif char in consonants:
        fcon+= char
    else:
        fother += char
print("Process Completed")
print("Vowels: " + fvowels)
print("Consonants: " + fcon)
print("Other: "+fother)