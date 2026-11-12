#coding : utf-8
#Nom du fichier : s604_mastermind_final.py
#Auteur : LE CORRE-PENEAU Elven
#Date de création : 06/11/2025
#Version : 1.0
#Objet : Etape 5 - Version finale simplifiée

import random

print("--- Jeu Mastermind ---")
codeSecret = random.sample(range(1, 7), 4)
print("Code secret :", codeSecret)

# ----- Lecture et validation de la proposition
proposition = []
propositionValide = False
while not propositionValide:
    proposition = []
    saisie = input("Entrez 4 chiffres entre 1 et 6 : ")

    # Vérifie que la saisie contient exactement 4 caractères
    if len(saisie) != 4:
        print("Erreur : il faut saisir exactement 4 chiffres.")
        continue

    # Vérifie que tous les caractères sont des chiffres
    if not saisie.isdigit():
        print("Erreur : saisie non numérique.")
        continue

    # Conversion en liste d'entiers
    for chiffre in saisie:
        proposition.append(int(chiffre))

    # Vérifie que tous les chiffres sont compris entre 1 et 6
    chiffres_valides = True
    for chiffre in proposition:
        if chiffre < 1 or chiffre > 6:
            print("Erreur : chiffres entre 1 et 6 uniquement.")
            chiffres_valides = False
            break  # Sort de la boucle for

    if not chiffres_valides:
        continue  # Retourne au début de la boucle while

    # Vérifie qu’il n’y a pas de doublon
    if len(set(proposition)) != 4:
        print("Erreur : pas de doublon autorisé.")
        continue

    # Si toutes les conditions sont remplies, la saisie est valide
    propositionValide = True

print("Proposition acceptée :", proposition)
print("Fin de l'étape 2 : saisie correcte.")


#Etape 3
#On créer les variables qui serviront de compteurs pour les chiffres bien placés et mal placés.
bien_place = 0
mal_place = 0
for i in range(min(len(codeSecret), len(proposition))):
    if codeSecret[i] == proposition[i]:
        bien_place += 1
    else:
        mal_place += 1
print("Il y a", bien_place, "chiffres qui sont bien placés et ", mal_place, "chiffres qui sont mal placés.")

#Etape 4
#On créer une variable compteur pour compter le nombre de tentatives
compteur = 1
#On fait une boucle tant que, si le compteur n'est pas égal à 10 ou que le code saisi n'est pas le même que le code généré cela continu.
while codeSecret!=proposition and compteur < 10:
    compteur += 1
    #On refait toute la partie de saisie et de validation du code
    proposition = []
    propositionValide = False
    while not propositionValide:
        proposition = []
        saisie = input("Entrez 4 chiffres entre 1 et 6 : ")

        # Vérifie que la saisie contient exactement 4 caractères
        if len(saisie) != 4:
            print("Erreur : il faut saisir exactement 4 chiffres.")
            continue

        # Vérifie que tous les caractères sont des chiffres
        if not saisie.isdigit():
            print("Erreur : saisie non numérique.")
            continue

        # Conversion en liste d'entiers
        for chiffre in saisie:
            proposition.append(int(chiffre))

        # Vérifie que tous les chiffres sont compris entre 1 et 6
        chiffres_valides = True
        for chiffre in proposition:
            if chiffre < 1 or chiffre > 6:
                print("Erreur : chiffres entre 1 et 6 uniquement.")
                chiffres_valides = False
                break  # Sort de la boucle for

        if not chiffres_valides:
            continue  # Retourne au début de la boucle while

        # Vérifie qu’il n’y a pas de doublon
        if len(set(proposition)) != 4:
            print("Erreur : pas de doublon autorisé.")
            continue

        # Si toutes les conditions sont remplies, la saisie est valide
        propositionValide = True
    print("Il vous reste" ,10-compteur, "essais.", "Il y a", bien_place, "chiffres qui sont bien placés et ", mal_place, "chiffres qui sont mal placés.")
    if compteur == 10:
        print("Vous avez perdu ! Le code secret était ", codeSecret)

print("Bravo ! Vous avez trouvé le code secret", codeSecret, "en", compteur, "tentatives.")