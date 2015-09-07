#NUMBER TO LETTER BY ISAAC L
done = False
while not done:
    alpha="abcdefghijklmnopqrstuvwxyz"
    userInput = input("Input a number and this app will convert it into the letter corresponding to the position in the alphabet: ")
    if userInput == "exit":
        done = True
    if userInput == "0":
        print("Dont type 0... thats just mean...")
    else:
        try:
            print(alpha[int(userInput) - 1])
        except IndexError:
            print("INDEX ERROR: STRING INDEX OUT OF RANGE (Your number exceeded 26)")
        except ValueError:
            print("VALUE ERROR: EXPECTED TYPE INT (Your number was not a number)")