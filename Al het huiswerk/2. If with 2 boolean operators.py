leeftijd= input("Geef je leeftijd? ")
Paspoort= input("Heeft u een nederlands paspoort? ")
if int(leeftijd) >18 and Paspoort == "ja":
    print("Gefeliciteerd u mag stemmen")
else:
    print("Helaas u mag niet stemmen")