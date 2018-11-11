def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()
    aantalregels= len(regels)
    aantalvrij = 12-aantalregels
    print(aantalvrij)

def nieuwe_kluis():
    kluisnummers = []
    for i in range(1, 13):
        kluisnummers.append(i)

    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    infile.close()

    for regel in regels:
        kluisinfo = regel.split(';')
        nummer = int(kluisinfo[0])
        kluisnummers.remove(nummer)

    if len(kluisnummers) > 0:
        kluisnummer = kluisnummers[0]
        print('Je kluisnummer is {}'.format(kluisnummer))
        code = input('Wat is je code: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('\n{};{}'.format(kluisnummer, code))
        outfile.close()
    else:
        print('Er is geen kluis meer vrij!')

def kluis_openen():
    nummer= input('Wat is je nummer? ')
    code= input('Wat is je code? ')
    infile=open('kluizen.txt', 'r')
    regels= infile.readlines()
    infile.close()
    for regel in regels:
        kluisinfo= regel.split(';')
        kluisnummer = kluisinfo[0]
        kluiscode = kluisinfo[1].strip()
        gegevenscorrect = nummer == kluisnummer and code== kluiscode
        if gegevenscorrect == True and code==kluiscode:
            print('De kluis wordt geopend')


print('1. Ik wil weten hoeveel kluizen nog vrij zijn ')
print('2. Ik wil een nieuwe kluis')
print('3. Ik wil even iets uit mijn kluis halen')
keuze = int(input('geef keuze'))
if keuze == 1:
    toon_aantal_kluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
elif keuze == 3:
    kluis_openen()
else:
    print('Foute keuze')