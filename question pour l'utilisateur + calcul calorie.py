age = input("Quel âge avez-vous ? ")
"Quel âge avez-vous ? " 
print(age)
intage = int(age)
print(intage)


sexe = input("Êtes vous un homme ou une femme ?")
"Êtes vous un homme ou une femme ?"
print(sexe)


activitephysique = input("A quelle fréquence pratiquez vous une activité physique chaque semaine?")
"A quelle fréquence pratiquez vous une activité physique chaque semaine?"
print(activitephysique)
intactivitephysique = int(activitephysique)


weight = input("Quel est votre poids (en kg)?")
"Quel est votre poids (en kg)?"
print(weight)
intweight = float(weight)
"Quel est votre poids (en kg)?"
print(intweight)


size = input("Quel est votre taille (en cm)?")
"Quel est votre taille (en cm)?"
print(size)



if sexe == 'femme':
    metabolismedebasefemme = 447.593 + (9.247*intweight) + (3.098*intsize) - (4.330*intage)
    a=metabolismedebasefemme
    print(a)

else: 
    metabolismedebasehomme = 88.362 + (13.397*intweight) + (4.799*intsize) - (5.677*intage)
    a=metabolismedebasehomme
    print(a)


if intactivitephysique < 1:
    a=1.2*a 
elif 1 <= intactivitephysique <= 3:
    a=1.375*a
elif 4 <= intactivitephysique <= 6:
    a=1.55*a 
else: 
    a=1.725*a 
print(a)



glucides = (55/100)*a
print(glucides)
proteines = (30/100)*a
print(proteines)
graisses = (15/100)*a
print(graisses)
