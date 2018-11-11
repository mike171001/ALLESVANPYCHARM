def inlezen_beginstation(stations):
    while True:
        beginstation = input("Wat is uw beginstation: ")

        if beginstation in stations:
            return beginstation
        else:
            print("Dit station staat niet in het traject.")

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input("Wat is uw eindstation: ")

        if eindstation in stations:
            if stations.index(beginstation) < stations.index(eindstation):
                return eindstation
            elif stations.index(beginstation) == stations.index(eindstation):
                print("U bent al op dit station.")
            else:
                print("U heeft dit station gemist {} ligt voor {} op de route.".format(eindstation, beginstation))
        else:
            print("De ingevoerde stationsnaam is hier niet.")

def omroepen_reis(stations, beginstation, eindstation):
    BeginIndex = stations.index(beginstation)
    EindIndex = stations.index(eindstation)

    print("\nHet beginstation {}e is het {}e station in het traject".format(beginstation, BeginIndex + 1))
    print("Het eindstation {}e is het {}e station in het traject".format(eindstation, EindIndex + 1))
    print("De trein passeert", (EindIndex - BeginIndex), "station(s)")
    print("De prijs van het kaartje is", ((EindIndex - BeginIndex) * 5),"euro\n")

    print("U stapt in op:", beginstation)
    for i in range(BeginIndex + 1, EindIndex):
        print(stations[i])
    print("U stapt uit op:", eindstation)

stations = [
    "Schagen",
    "Heerhugowaard",
    "Alkmaar",
    "Castricum",
    "Zaandam",
    "Amsterdam Sloterdijk",
    "Amsterdam Centraal",
    "Amsterdam Amstel",
    "Utrecht Centraal",
    "\'s-Hertogenbosch",
    "Eindhoven",
    "Weert",
    "Roermond",
    "Sittard",
    "Maastricht",
]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)