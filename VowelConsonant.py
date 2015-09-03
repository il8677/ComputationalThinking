vowels = ["a","e","i","o","u"]
fvowels = ""
fcon=""
userInput = input("Please input sentance to split: ")
print ("Splitting sentance: " + userInput)
for char in userInput:
    if char in vowels:
        fvowels += char
    else:
        fcon += char
print("Process Completed")
print("Vowels: " + fvowels)
print("Consonants: " + fcon)