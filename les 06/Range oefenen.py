getallenrij = [2, 4, 6, 8, 10, 9, 7]
getal = int(input('welk getal? '))
gevonden = False
if getal in getallenrij:
    gevonden = True
    print(gevonden)
else:
    print( 'Het nummer' + gevonden + zit niet in de lijst)