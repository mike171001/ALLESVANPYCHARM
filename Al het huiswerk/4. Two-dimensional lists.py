studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   antwoord = []
   for studentcijfers in studentencijfers:
       antwoord.append(sum(studentcijfers) / len(studentcijfers))
   return antwoord

def gemiddelde_van_alle_studenten(studentencijfers):
   antwoord = 0
   cijfers = 0
   for studentcijfers in studentencijfers:
       for cijfer in studentcijfers:
           antwoord += cijfer
           cijfers += 1
   return antwoord / cijfers

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))