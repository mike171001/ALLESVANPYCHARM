
while True:
    Woord = input("Geef een woord op met 4 letters")
    if len(Woord) == 4:
        break
    else:
        print(Woord, "heeft {} letters".format(len(Woord)))
print("Inlezen van correcte string {} is geslaagd" .format(Woord))