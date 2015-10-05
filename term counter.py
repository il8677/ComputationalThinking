termn = input("Number of Terms: ")
termn = int(termn)
terms = []
final =0
for i in range (0, termn):
    cu = input("Term " +str(i + 1)+ ": ")
    cu = int(cu)
    terms.append(cu)
for item in terms:
    final += item
print(final)