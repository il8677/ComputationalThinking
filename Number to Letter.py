#NUMBER TO LETTER BY ISAAC L
done = False
while not done:
    alpha="abcdefghijklmnopqrstuvwxyz"
    userInput = input("Input a number and this app will convert it into the letter corresponding to the position in the alphabet: ")
    if userInput == "exit":
        done = True
    else:
        print(alpha[int(userInput) - 1])