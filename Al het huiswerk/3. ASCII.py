def code(invoerstring):
    return "".join([chr(ord(letter) + 3) for letter in invoerstring])

Name = input("Voer uw naam in: ")
Beginstation = input("Voer uw beginstation in: ")
Eindstation = input("Voer uw eindbestemming in: ")
print(code(Name + Beginstation + Eindstation))