print("Welcome to the F.A.T C.A.T program, this program encrypts messages using the reverse cipher method") #Prints whats in the parenteses
sentence = input("What do you want to encrypt? ") #Declares a varible and stores what the user inputs
final = ""
i = len(sentence) -1
while(i != -1):
    final+= sentence[i];
    i -= 1
print(final)