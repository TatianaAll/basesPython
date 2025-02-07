def salaire_mensuel (salaire_annuel):
    return round(int(salaire_annuel)/12)

def salaire_hebdomadaire(salaire_mensuel):
    return round(salaire_mensuel/4)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return round(salaire_hebdomadaire/int(heures_travaillees))

salaire_annuel = input("Renseignez votre salaire annuel : ")
salaire_mensuel_perso = salaire_mensuel(salaire_annuel)
#print("salaire par mois : ", salaire_mensuel_perso, "€")
salaire_hebdo_perso = salaire_hebdomadaire(salaire_mensuel_perso)
#print("salaire par semaine : ", salaire_hebdo_perso, "€")

heure_semaine = input("Nombre d'heure par semaine : ")
salaire_horaire_perso = salaire_horaire(salaire_hebdo_perso, heure_semaine)
print("Salaire par heure : ", salaire_horaire_perso, "€ par heure")
