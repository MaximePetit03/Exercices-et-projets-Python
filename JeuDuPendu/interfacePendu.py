import customtkinter as ctk  # Bibliothèque pour une interface moderne (boutons arrondis, mode sombre)
import tkinter as tk  # Bibliothèque de base pour les éléments spécifiques comme le Canvas
import random

# Définit le thème sombre et la couleur d'accentuation
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JeuPendu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.liste_de_mots = [
            # ANIMAUX
            "lion", "tigre", "elephant", "girafe", "zebre", "chien", "chat", "lapin", 
            "oiseau", "poisson", "serpent", "tortue", "grenouille", "loup", "ours", 
            "renard", "singe", "cheval", "vache", "cochon", "abeille", "requin", 
            "dauphin", "baleine", "fourmi", "canard", "mouton", "chevre", "souris", 
            "poule", "aigle", "hibou", "crabe", "crevette", "meduse", "scorpion",
            "araignee", "papillon", "homard", "pingouin", "panda", "koala", "hamster",

            # VERBES
            "manger", "boire", "dormir", "courir", "marcher", "sauter", "lire", "ecrire", 
            "parler", "ecouter", "regarder", "jouer", "travailler", "chanter", "danser", 
            "penser", "aimer", "donner", "prendre", "aller", "venir", "vouloir", "pouvoir", 
            "chercher", "trouver", "gagner", "perdre", "reussir", "apprendre", "coder", 
            "aider", "partager", "ouvrir", "fermer", "voyager", "construire", "detruire",
            "conduire", "cuisiner", "nettoyer", "reparer", "choisir", "attendre",

            # DIVERS
            "avion", "train", "velo", "camion", "moto", "metro", "gare", "aeroport",
            "ville", "village", "route", "chemin", "pont", "tunnel", "chateau",
            "musee", "cinema", "theatre", "hotel", "plage", "desert", "ocean", "ile",
            "table", "chaise", "ordinateur", "livre", "stylo", "cahier", "maison", 
            "voiture", "arbre", "fleur", "soleil", "lune", "ciel", "eau", "feu", 
            "terre", "vent", "montagne", "riviere", "foret", "fenetre", "porte", 
            "clavier", "ecran", "souris", "bureau", "lampe", "tasse", "cafe", 
            "pomme", "ecole", "jardin", "bateau", "miroir", "armoire", "coussin",
            "canape", "rideau", "valise", "montre", "journal", "bouteille", "assiette",
            "pain", "fromage", "chocolat", "gateau", "pizza", "pates", "riz", "soupe",
            "salade", "fruit", "legume", "orange", "banane", "fraise", "citron",
            "viande", "oeuf", "sucre", "sel", "beurre", "lait", "jus", "the"

            # SCIENCES
            "planete", "etoile", "galaxie", "comete", "astronaute", "fusee", "telescope",
            "atome", "molecule", "energie", "lumiere", "gravite", "vitesse", "temps",
            "espace", "robot", "science", "physique", "chimie", "biologie", "calcul",
        ]
        
        self.mot_choisi = random.choice(self.liste_de_mots)
        self.pendu = list(self.mot_choisi)
        self.essais_restant = 11
        self.lettres_trouvees = []
        self.lettres_dites = []

        # Paramètre de la fenêtre
        self.title("Jeu du pendu")
        self.geometry("700x600")
        self.create_interface()
    
    # Crée tous les éléments visuels de la fenêtre
    def create_interface(self):
        # CTkLabel : Affiche du texte simple
        self.label_titre = ctk.CTkLabel(self, text="LE JEU DU PENDU", font=("Impact", 35))
        self.label_titre.pack(pady=20)

        # CTkCanvas : Zone de dessin permettant de tracer des lignes et des formes
        self.canvas = ctk.CTkCanvas(self, width=200, height=230, bg="#2b2b2b", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Zone affichant le mot masqué (ex: _ _ _ _)
        self.label_mot = ctk.CTkLabel(self, text=self.affichage(), font=("Consolas", 40, "bold"))
        self.label_mot.pack(pady=20)

        # CTkEntry : Champ où l'utilisateur tape sa lettre
        self.entree = ctk.CTkEntry(self, placeholder_text="Lettre", width=120, height=45, justify="center")
        self.entree.pack(pady=10)
        
        # .bind("<Return>") : Permet de valider en appuyant sur la touche 'Entrée' du clavier
        self.entree.bind("<Return>", lambda e: self.check_letters())

        # CTkButton : Bouton cliquable pour lancer la vérification
        self.btn_valider = ctk.CTkButton(self, text="VALIDER", command=self.check_letters)
        self.btn_valider.pack(pady=10)

        # Labels d'informations secondaires
        self.label_essais = ctk.CTkLabel(self, text=f"Essais restants : {self.essais_restant}", font=("Segoe UI", 14))
        self.label_essais.pack(pady=5)

        self.label_dites = ctk.CTkLabel(self, text="Lettres essayées : ", font=("Segoe UI", 14), text_color="white")
        self.label_dites.pack(pady=5)

    # Transforme la liste de lettres trouvées en chaîne lisible (ex: h _ l _ o )
    def affichage(self):
        affichage = ""
        for lettre in self.pendu:
            if lettre in self.lettres_trouvees:
                affichage += lettre + " "
            else:
                affichage += "_ "
        return affichage

    # Dessine une partie du pendu sur le Canvas selon le nombre d'erreurs
    def draw_pendu(self):
        c = self.canvas
        couleur = "#ffffff"
        largeur = 3
        etape = 11 - self.essais_restant # Détermine quelle partie dessiner

        # Coordonnées (x1, y1, x2, y2) pour tracer chaque segment
        if etape == 1: c.create_line(20, 210, 180, 210, fill=couleur, width=largeur) # Socle
        elif etape == 2: c.create_line(50, 210, 50, 20, fill=couleur, width=largeur) # Poteau V
        elif etape == 3: c.create_line(50, 20, 150, 20, fill=couleur, width=largeur) # Poteau H
        elif etape == 4: c.create_line(50, 60, 90, 20, fill=couleur, width=largeur) # Diagonale
        elif etape == 5: c.create_line(150, 20, 150, 50, fill=couleur, width=largeur) # Corde
        elif etape == 6: c.create_oval(135, 50, 165, 80, outline=couleur, width=largeur) # Tête
        elif etape == 7: c.create_line(150, 80, 150, 140, fill=couleur, width=largeur) # Corps
        elif etape == 8: c.create_line(150, 90, 120, 120, fill=couleur, width=largeur) # Bras G
        elif etape == 9: c.create_line(150, 90, 180, 120, fill=couleur, width=largeur) # Bras D
        elif etape == 10: c.create_line(150, 140, 125, 190, fill=couleur, width=largeur) # Jambe G
        elif etape == 11: c.create_line(150, 140, 175, 190, fill=couleur, width=largeur) # Jambe D

    # Récupère la lettre et applique la logique de jeu
    def check_letters(self):
        guess = self.entree.get().lower()
        self.entree.delete(0, ctk.END) # Efface le champ de saisie après validation

        # Vérifications de base
        if len(guess) != 1 or not guess.isalpha() or guess in self.lettres_dites:
            return

        self.lettres_dites.append(guess)
        # .configure permet de mettre à jour le texte d'un label dynamiquement
        self.label_dites.configure(text=f"Lettres déjà dites : {', '.join(self.lettres_dites)}")

        if guess in self.pendu:
            self.lettres_trouvees.append(guess)
            self.label_mot.configure(text=self.affichage())
            
            # Condition de victoire
            if "_" not in self.affichage():
                # On remplace le mot masqué par le message de victoire
                self.label_mot.configure(text=f"Gagné ! Le mot était : {self.mot_choisi.upper()}", text_color="#01ff01", font=("Segoe UI", 25, "bold"))
                
                # On désactive le bouton pour empêcher de continuer
                self.btn_valider.configure(state="disabled", text="Gagné")
                
                # On attend 3 secondes avant de relancer la partie
                self.after(3000, self.reset)
        else:
            self.essais_restant -= 1
            self.draw_pendu() # On dessine une partie du pendu
            self.label_essais.configure(text=f"Essais restants : {self.essais_restant}")
            
            # Condition de défaite
            if self.essais_restant == 0:
                # On remplace le mot masqué par le message de défaite
                self.label_mot.configure(text=f"Perdu ! Le mot était : {self.mot_choisi.upper()}", text_color="#ff0000", font=("Segoe UI", 25, "bold"))
                
                # On désactive le bouton pour empêcher de continuer
                self.btn_valider.configure(state="disabled", text="PERDU")
                
                # On attend 5 secondes avant de relancer la partie
                self.after(5000, self.reset)
    
    # Réinitialise toutes les variables
    def reset(self):

        self.mot_choisi = random.choice(self.liste_de_mots)
        self.pendu = list(self.mot_choisi)
        self.essais_restant = 10
        self.lettres_trouvees = []
        self.lettres_dites = []
        self.canvas.delete("all") # Efface tout le dessin du Canvas
        self.label_mot.configure(text=self.affichage())
        self.label_mot.configure(text_color="white")
        self.label_essais.configure(text=f"Essais restants : {self.essais_restant}")
        self.label_dites.configure(text="Lettres déjà dites : ")

if __name__ == "__main__":
    app = JeuPendu()
    app.mainloop() # Lance la boucle principale de l'interface