# On lit le fichier pour connaitre les taches enregistrées
file = open("list.txt", "a")

print("Choisi ce que tu veux faire \n")
choice = int(input("1 -> ajouter une tache\n 2 -> supprimer une tache"))

if choice == 1:
    # On demande la tâche
    tache = input("Ajoute une tache : ")

    # On écrit la tâche dans le fichier puis on ferme le fichier pour enregistrer
    file.write(tache + "\n")
    file.close()

if choice == 2:
    file = open("list.txt", "r")
    lines = file.readline()
    file.close()

    print("\nVoici les tâches actuelles :")

# On affiche le fichier avec la tache ajouté
# print(file.read())
# file.close()

