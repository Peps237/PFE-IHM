import tkinter as tk
from tkinter import messagebox

class IHMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ABI_HMI ZONE DE CERCLAGE SCIE 3")
        self.root.configure(bg="#FFFFFF")  # fond blanc

        # Titre principal
        self.title_label = tk.Label(self.root, text="ABI_HMI POUR LE CERCLAGE DE LA SCIE 3", font=("Arial", 24), bg="#FFFFFF", fg="#000000")
        self.title_label.pack(pady=20)

        # Menu principal pour navigation entre pages
        self.menu_frame = tk.Frame(self.root, bg="#FFFFFF", highlightbackground="#000000", highlightthickness=2)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        self.pages = {
            "Pince pour l'empilage": self.pince,
            "Empilage des billettes": self.Empilage,
            "Cerclage des Billettes": self.Cerclage,
            "Données de la zone de cerclage": self.Donnees_cerclage,
        }

        for i, (name, _) in enumerate(self.pages.items()):
            btn = tk.Button(
                self.menu_frame,
                text=name,
                command=lambda n=name: self.show_page(n),
                bg="#FFFFFF",
                fg="#000000",
                highlightbackground="#000000",
                highlightthickness=2,
                anchor="w",
                padx=10,
                borderwidth=2,
                relief="ridge"
            )
            btn.pack(fill=tk.X, pady=5)

        self.page_frame = tk.Frame(self.root, bg="#FFFFFF", highlightbackground="#000000", highlightthickness=2)
        self.page_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.current_page = None
        self.show_page("Pince pour l'empilage")

    def clear_page(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()

    def show_page(self, page_name):
        self.clear_page()
        if page_name in self.pages:
            self.pages[page_name]()
            self.title_label.config(text=page_name.upper())

            # changer la couleur du bouton de la page sélectionnée
            for widget in self.menu_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text") == page_name:
                    widget.config(bg="#000000", fg="#FFFFFF")
                else:
                    widget.config(bg="#FFFFFF", fg="#000000")

    def pince(self):
        tk.Label(self.page_frame, text="C'est ABI qui se chargera de la conception de l'IHM et du controle de la pince.",
                 wraplength=600, bg="#FFFFFF", fg="#000000", font=("Arial", 14)).pack(pady=20)

    def Empilage(self):
        # Création d'un frame principal
        frame = tk.Frame(self.page_frame, bg="#FFFFFF")
        frame.pack(fill="both", expand=True)

        # Main frame contenant les quatre sous-frames
        main_frame = tk.Frame(frame, bg="#F0F0F0")
        main_frame.pack(fill="both", expand=True)

        # Sous-frames avec bordure, marges et configuration
        frame1 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        frame2 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        frame3 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame3.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        frame4 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame4.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Configuration des lignes et colonnes pour s'adapter à l'espace disponible
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Sélection de la méthode dans le premier carré
        method_frame = tk.Frame(frame1, bg="#FFFFFF", borderwidth=1, relief="solid", highlightbackground="#000000")
        method_frame.pack(side="top", fill="x", pady=10)

        # Titre de la section
        tk.Label(method_frame, text="Sélectionnez une méthode pour définir l'écartement des bras:",
                 bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold")).pack(pady=5)

        # Variable pour la méthode
        method_var = tk.StringVar()
        method_var.set("saisie")

        # Fonction pour mettre à jour le style des radiobuttons en fonction de la sélection
        def update_radiobutton_style(selected_value):
            # Mettre à jour les styles des boutons radio selon la sélection
            for rb, value in radiobuttons.items():
                if value == selected_value:
                    rb.config(bg="#000000", fg="#FFFFFF", selectcolor="#000000")  # Style pour le bouton sélectionné
                else:
                    rb.config(bg="#FFFFFF", fg="#000000",
                              selectcolor="#FFFFFF")  # Style pour les boutons non sélectionnés

        # Dictionnaire pour stocker les radiobuttons et leurs valeurs
        radiobuttons = {}

        # Radiobutton pour la première option
        rb1 = tk.Radiobutton(method_frame, text="Saisir les données sur les billettes", variable=method_var,
                             value="saisie",
                             bg="#FFFFFF", fg="#000000", font=("Arial", 11), selectcolor="#D3D3D3",
                             activebackground="#F0F0F0", activeforeground="#000000",
                             indicatoron=0, relief="flat", padx=10, pady=5,
                             command=lambda: update_radiobutton_style("saisie"))
        rb1.pack(fill="x", pady=5)
        radiobuttons[rb1] = "saisie"

        # Radiobutton pour la deuxième option
        rb2 = tk.Radiobutton(method_frame, text="Utiliser une lettre prédéfinie", variable=method_var, value="lettre",
                             bg="#FFFFFF", fg="#000000", font=("Arial", 11), selectcolor="#D3D3D3",
                             activebackground="#F0F0F0", activeforeground="#000000",
                             indicatoron=0, relief="flat", padx=10, pady=5,
                             command=lambda: update_radiobutton_style("lettre"))
        rb2.pack(fill="x", pady=5)
        radiobuttons[rb2] = "lettre"

        # Bouton de validation de la méthode
        tk.Button(method_frame, text="Valider la méthode",
                  command=lambda: self.show_method(method_var.get(), frame1),
                  bg="#4CAF50", fg="#FFFFFF", font=("Arial", 11, "bold"),
                  relief="raised", borderwidth=1, highlightbackground="#000000",
                  highlightthickness=1).pack(pady=10)

        # Frame pour afficher les éléments de la méthode sélectionnée
        self.method_content_frame = tk.Frame(frame1, bg="#FFFFFF")
        self.method_content_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Positionnement des bras dans le deuxième carré
        tk.Label(frame2, text="\nPositionnement des bras pour chaque chariot:", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 14, 'bold')).pack(pady=15)
        tk.Label(frame2, text="Entrez les positions des 8 bras (en mm ou en lettres) (le premier étant celui le plus "
                              "au Nord) :", bg="#FFFFFF", fg="#000000", font=("Arial", 12)).pack()

        # Liste des positions actuelles des bras (par exemple, N/A si c'est la première fois)
        positions_actuelles = ["N/A"] * 8  # Utilisez "N/A" pour la première fois

        # Cadre pour afficher les deux tableaux côte à côte
        positions_frame = tk.Frame(frame2, bg="#FFFFFF")
        positions_frame.pack(pady=20)

        # Titres des tableaux avec un style amélioré
        tk.Label(positions_frame, text="Positions actuelles des bras :", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12, 'bold')).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(positions_frame, text="Positions à attribuer aux bras :", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12, 'bold')).grid(row=0, column=1, padx=10, pady=10)

        # Tableau des positions actuelles des bras
        for i, position in enumerate(positions_actuelles):
            tk.Label(positions_frame, text=f"Bras {i + 1}: {position}", fg="#A9A9A9", font=("Arial", 10), borderwidth=2,
                     relief="solid", padx=10, pady=5).grid(row=i + 1, column=0, padx=10, pady=5)

        # Tableau des positions à attribuer aux bras
        positions = []
        default_values = [f"Bras {i + 1}" for i in range(8)]  # "Bras 1", "Bras 2", ..., "Bras 8"
        for i in range(8):
            position = tk.Entry(positions_frame, width=20, font=("Arial", 10), fg="#A9A9A9", borderwidth=2,
                                relief="solid", justify="center")  # Gris clair pour le texte
            position.insert(0, default_values[i])  # Insérer le texte par défaut
            position.bind("<FocusIn>",
                          lambda event, pos=position, i=i: clear_default_value(event, pos, i))  # Effacer si focus
            position.bind("<FocusOut>", lambda event, pos=position, i=i: restore_default_value(event, pos,
                                                                                               i))
            position.grid(row=i + 1, column=1, padx=10, pady=5)
            positions.append(position)

        # Fonction pour effacer le texte par défaut quand l'utilisateur clique sur le champ
        def clear_default_value(event, position, index):
            if position.get() == f"Bras {index + 1}":  # Si le texte par défaut est encore là
                position.delete(0, tk.END)  # Effacer le texte par défaut
                position.config(fg="#000000")  # Changer la couleur du texte pour noir (normal)

        # Fonction pour restaurer la valeur par défaut si l'utilisateur quitte la case sans entrer de valeur
        def restore_default_value(event, position, index):
            if position.get() == "":  # Si la case est vide
                position.insert(0, f"Bras {index + 1}")  # Restaurer le texte par défaut
                position.config(fg="#A9A9A9")  # Rendre le texte gris pour indiquer la valeur par défaut

        # Cadre pour regrouper les boutons et les centrer
        button_frame = tk.Frame(frame2, bg="#FFFFFF")
        button_frame.pack(pady=15)

        # Bouton de validation
        validate_button = tk.Button(
            button_frame, text="Valider", command=lambda: self.valider_positions(positions),
            bg="#4CAF50", fg="#FFFFFF", highlightbackground="#000000", highlightthickness=2,
            borderwidth=2, relief="ridge", font=("Arial", 12, 'bold')
        )
        validate_button.pack(side=tk.LEFT, padx=20)

        # Fonction pour réinitialiser les champs avec les valeurs par défaut
        def reset_fields():
            for i, position in enumerate(positions):
                position.delete(0, tk.END)  # Effacer le texte actuel
                position.insert(0, default_values[i])  # Remettre le texte par défaut
                position.config(fg="#A9A9A9")  # Rendre le texte gris par défaut

        # Bouton de réinitialisation
        reset_button = tk.Button(
            button_frame, text="Réinitialiser", command=reset_fields,
            bg="#FF5733", fg="#FFFFFF", highlightbackground="#000000", highlightthickness=2,
            borderwidth=2, relief="ridge", font=("Arial", 12, 'bold')
        )
        reset_button.pack(side=tk.LEFT, padx=20)

        # Titre de la section
        tk.Label(frame3, text="\nConfiguration de la position du chariot:", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 14, "bold")).pack(pady=10)

        # Cadre pour l'entrée de position
        chariot_frame = tk.Frame(frame3, bg="#FFFFFF")
        chariot_frame.pack(fill="x", padx=10, pady=10)

        # Ligne pour les positions actuelle et désirée
        positions_frame = tk.Frame(chariot_frame, bg="#FFFFFF")
        positions_frame.pack(fill="x", pady=10)

        # Position actuelle (grise et non modifiable)
        tk.Label(positions_frame, text="Position actuelle :", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky="e")
        position_actuelle_label = tk.Entry(positions_frame, font=("Arial", 12), relief="solid", bd=1, state="disabled",
                                           disabledforeground="#808080")
        position_actuelle_label.insert(0, "N/A")  # Par défaut, "N/A"
        position_actuelle_label.grid(row=0, column=1, padx=5, sticky="w")

        # Position désirée (avec texte par défaut)
        tk.Label(positions_frame, text="Position désirée :", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12)).grid(row=0, column=2, padx=5, sticky="e")
        position_desiree = tk.Entry(positions_frame, font=("Arial", 12), relief="solid", bd=1, fg="#000000")

        # Gestion du texte par défaut
        default_text = "En mm (depuis le nord)"
        position_desiree.insert(0, default_text)
        position_desiree.config(fg="#808080")  # Couleur grise pour le texte par défaut

        # Frame 4 - Informations Complémentaires
        tk.Label(frame4, text="Informations de l'empilage", font=("Arial", 14, "bold"), bg="#FFFFFF").pack(pady=10)

        # Nombre de cerclages déjà effectués
        tk.Label(frame4, text="Nombre de billettes deposées :", bg="#FFFFFF", anchor="w").pack(fill="x", padx=10)
        nombre_billettes_deposees = tk.Label(frame4, text="9/15", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#000000")
        nombre_billettes_deposees.pack(pady=5)

        # Nombre de chevrons restants
        tk.Label(frame4, text="Disposition de l'empilage :", bg="#FFFFFF", anchor="w").pack(fill="x", padx=10)
        Disposition_de_empilage = tk.Label(frame4, text="X-X-X-X", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#000000")
        Disposition_de_empilage.pack(pady=5)

        # Feuillard restant
        tk.Label(frame4, text="Type de butées a utiliser :", bg="#FFFFFF", anchor="w").pack(fill="x", padx=10)
        Type_de_butees = tk.Label(frame4, text="Longues", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#000000")
        Type_de_butees.pack(pady=5)

        # Indication de problème
        indication_probleme = tk.Label(
            frame4, text="Rien à signaler", font=("Arial", 12, "bold"),
            bg="#FFFFFF", fg="#008000"  # Texte vert
        )
        indication_probleme.pack(pady=10)

        # Bouton pour valider le réarmement
        tk.Button(
            frame4, text="Valider le réarmement", bg="#4CAF50", fg="#000000",
            command=lambda: valider_rearmement(indication_probleme)
        ).pack(pady=10)

        # Fonction pour simuler le réarmement
        def valider_rearmement(indication_probleme_label):
            # Exemple de logique pour gérer les problèmes
            probleme_detecte = False  # Changez cette variable pour simuler un problème

            if probleme_detecte:
                indication_probleme_label.config(
                    text="Problème détecté : Vérifiez les capteurs", fg="#FF0000"
                )
            else:
                indication_probleme_label.config(
                    text="Rien à signaler", fg="#008000"
                )

        def on_focus_in(event):
            if position_desiree.get() == default_text:
                position_desiree.delete(0, "end")
                position_desiree.config(fg="#000000")  # Couleur normale pour le texte saisi

        def on_focus_out(event):
            if not position_desiree.get().strip():
                position_desiree.insert(0, default_text)
                position_desiree.config(fg="#808080")  # Couleur grise pour le texte par défaut

        position_desiree.bind("<FocusIn>", on_focus_in)
        position_desiree.bind("<FocusOut>", on_focus_out)

        position_desiree.grid(row=0, column=3, padx=5, sticky="w")

        # Fonction pour mettre à jour la position actuelle
        def update_position_actuelle(value):
            if not value.strip():
                value = "N/A"  # Si aucune donnée n'est reçue, afficher "N/A"
            position_actuelle_label.config(state="normal")  # Activer temporairement pour mise à jour
            position_actuelle_label.delete(0, "end")
            position_actuelle_label.insert(0, value)
            position_actuelle_label.config(state="disabled")  # Désactiver à nouveau

        # Exemple d'utilisation de la mise à jour (peut être déclenché ailleurs dans le programme)
        update_position_actuelle("")  # Met à jour avec "N/A" si aucune donnée

        # Bouton de validation
        tk.Button(chariot_frame, text="Valider la position",
                  command=lambda: self.validate_chariot_1D(position_actuelle_label["text"], position_desiree.get()),
                  bg="#4CAF50", fg="#FFFFFF", font=("Arial", 12, "bold"), relief="raised",
                  borderwidth=1, padx=10, pady=5).pack(pady=10)

        # Bouton pour réinitialiser la position à 0
        def reset_position():
            # Réinitialiser la position désirée et actuelle
            position_desiree.delete(0, "end")
            position_desiree.insert(0, "0")  # Réinitialise la position désirée à 0
            position_desiree.config(fg="#000000")  # Rendre le texte normal
            update_position_actuelle("N/A")  # Réinitialiser la position actuelle à "N/A"

        # Ajouter le bouton de réinitialisation
        tk.Button(chariot_frame, text="Réinitialiser la position",
                  command=reset_position, bg="#FF6347", fg="#FFFFFF", font=("Arial", 12, "bold"), relief="raised",
                  borderwidth=1, padx=10, pady=5).pack(pady=10)

    def validate_chariot_1D(self, position_actuelle, position_desiree):
        # Valider que la position actuelle et désirée sont correctes
        if position_actuelle == "N/A" or position_desiree == "En mm (depuis le nord)":
            tk.messagebox.showerror("Erreur", "Veuillez entrer des positions valides")
            return

        try:
            # Convertir les entrées en valeurs numériques (si applicable)
            position_desiree_val = int(position_desiree)

            # Validation d'une position raisonnable, vous pouvez ajouter d'autres critères
            if position_desiree_val < 0 or position_desiree_val > 10000:
                raise ValueError("La position désirée doit être un nombre entre 0 et 10000")

            # Si tout est validé, afficher un message de succès
            tk.messagebox.showinfo("Succès", f"Position du chariot validée:\n"
                                             f"Position actuelle: {position_actuelle}\n"
                                             f"Position désirée: {position_desiree_val} mm")
        except ValueError as e:
            tk.messagebox.showerror("Erreur", f"Erreur dans la position désirée : {str(e)}")

    # Fonction pour valider les positions
    def valider_positions(self, positions):
        # Vérification si toutes les cases sont remplies
        if any(position.get() == "" for position in positions):
            tk.messagebox.showerror("Erreur", "Veuillez remplir toutes les cases")
            return

        # Correspondance lettres -> valeurs croissantes
        valeurs_possibles = [
            12, 25, 37, 48, 59, 64, 78, 85, 92, 101,
            115, 128, 135, 147, 159, 170, 182, 195, 208, 221,
            234, 250, 265, 278, 290, 305
        ]
        correspondance = {chr(65 + i): valeurs_possibles[i] for i in range(26)}  # A-Z

        # Récupération des valeurs entrées par l'utilisateur
        valeurs = [position.get() for position in positions]

        try:
            valeurs_converties = []
            for valeur in valeurs:
                # Vérification si c'est un entier
                if valeur.isdigit():
                    valeurs_converties.append(int(valeur))
                # Vérification si c'est une seule lettre
                elif len(valeur) == 1 and valeur.upper() in correspondance:
                    valeurs_converties.append(correspondance[valeur.upper()])
                else:
                    raise ValueError(f"Valeur non valide : {valeur}")

            # Vérification si les valeurs sont dans l'ordre croissant
            if valeurs_converties != sorted(valeurs_converties):
                tk.messagebox.showerror("Erreur", "Les positions des bras doivent être dans l'ordre croissant")
                return

            # Vérification de la distance minimale et maximale entre les bras
            for i in range(len(valeurs_converties) - 1):
                if i < 3:
                    if valeurs_converties[i + 1] - valeurs_converties[i] > 130 or valeurs_converties[i + 1] - \
                            valeurs_converties[i] < 400:
                        tk.messagebox.showerror(
                            "Erreur",
                            f"La distance entre les bras {i + 1} et {i + 2} est incorrecte"
                        )
                        return
                if i >= 4:
                    if valeurs_converties[i + 1] - valeurs_converties[i] > 130 or valeurs_converties[i + 1] - \
                            valeurs_converties[i] < 400:
                        tk.messagebox.showerror(
                            "Erreur",
                            f"La distance entre les bras {i + 1} et {i + 2} est incorrecte"
                        )
                        return

            # Les positions des bras sont valides
            tk.messagebox.showinfo("Succès", "Les positions des bras sont valides")

        except ValueError as e:
            tk.messagebox.showerror("Erreur", str(e))

    def show_method(self, method, frame):
        # Suppression du contenu précédent
        for widget in self.method_content_frame.winfo_children():
            widget.destroy()

        # Affichage de la méthode sélectionnée
        if method == "saisie":
            self.show_saisie(self.method_content_frame)
        elif method == "lettre":
            self.show_lettre(self.method_content_frame)

    def show_saisie(self, frame):
        # Titre de la section
        tk.Label(frame, text="\nConfiguration de l'écartement des bras:", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(frame, text="Entrée des spécifications:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).pack(pady=5)

        # Frame pour les champs
        input_frame = tk.Frame(frame, bg="#FFFFFF")
        input_frame.pack(pady=10, padx=10, fill="x")

        # Diamètre des billettes
        tk.Label(input_frame, text="Diamètre des billettes (mm):", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(
            row=1, column=0, sticky="w", pady=5)
        billet_diameter = tk.Entry(input_frame, font=("Arial", 10), relief="flat", highlightthickness=1,
                                   highlightbackground="#CCCCCC", width=20)
        billet_diameter.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Nombre de billettes
        tk.Label(input_frame, text="Nombre de billettes:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=2,
                                                                                                                column=0,
                                                                                                                sticky="w",
                                                                                                                pady=5)
        billet_count = tk.Entry(input_frame, font=("Arial", 10), relief="flat", highlightthickness=1,
                                highlightbackground="#CCCCCC", width=20)
        billet_count.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Ajustement des colonnes
        input_frame.columnconfigure(1, weight=0)

        # Bouton de validation
        tk.Button(frame, text="Valider",
                  command=lambda: self.validate_billet_params(billet_diameter.get(),
                                                              billet_count.get(), ""),
                  bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="raised",
                  borderwidth=1, padx=10, pady=5).pack(pady=15)

        # Gestion du focus
        billet_diameter.bind("<Return>", lambda _: billet_count.focus_set())
        billet_count.bind("<Return>", lambda _: self.validate_billet_params(billet_diameter.get(),
                                                                            billet_count.get(), ""))

    def show_lettre(self, frame):
        # Titre de la section
        tk.Label(frame, text="\nEntrée de la lettre prédéfinie:", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12, "bold")).pack(pady=10)

        # Frame pour les champs
        input_frame = tk.Frame(frame, bg="#FFFFFF")
        input_frame.pack(pady=10, padx=10, fill="x")

        # Lettre prédéfinie
        tk.Label(input_frame, text="Entrez la lettre prédéfinie:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", pady=5)
        preset_letter = tk.Entry(input_frame, font=("Arial", 10), relief="flat", highlightthickness=1,
                                 highlightbackground="#CCCCCC", width=20)
        preset_letter.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Ajustement des colonnes
        input_frame.columnconfigure(1, weight=0)

        # Bouton de validation
        tk.Button(frame, text="Valider",
                  command=lambda: self.validate_billet_params("", "", "", preset_letter.get()),
                  bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="raised",
                  borderwidth=1, padx=10, pady=5).pack(pady=15)

        # Gestion du focus
        preset_letter.bind("<Return>", lambda _: self.validate_billet_params("", "", "", preset_letter.get()))

    def Cerclage(self):
        frame = tk.Frame(self.page_frame, bg="#FFFFFF")
        frame.pack(fill="both", expand=True)

        # Main frame containing four subframes
        main_frame = tk.Frame(frame, bg="#F0F0F0")
        main_frame.pack(fill="both", expand=True)

        frame1 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        frame2 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        frame3 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame3.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        frame4 = tk.Frame(main_frame, bg="#FFFFFF", borderwidth=2, relief="ridge", highlightbackground="#000000")
        frame4.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Configure grid
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Reinitialization Function
        def reset_current_data(entries):
            for entry in entries:
                entry.delete(0, tk.END)

        # Validation Function
        def validate_entries(entries, checkboxes, current_position_station, arm_center_positions):
            # Get the values from the entries
            values = [entry.get() for entry in entries]
            print("Validated Values:", values)
            validated_positions = set()  # Pour éviter les doublons
            invalid_entries = []  # Pour stocker les valeurs non valides
            errors = []  # Liste des erreurs à afficher

            for entry in entries:
                value = entry.get().strip()  # Récupérer et nettoyer l'entrée

                # Vérification que la valeur est un entier
                if not value.isdigit():
                    invalid_entries.append(value)
                    continue

                position = int(value)

                # Vérification des doublons
                if position in validated_positions:
                    errors.append(f"Position en double ignorée : {position} mm")
                    continue

                # Vérification de la position du chariot de la station
                if position < current_position_station + 250 or position > current_position_station + 2000:
                    errors.append(
                        f"Position {position} mm invalide : doit être > {current_position_station} mm (station 2)")
                    continue

                # Vérification de la proximité du bras d’empilage
                if abs(position - arm_center_positions) < 100:
                    errors.append(f"Position {position} mm trop proche du bras d’empilage (min 100 mm requis)")
                    continue

                # Ajout de la position validée
                validated_positions.add(position)

            # Affichage des erreurs s'il y en a
            if invalid_entries or errors:
                error_message = "Erreurs détectées :\n\n"
                if invalid_entries:
                    error_message += "Valeurs non valides (doivent être des entiers) : " + ", ".join(
                        invalid_entries) + "\n"
                if errors:
                    error_message += "\n".join(errors)

                messagebox.showerror("Erreur de validation", error_message)

            # Validate the checkboxes
            for i, (che_var, str_var) in enumerate(checkboxes):
                if che_var.get() == 1 and str_var.get() == 0:
                    messagebox.showwarning(
                        "Validation Error",
                        f"Erreur: La case chevron 'Che.' est cochée sans que Strapping 'Str.' ne soit également cochée à la ligne {i + 1}."
                    )
                    return  # Stop further validation if the error is found

            # Once validated, copy the "Positions desirees" checkboxes to "Positions actuelles"
            for i, (che_var, str_var) in enumerate(checkboxes):
                # Get the checkbox values from positions desirees
                desired_che = che_var.get()
                desired_str = str_var.get()

                # Update the "Positions actuelles" checkboxes
                checkboxes[i] = (desired_che, desired_str)

        # Create Interface Function
        def create_interface(parent_frame, station_title, checkboxes):
            tk.Label(parent_frame, text=station_title, font=("Arial", 14, "bold"), bg=parent_frame["bg"]).grid(
                row=0, column=0, columnspan=9, pady=5, sticky="nsew"
            )

            # Configuration pour centrer le contenu de la grille
            parent_frame.grid_columnconfigure(0, weight=1)
            parent_frame.grid_columnconfigure(8, weight=1)

            # Labels for columns
            tk.Label(parent_frame, text="Positions actuelles", font=("Arial", 10), bg=parent_frame["bg"]).grid(row=1,
                                                                                                               column=2,
                                                                                                               padx=5)

            tk.Label(parent_frame, text="Che.", font=("Arial", 10), bg=parent_frame["bg"]).grid(row=1, column=3, padx=5)
            tk.Label(parent_frame, text="Str.", font=("Arial", 10), bg=parent_frame["bg"]).grid(row=1, column=4, padx=5)

            tk.Label(parent_frame, text="Positions desirees", font=("Arial", 10), bg=parent_frame["bg"]).grid(row=1,
                                                                                                              column=5,
                                                                                                              padx=5)

            # Labels for "Che." and "Str." for both sections
            tk.Label(parent_frame, text="Che.", font=("Arial", 10), bg=parent_frame["bg"]).grid(row=1, column=6, padx=5)
            tk.Label(parent_frame, text="Str.", font=("Arial", 10), bg=parent_frame["bg"]).grid(row=1, column=7, padx=5)

            # Dynamic data population
            entries = []  # Store current data entry widgets
            for i in range(8):  # Example: 8 rows
                tk.Label(parent_frame, text=f"{i + 1}.", bg=parent_frame["bg"]).grid(row=i + 2, column=1, padx=5)

                # Static "Positions actuelles" (grayed out and non-editable)
                system_data = tk.Label(parent_frame, text="N/A", bg="#A9A9A9", borderwidth=1, relief="solid", width=12)
                system_data.grid(row=i + 2, column=2, padx=5)

                # Checkboxes for "Positions actuelles" (Che. & Str.) - non-editable, grayed out
                che_var = tk.IntVar()
                str_var = tk.IntVar()
                checkboxes.append((che_var, str_var))
                # Grayed "Che." and "Str." for positions actuelles

                che_checkbox = tk.Checkbutton(parent_frame, variable=che_var, bg="#A9A9A9", state="disabled")
                che_checkbox.grid(row=i + 2, column=3, padx=5)
                str_checkbox = tk.Checkbutton(parent_frame, variable=str_var, bg="#A9A9A9", state="disabled")
                str_checkbox.grid(row=i + 2, column=4, padx=5)

                # Editable "Positions desirees"
                current_data = tk.Entry(parent_frame, width=12)
                current_data.grid(row=i + 2, column=5, padx=5)
                entries.append(current_data)

                # Checkboxes for "Positions desirees" (Che. & Str.)
                che_checkbox_2 = tk.Checkbutton(parent_frame, variable=che_var, bg=parent_frame["bg"])
                che_checkbox_2.grid(row=i + 2, column=6, padx=5)
                str_checkbox_2 = tk.Checkbutton(parent_frame, variable=str_var, bg=parent_frame["bg"])
                str_checkbox_2.grid(row=i + 2, column=7, padx=5)

            # Buttons
            tk.Button(parent_frame, text="Reinitialiser", command=lambda: reset_current_data(entries),
                      bg="#FF5733").grid(row=11, column=5, pady=10)

            current_position_station = 2500

            # Les positions des bras
            arm_positon = 2750

            tk.Button(parent_frame, text="Valider", command=lambda: validate_entries(entries, checkboxes, current_position_station, arm_positon),
                      bg="#4CAF50").grid(row=11, column=3, pady=12)

        checkboxes1 = []  # Store the checkbox pairs (che_var1, str_var1)
        checkboxes2 = []  # Store the checkbox pairs (che_var2, str_var2)

        # Create interfaces for Station 1 and Station 2
        create_interface(frame1, "Station 1 (Chariot Nord)", checkboxes1)
        create_interface(frame2, "Station 2 (Chariot Sud)",checkboxes2)

        # Fonction pour restaurer la valeur par défaut si l'utilisateur quitte la case sans entrer de valeur
        def restore_default_value(event, position, index):
            if position.get() == "":  # Si la case est vide
                position.insert(0, f"Bras {index + 1}")  # Restaurer le texte par défaut
                position.config(fg="#A9A9A9")  # Rendre le texte gris pour indiquer la valeur par défaut

        # Titre de la section
        tk.Label(frame3, text="\nConfiguration de la position du chariot:", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 14, "bold")).pack(pady=10)

        # Cadre pour l'entrée de position
        chariot_frame = tk.Frame(frame3, bg="#FFFFFF")
        chariot_frame.pack(fill="x", padx=10, pady=10)

        # Ligne pour les positions actuelle et désirée
        positions_frame = tk.Frame(chariot_frame, bg="#FFFFFF")
        positions_frame.pack(fill="x", pady=10)

        # Position actuelle (grise et non modifiable)
        tk.Label(positions_frame, text="Position actuelle :", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky="e")
        position_actuelle_label = tk.Entry(positions_frame, font=("Arial", 12), relief="solid", bd=1, state="disabled",
                                           disabledforeground="#808080")
        position_actuelle_label.insert(0, "N/A")  # Par défaut, "N/A"
        position_actuelle_label.grid(row=0, column=1, padx=5, sticky="w")

        # Position désirée (avec texte par défaut)
        tk.Label(positions_frame, text="Position désirée :", bg="#FFFFFF", fg="#000000",
                 font=("Arial", 12)).grid(row=0, column=2, padx=5, sticky="e")
        position_desiree = tk.Entry(positions_frame, font=("Arial", 12), relief="solid", bd=1, fg="#808080")

        # Texte par défaut
        default_text = "En mm (depuis le nord)"
        position_desiree.insert(0, default_text)
        position_desiree.config(fg="#808080")  # Couleur grise pour le texte par défaut

        # Gestion du texte par défaut
        def on_focus_in(event):
            if position_desiree.get() == default_text:
                position_desiree.delete(0, "end")
                position_desiree.config(fg="#000000")  # Couleur normale pour le texte saisi

        def on_focus_out(event):
            if not position_desiree.get().strip():
                position_desiree.insert(0, default_text)
                position_desiree.config(fg="#808080")  # Couleur grise pour le texte par défaut

        position_desiree.bind("<FocusIn>", on_focus_in)
        position_desiree.bind("<FocusOut>", on_focus_out)

        position_desiree.grid(row=0, column=3, padx=5, sticky="w")

        # Fonction pour mettre à jour la position actuelle
        def update_position_actuelle(value):
            if not value.strip():
                value = "N/A"  # Si aucune donnée n'est reçue, afficher "N/A"
            position_actuelle_label.config(state="normal")  # Activer temporairement pour mise à jour
            position_actuelle_label.delete(0, "end")
            position_actuelle_label.insert(0, value)
            position_actuelle_label.config(state="disabled")  # Désactiver à nouveau

        # Exemple d'utilisation de la mise à jour (peut être déclenché ailleurs dans le programme)
        update_position_actuelle("")  # Met à jour avec "N/A" si aucune donnée

        # Fonction de validation de la position
        def validate_position():
            value = position_desiree.get()
            if value == default_text or not value.isdigit():
                messagebox.showerror("Erreur", "Veuillez entrer une position valide.")
                return
            messagebox.showinfo("Validation", f"Position validée : {value} mm.")

        # Bouton de validation
        tk.Button(chariot_frame, text="Valider la position",
                  command=validate_position, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 12, "bold"), relief="raised",
                  borderwidth=1, padx=10, pady=5).pack(pady=10)

        # Fonction pour réinitialiser la position
        def reset_position():
            # Réinitialiser la position désirée et actuelle
            position_desiree.delete(0, "end")
            position_desiree.insert(0, default_text)  # Réinitialise la position désirée au texte par défaut
            position_desiree.config(fg="#808080")  # Rendre le texte gris
            update_position_actuelle("N/A")  # Réinitialiser la position actuelle à "N/A"

        # Bouton pour réinitialiser la position
        tk.Button(chariot_frame, text="Réinitialiser la position",
                  command=reset_position, bg="#FF6347", fg="#FFFFFF", font=("Arial", 12, "bold"), relief="raised",
                  borderwidth=1, padx=10, pady=5).pack(pady=10)

        # Frame 4 - Informations Complémentaires
        tk.Label(frame4, text="Informations du cerclage", font=("Arial", 14, "bold"), bg="#FFFFFF").pack(pady=10)

        # Nombre de cerclages déjà effectués
        tk.Label(frame4, text="Nombre de cerclages déjà effectués :", bg="#FFFFFF", anchor="w").pack(fill="x", padx=10)
        cerclages_effectues = tk.Label(frame4, text="0", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#000000")
        cerclages_effectues.pack(pady=5)

        # Nombre de chevrons restants
        tk.Label(frame4, text="Nombre de chevrons restants :", bg="#FFFFFF", anchor="w").pack(fill="x", padx=10)
        chevrons_restants = tk.Label(frame4, text="0", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#000000")
        chevrons_restants.pack(pady=5)

        # Feuillard restant
        tk.Label(frame4, text="Feuillard restant :", bg="#FFFFFF", anchor="w").pack(fill="x", padx=10)
        feuillard_restant = tk.Label(frame4, text="0", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#000000")
        feuillard_restant.pack(pady=5)

        # Indication de problème
        indication_probleme = tk.Label(
            frame4, text="Rien à signaler", font=("Arial", 12, "bold"),
            bg="#FFFFFF", fg="#008000"  # Texte vert
        )
        indication_probleme.pack(pady=10)

        # Bouton pour valider le réarmement
        tk.Button(
            frame4, text="Valider le réarmement", bg="#4CAF50", fg="#000000",
            command=lambda: valider_rearmement(indication_probleme)
        ).pack(pady=10)

        # Fonction pour simuler le réarmement
        def valider_rearmement(indication_probleme_label):
            # Exemple de logique pour gérer les problèmes
            probleme_detecte = False  # Changez cette variable pour simuler un problème

            if probleme_detecte:
                indication_probleme_label.config(
                    text="Problème détecté : Vérifiez les capteurs", fg="#FF0000"
                )
            else:
                indication_probleme_label.config(
                    text="Rien à signaler", fg="#008000"
                )

    #Donnee de cerclage resume
    def Donnees_cerclage(self):
        tk.Label(self.page_frame, text="Données de la zone de cerclage", font=("Arial", 16), bg="#FFFFFF",
                 fg="#000000").pack(pady=10)

        tk.Label(self.page_frame,
                 text="C'est ABI qui se chargera de la conception de la zone de diffusion d'information.",
                 wraplength=600, bg="#FFFFFF", fg="#000000", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.page_frame, text="Informations a fournir:", bg="#FFFFFF", fg="#000000").pack()
        tk.Label(self.page_frame, text="- Paramètres actuels du cerclage (avec/sans chevrons)", bg="#FFFFFF",
                 fg="#000000").pack()
        tk.Label(self.page_frame, text="- Étapes du processus", bg="#FFFFFF", fg="#000000").pack()
        tk.Label(self.page_frame, text="- Vitesse des opérations", bg="#FFFFFF", fg="#000000").pack()
        tk.Label(self.page_frame, text="- Type de billettes", bg="#FFFFFF", fg="#000000").pack()
        tk.Label(self.page_frame, text="- Écartement des bras et positions des chariots", bg="#FFFFFF",
                 fg="#000000").pack()
        tk.Label(self.page_frame, text="- Détails des alarmes", bg="#FFFFFF", fg="#000000").pack()
        tk.Label(self.page_frame, text="- Historique des opérations", bg="#FFFFFF", fg="#000000").pack()

    def validate_billet_params(self, chevron_length, billet_diameter, billet_count, preset_letter):
        if preset_letter:
            messagebox.showinfo("Validation", f"Préréglage avec la lettre: {preset_letter} appliqué.")
        else:
            messagebox.showinfo("Validation",
                                f"Spécifications: Chevron: {chevron_length}mm, Diamètre: {billet_diameter}mm, Nombre: {billet_count}")

    def reset_positions(self):
        messagebox.showinfo("Réinitialisation", "Positions réinitialisées aux valeurs par défaut.")

    def validate_cerclage_params(self, num_cerclages, positions, speed, billet_type):
        messagebox.showinfo("Validation",
                            f"Nombre de cerclages: {num_cerclages}, Positions: {positions}, Vitesse: {speed}, Type: {billet_type}")


if __name__ == "__main__":
    root = tk.Tk()
    app = IHMApp(root)
    root.mainloop()
