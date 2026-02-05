import random

liste_de_mots = [
    "lion", "tigre", "elephant", "girafe", "zebre", "chien", "chat", "lapin", 
    "oiseau", "poisson", "serpent", "tortue", "grenouille", "loup", "ours", 
    "renard", "singe", "cheval", "vache", "cochon", "abeille", "requin", 
    "dauphin", "baleine", "fourmi", "canard", "mouton", "chevre", "souris", 
    "poule", "aigle", "hibou", "crabe", "crevette",

    "manger", "boire", "dormir", "courir", "marcher", "sauter", "lire", "ecrire", 
    "parler", "ecouter", "regarder", "jouer", "travailler", "chanter", "danser", 
    "penser", "aimer", "donner", "prendre", "aller", "venir", "vouloir", "pouvoir", 
    "chercher", "trouver", "gagner", "perdre", "reussir", "apprendre", "coder", 
    "aider", "partager", "ouvrir",

    "table", "chaise", "ordinateur", "livre", "stylo", "cahier", "maison", 
    "voiture", "arbre", "fleur", "soleil", "lune", "ciel", "eau", "feu", 
    "terre", "vent", "montagne", "riviere", "foret", "fenetre", "porte", 
    "clavier", "ecran", "souris", "bureau", "lampe", "tasse", "cafe", 
    "pomme", "ecole", "jardin", "bateau"
]
mot_choisi = random.choice(liste_de_mots)

pendu = list(mot_choisi)

essais_restant = 10
mot_trouve = False
lettres_trouvees = []
lettres_dites = []

print("Tu dois trouver le mot en moins de 10 essais lettre par lettre")

while essais_restant > 0 and mot_trouve == False:

    affichage = ""
    for lettre in pendu:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    print(f"\nMot : {affichage}")

    guess = input("Donne une lettre : ").lower()


    # Ajoute la lettre au
    lettres_dites.append(guess)
    if guess in lettres_trouvees:
        print(f"Tu as déjà proposé la lettre '{guess}'. Essaie une autre.")
        continue
    elif guess in pendu:
        print(f"{guess} est dans le mot ")
        lettres_trouvees.append(guess)
    # Vérifier si la lettre a déjà été proposée
    else:
        essais_restant -= 1
        print(f"Faux ! Il te reste {essais_restant} tentatives")
    
    gagne = True
    for lettres in pendu:
        if lettres not in lettres_trouvees:
            gagne = False
    
    if gagne:
        mot_trouve = True

if mot_trouve:
    print("Félicitations, tu as gagné !")
else:
    print(f"Perdu, le mot était {''.join(pendu)}")
