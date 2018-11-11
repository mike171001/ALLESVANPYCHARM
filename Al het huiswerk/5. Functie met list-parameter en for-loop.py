
def kwadraten_som(grondgetallen):
    totaal = 0

    for getal in grondgetallen:
        if getal >0:
            antwoord = getal **2
            totaal = totaal + antwoord
    return totaal

grondgetallen = [4, 5, 3, -81]
x = kwadraten_som(grondgetallen)
print(x)
