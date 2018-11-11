import xmltodict

def processXML(filename):
    with open(filename) as XMLFile:
        return xmltodict.parse(XMLFile.read())

producten = processXML('producten.xml')
producten = producten['artikelen']['artikel']

for product in producten:
    print(product['naam'])