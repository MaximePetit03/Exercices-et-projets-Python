# On s'assure que le fichier existe
file = open("list.txt", "a")
file.close()

while True:
    print("\nChoisi ce que tu veux faire")
    # Ajout d'une option pour pouvoir sortir de la boucle
    choice = int(input("1 -> ajouter une tache\n2 -> supprimer une tache\n3 -> Voir les taches\n4 -> Quitter\n"))

    if choice == 3:
        file = open("list.txt", "r")
        # On lit le fichier pour connaitre les taches enregistrées
        print("\nVoici les tâches actuelles :\n" + file.read())
        file.close()

    if choice == 1:
        # On demande la tâche
        tache = input("Ajoute une tache : ")

        # On écrit la tâche dans le fichier puis on ferme le fichier pour enregistrer
        file = open("list.txt", "a")
        file.write(tache + "\n")
        file.close()
        
        file = open("list.txt", "r")
        print("\nVoici les tâches actuelles :\n" + file.read())
        file.close()

    if choice == 2:
        file = open("list.txt", "r")
        lines = file.readlines()
        file.close()

        print("\nVoici les tâches actuelles :")
        # 'enumerate' permet de parcourir la liste 'lines' en récupérant deux choses à la fois
        #'i' : l'index, que l'on fait commencer à 1 au lieu de 0
        for i, ligne in enumerate(lines, 1):
            # Affiche le numéro suivi de la tâche (strip retire le saut de ligne invisible)
            print(f"{i}. {ligne.strip()}")
            
        num = int(input("\nDonne le numéro de la tâche à supprimer : "))

        # Vérifie que le numéro entré existe bien dans la liste
        if 1 <= num <= len(lines):
            # Supprime l'élément,on fait -1 car Python compte à partir de 0
            lines.pop(num - 1)
            # Ouvre le fichier en mode écrasement ('w') pour mettre à jour la liste
            file = open("list.txt", "w")
            # Réécrit toutes les lignes restantes dans le fichier
            file.writelines(lines)
            # Ferme le fichier pour enregistrer les modifications
            file.close()

    if choice == 4:
        break