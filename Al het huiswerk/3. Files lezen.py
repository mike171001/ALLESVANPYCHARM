file = open('Kaartnummers.txt')
regels= file.readlines()
file.close()

getal = []
for regel in regels:
    getal.append(regel.split(', ')[0])
    hoogstegetal= max(getal)

print('deze file telt {} regels '.format(len(regels)))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(hoogstegetal, getal.index(hoogstegetal)+1 ))
