while True:
    try:
        aantal = int(input('Aantal mensen: '))
        if aantal < 0:
            raise ValueError('Negatieve getallen zijn niet toegestaan!')
        print('Prijs per persoon:', (4356.0 / aantal))
    except TypeError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except ZeroDivisionError:
        print('Delen door 0 kan niet!')
    except ValueError:
        print('Onjuiste invoer!')