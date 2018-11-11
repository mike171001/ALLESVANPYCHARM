import xmltodict

def processXML(filename):
    with open(filename) as XMLFile:
        return xmltodict.parse(XMLFile.read())

stations = processXML('allestations.xml')

print('Dit zijn de codes en types van de {} stations:'.format(len(stations)))
for station in stations['Stations']['Station']:
    print('{:5}- {}'.format(station['Code'], station['Type']))

print('\nDit zijn alle stations met 1 of meer synoniemen:')
for station in stations['Stations']['Station']:
    if station['Synoniemen']:
        print('{:5}- {}'.format(station['Code'], station['Synoniemen']))

print('\nDit is de lange naam van elk station:')
for station in stations['Stations']['Station']:
    print('{:5}- {}'.format(station['Code'], station['Namen']['Lang']))