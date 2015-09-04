done = False
while not done:
    alpha="abcdefghijklmnopqrstuvwxyz"
    userInput = input("What letter position do you want to find? ")
    if userInput == "exit":
        done = True
    else:
        print(alpha.find(userInput.lower()) + 1)