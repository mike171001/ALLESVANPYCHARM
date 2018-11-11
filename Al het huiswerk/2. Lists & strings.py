num_strings = 0
string = []
new_strings = []

while num_strings != 10:
    string.append((input("Vul hier een woord in")))
    num_strings += 1

for i in range(len(string)):
    if len(string[i]) == 4:
        new_strings.append(string[i])
print("De nieuw-gemaakte lijst met alle vier-letter strings is: ")
print(new_strings)