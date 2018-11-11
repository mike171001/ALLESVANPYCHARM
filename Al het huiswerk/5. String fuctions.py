def gemiddelde():
    zin = input("Vul een willekeurige zin in: ").split(" ")
    som = 0
    for woord in zin:
        som += len(woord)
    print("Gemiddelde aantal karakters per woord:",float((som / len(zin))))
gemiddelde()