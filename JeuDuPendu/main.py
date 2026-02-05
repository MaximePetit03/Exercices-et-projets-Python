import random

# Liste de mots à deviner
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

pendu = list(mot_choisi) # Récupère le mot aléatoire
essais_restant = 10 # Nombres d'essais pour gagner

mot_trouve = False
lettres_trouvees = [] # Les lettres trouvées dans le mot
lettres_dites = [] # Toutes les lettres déjà dites

print("Tu dois trouver le mot en moins de 10 essais lettre par lettre")

# Tant que le mot n'est pas trouvé ou que le nombre d'essai ne tombe pas à 0
while essais_restant > 0 and mot_trouve == False:

    # On initialise une chaîne vide pour construire l'affichage visuel (ex: "h _ _ lo")
    affichage = ""
    
    # On parcourt chaque lettre du mot à deviner une par une
    for lettre in pendu:
        # Si la lettre du mot a déjà été devinée par le joueur
        if lettre in lettres_trouvees:
            affichage += lettre + " " # On affiche la lettre suivie d'un espace
        else:
            affichage += "_ " # Sinon, on affiche un tiret et un espace
            
    # On affiche le résultat avec les lettres que le joueur a trouvé
    print(f"\nMot : {affichage}")

    # On récupère la lettre, et .lower() force les minuscules pour éviter les erreurs
    guess = input("Donne une lettre : ").lower()

    while len(guess) != 1 or not guess.isalpha():
        print("Erreur : Tu dois entrer une seule lettre (pas de chiffres ni de mots).")
        guess = input("Donne une lettre : ").lower()

    # La lettre a déjà été trouvée précédemment
    if guess in lettres_dites:
        print(f"Tu as déjà proposé la lettre '{guess}'. Essaie une autre.")
        continue # On remonte au début du 'while' sans exécuter la suite

    # On enregistre la lettre dans l'historique des tentatives
    lettres_dites.append(guess)

    # La lettre est correcte et n'avait pas encore été trouvée
    if guess in pendu:
        print(f"{guess} est dans le mot ")
        lettres_trouvees.append(guess) # On l'ajoute aux bonnes réponses
    
    # La lettre n'est pas du tout dans le mot
    else:
        essais_restant -= 1 # On retire un essai
        print(f"Faux ! Il te reste {essais_restant} tentatives")
    
    # On part du principe que le joueur a gagné
    gagne = True 
    
    # On vérifie chaque lettre du mot à deviner
    for lettres in pendu:
        # Si une seule lettre du mot n'est pas dans 'lettres_trouvees'
        if lettres not in lettres_trouvees:
            gagne = False # Alors il n'a pas encore gagné
    
    if gagne:
        mot_trouve = True

if mot_trouve:
    print("Félicitations, tu as gagné !")
else:
    print(f"Perdu, le mot était {''.join(pendu)}")
