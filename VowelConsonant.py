vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyz"
consonants+=consonants.upper()
#The f means final, I thought acually writing final would take to long
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
