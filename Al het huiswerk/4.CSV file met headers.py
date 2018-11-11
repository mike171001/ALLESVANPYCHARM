import csv

product_info = [
    { 'artikelnummer': 121, 'artikelcode': 'ABC123', 'naam': 'Highlight pen', 'voorraad': 231, 'prijs': 0.56 },
    { 'artikelnummer': 123, 'artikelcode': 'PQR678', 'naam': 'Nietmachine', 'voorraad': 587, 'prijs': 9.99 },
    { 'artikelnummer': 128, 'artikelcode': 'ZYX163', 'naam': 'Bureaulamp', 'voorraad': 34, 'prijs': 19.95 },
    { 'artikelnummer': 137, 'artikelcode': 'MLK709', 'naam': 'Monitorstandaard', 'voorraad': 66, 'prijs': 32.50 },
    { 'artikelnummer': 271, 'artikelcode': 'TRS665', 'naam': 'Ipad hoes', 'voorraad': 155, 'prijs': 19.01 }
]

with open('producten.csv', 'w', newline='\n') as WriteCSVFile:
    writer = csv.writer(WriteCSVFile, delimiter=';')
    writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))

    for product in product_info:
        writer.writerow((
            product['artikelnummer'],
            product['artikelcode'],
            product['naam'],
            product['voorraad'],
            product['prijs']))

with open('products.csv', 'r', newline='\n') as ReadCSVFile:
    top = { 'naam': '', 'prijs': 0.0 }
    low = { 'artikelnummer': 0, 'voorraad': 1000 }
    total_voorraad = 0
    reader = csv.DictReader(ReadCSVFile, delimiter=';')

    for row in reader:
        total_voorraad += int(row['voorraad'])
        if float(row['prijs']) > top['prijs']:
            top['naam'] = row['naam']
            top['prijs'] = float(row['prijs'])
        if int(row['voorraad']) < low['voorraad']:
            low['artikelnummer'] = int(row['artikelnummer'])
            low['voorraad'] = int(row['voorraad'])

    print('Het duurste artikel is {} en die kost {} Euro'.format(top['naam'], top['prijs']))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(low['voorraad'], low['artikelnummer']))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(total_voorraad))