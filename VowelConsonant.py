vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyz"
consonants+=consonants.upper()
#The f means final, I thought acually writing final would take to long
fvowels = ""
fcon=""
fother=""
userInput = input("Please input sentance to split: ")
print ("Splitting sentance: " + userInput)
#Iterates through inputed charecters
for char in userInput:
    #Checks if the current iterated charecter is a vowel
    if char in vowels:
        fvowels += char
    #Checks if the current iterated charecter is a consonant
    elif char in consonants:
        fcon+= char
    #Otherwise
    else:
        fother += char
print("Process Completed")
print("Vowels: " + fvowels)
print("Consonants: " + fcon)
print("Other: "+fother)