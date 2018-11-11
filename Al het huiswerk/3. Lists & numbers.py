invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen = [int(i) for i in invoer.split('-')]
getallen.sort()
print("Gesorteerde list van ints:", getallen)
print("Grootste getal:", max(getallen), "en Kleinste Getal:", min(getallen))
print("Aantal Getallen:", len(getallen), "Som van de Getallen:", sum(getallen))
print("Het gemiddelde is:", sum(getallen)/len(getallen))