import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Configuration du thème
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Index de la tache séléctionné pour pouvoir la modifier
index_a_modfier = None

# Fonctions

def ajouter_tache(event=None):
    tache = entree.get()
    if tache != "":
        # On utilise le nouveau nom ici
        liste_graphique.insert(ctk.END, tache)
        
        file = open("list.txt", "a")
        file.write(tache + "\n")
        file.close()
        
        entree.delete(0, ctk.END)

def supprimer_tache(event=None):
    selection = liste_graphique.curselection()

    if selection:
        message = f"Supprimer {len(selection)} tâche(s) ?"
        reponse = messagebox.askyesno("Confirmation", message)
        if reponse == True:
            # On supprime les éléments de l'interface
            for index in reversed(selection):
                liste_graphique.delete(index)

            # On récupère toutes les tâches restantes dans l'interface
            toutes_les_taches = liste_graphique.get(0, ctk.END)

            # Ecrase le fichier avec ces tâches mises à jour
            file = open("list.txt", "w")
            for t in toutes_les_taches:
                file.write(t + "\n")
            file.close()

def modifier_tache(event):
    global index_a_modfier
    selection = liste_graphique.curselection()
    if selection:
        index_a_modfier = selection[0]
        texte_actuel = liste_graphique.get(index_a_modfier)
        
        entree.delete(0, ctk.END)
        entree.insert(0, texte_actuel)
        entree.focus()

def confirm_modif(event=None):
    global index_a_modfier
    # On vérifie qu'une modification est bien en cours
    if index_a_modfier is not None:
        nouvelle_tache = entree.get()
        
        if nouvelle_tache != "":
            # On remplace dans l'interface
            liste_graphique.delete(index_a_modfier)
            liste_graphique.insert(index_a_modfier, nouvelle_tache)
            
            # On met à jour le fichier
            toutes_les_taches = liste_graphique.get(0, ctk.END)
            file = open("list.txt", "w")
            for t in toutes_les_taches:
                file.write(t + "\n")
            file.close()
            
            entree.delete(0, ctk.END)
            index_a_modfier = None

def tout_selectionner(event=None):
    liste_graphique.selection_set(0, tk.END)
    return "break"

def gestion_entree(event):
    global index_a_modfier
    # Si un index est stocké, on modifie, sinon on ajoute
    if index_a_modfier is not None:
        confirm_modif(event)
    else:
        ajouter_tache(event)

# L'interface
root = ctk.CTk()
root.title("ToDoList")
root.geometry("700x600")

# Titre de la toDoList
label_titre = ctk.CTkLabel(root, text="MES TÂCHES", font=("Impact", 30))
label_titre.pack(pady=30)

# Zone de saisie
entree = ctk.CTkEntry(
    root, 
    placeholder_text="Quelles objectifs à faire avez vous aujourd'hui ?", 
    width=400, 
    height=50, 
    border_width=2,
    corner_radius=15
)
entree.pack(pady=10, padx=20)
entree.bind('<Return>', gestion_entree)

# Conteneur pour les boutons
frame_actions = ctk.CTkFrame(root, fg_color="transparent")
frame_actions.pack(pady=10)

btn_add = ctk.CTkButton(
    frame_actions, 
    text="AJOUTER", 
    command=ajouter_tache,
    width=120,
    height=40,
    corner_radius=20,
    fg_color="#1f6aa5",
    hover_color="#144870",
    font=("Segoe UI", 12, "bold")
)
btn_add.pack(side="left", padx=10)

btn_suppr = ctk.CTkButton(
    frame_actions, 
    text="SUPPRIMER", 
    command=supprimer_tache,
    width=120,
    height=40,
    corner_radius=20,
    fg_color="#d35b58",
    hover_color="#a54442",
    font=("Segoe UI", 12, "bold")
)
btn_suppr.pack(side="left", padx=10)

# Zone de la liste avec fond arrondi
list_frame = ctk.CTkFrame(root, corner_radius=15)
list_frame.pack(pady=20, padx=30, fill="both", expand=True)

liste_graphique = tk.Listbox(
    list_frame,
    selectmode=tk.EXTENDED,
    font=("Segoe UI", 12),
    bg="#2b2b2b",
    fg="#ecf0f1",
    selectbackground="#1f6aa5",
    selectforeground="white",
    borderwidth=0,
    highlightthickness=0,
    activestyle="none"
)
liste_graphique.pack(pady=15, padx=15, fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(liste_graphique)
scrollbar.pack(side="right", fill="y")
liste_graphique.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=liste_graphique.yview)

# sauvegarde auto
label_sauvegarde = ctk.CTkLabel(
    root, 
    text="Sauvegarde automatique activée", 
    font=("Segoe UI", 15),
    text_color="#2ecc71"
)
label_sauvegarde.pack(side="bottom", pady=5)

# Bindings
liste_graphique.bind('<Control-a>', tout_selectionner)
liste_graphique.bind('<Double-1>', modifier_tache)
liste_graphique.bind('<Delete>', supprimer_tache)
liste_graphique.bind('<BackSpace>', supprimer_tache)

# Chargement de la page
try:
    file = open("list.txt", "r")
    for ligne in file:
        liste_graphique.insert(tk.END, ligne.strip())
    file.close()
except FileNotFoundError:
    pass

root.mainloop()