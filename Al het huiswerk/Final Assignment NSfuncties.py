def standaardprijs(afstandKM):
    if afstandKM < 0:
        afstandKM = 0
    if afstandKM <= 50:
        afstandKM = afstandKM * 0.80
    else:
        afstandKM = 15 + (0.60 * afstandKM)
    return afstandKM

def ritprijs(leeftijd, weekendrit, afstandKM):
    antwoord= standaardprijs(afstandKM)
    if (leeftijd < 12 or leeftijd) >= 65 and weekendrit == False:
        antwoord = antwoord * 0.7
    elif (leeftijd < 12 or leeftijd >= 65) and weekendrit == True:
        antwoord = afstandKM * 0.65
    elif (leeftijd >=12 or leeftijd < 65) and weekendrit == True:
        antwoord = afstandKM * 0.6
    return antwoord


lijst1 = standaardprijs(52)
ritprijs(14, False, lijst1)


