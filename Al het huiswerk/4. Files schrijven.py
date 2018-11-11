
import datetime
namen = ["Miranda", "Piet", "Sacha", "Karel", "Kemal"]
Hardlopers = open("hardlopers.txt", "a")

for name in namen:
    Hardlopers.write("{}, {}\n".format(datetime.datetime.today().strftime("%a %d %b %Y"), name))
Hardlopers.close()

Hardlopers = open("hardlopers.txt", "r")

for line in Hardlopers.readlines():
    print(line)
Hardlopers.close()