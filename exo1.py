nom = "Allery"
prenom = "Tatiana"
annee_naissance = 1997
taille = 1.65
etudiant = False

#print(f"Bonjour je m'appelle {prenom} {nom}, et j'ai {2025-annee_naissance} ans")
#print(type(taille))

fruits = ["pomme", "clementine", "banane", "fruit de la passion"]
#print(fruits)
fruits[1] = "patate"
#print(fruits)

#ajout a une liste avec .append
fruits.append("abricot")
#print(fruits)

#retirer à une liste avec .remove
fruits.remove("patate")
#print(fruits)

#longueur de la liste
len(fruits)

#classer par orre alphabétique
fruits.sort()
#vérifier par un booléen si c'est présent ddans la liste
"banane" in fruits

#les dictionnaires
dictionnaire_fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}
#ajout d'un élément dans un dictionnaire : ajout de la clé = valeur
dictionnaire_fruits["kiwi"]  = "vert"
#stocker une valeur d'un dictionnaire dans un variable
couleur_banane = dictionnaire_fruits["banane"]

#changer la valeur d'une clé
dictionnaire_fruits["pomme"] = "vert"

del dictionnaire_fruits["pomme"]

contact = []
contact.append(dictionnaire_fruits)
print(contact)
