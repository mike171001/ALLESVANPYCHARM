def namen():
    namen = {}
    while True:
        naam_in = input('Volgende naam: ')
        if len(naam_in) == 0:
            for naam, voorkomst in namen.items():
                if voorkomst == 1:
                    print('Er is {} student met de naam {}'.format(voorkomst, naam))
                elif voorkomst > 1:
                    print('Er zijn {} studenten met de naam {}'.format(voorkomst, naam))
            break
        else:
            naam_bestaat = namen.keys()
            if naam_in in naam_bestaat:
                namen[naam_in] += 1
            else:
                namen[naam_in] = 1
namen()