nums = []
while True:
    Getallen = float(input("Geef een getal: "))
    if Getallen == 0:
        break
    nums.append(Getallen)
print("Er zijn", len(nums), "getallen ingevoerd, de som is:", sum(nums))
