bruin = {'Boxtel','Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel','Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print('[Stations bij beide trajecten.]')
print(bruin.intersection(groen), '\n')

print('[Stations met bruin zonder groen.]')
print(bruin.difference(groen), '\n')

print('[Stations met groen en zonder bruin.]')
print(groen.difference(bruin), '\n')

print('[Alle stations]')
print(bruin.union(groen))