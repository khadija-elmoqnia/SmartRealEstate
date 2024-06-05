import tkinter as tk
from tkinter import messagebox
import numpy as np
import webbrowser


def interface(prepare_data,predict_hpi):
    # Créer l'interface Tkinter
    app = tk.Tk()
    app.title("Prédiction du HPI")

    # Définir la taille de police pour les étiquettes et les champs de saisie
    font_size = 14

    # Fonction pour ouvrir les liens
    def open_link(url):
        webbrowser.open_new(url)

    # Fonction pour prédire le HPI
    def predict_and_show_hpi():
        # Préparer les données
        data = prepare_data(float(entry_mortgage_15yr.get()), float(entry_Consumer_price.get()), 
                            float(entry_Gross_Domestic_Product.get()),float(entry_personal_income.get()),
                            float(entry_population.get()), float(entry_total_construction.get()))

        # Faire des prédictions sur les données
        prediction = predict_hpi(data)

        # Afficher le résultat de la prédiction
        messagebox.showinfo("Résultat de la prédiction", f"La valeur prédite de HPI est : {prediction}")

    # Créer des champs de saisie pour les variables explicatives avec leurs liens
    def create_entry_with_link(label_text, link_url, row):
        label = tk.Label(app, text=label_text)
        label.grid(row=row, column=0, sticky="w")  # Déplacer le label à la colonne 0
        label.config(font=("Arial", font_size))

        link_label = tk.Label(app, text="Consulter ce site", fg="blue", cursor="hand2")
        link_label.grid(row=row, column=1, sticky="e")  # Déplacer le lien vers la colonne 1
        link_label.bind("<Button-1>", lambda event, url=link_url: open_link(url))
        link_label.config(font=("Arial", font_size))

        entry = tk.Entry(app)
        entry.grid(row=row, column=2, sticky="we")  # Les champs de saisie remplissent l'ensemble de la largeur disponible
        entry.bind("<Return>", lambda event=None: predict_and_show_hpi())  # Permet de déclencher la prédiction en appuyant sur "Entrée"
        entry.config(font=("Arial", font_size))

        return entry

    # Créer les champs de saisie avec les liens associés
    row_num = 0
    entry_mortgage_15yr = create_entry_with_link("Mortgage_15yr:", "https://fred.stlouisfed.org/series/MORTGAGE15US", row_num)
    row_num += 1
    entry_Consumer_price= create_entry_with_link("Consumer price index:", "https://www2.nhes.nh.gov/GraniteStats/SessionServlet?page=CPI.jsp&SID=5&country=000000&countryName=United%20States", row_num)
    row_num += 1
    entry_personal_income = create_entry_with_link("Personal income:", "https://fred.stlouisfed.org/series/PI", row_num)
    row_num += 1
    entry_population = create_entry_with_link("Population:", "https://fred.stlouisfed.org/series/POPTHM", row_num)
    row_num += 1
    entry_total_construction = create_entry_with_link("Total construction:", "https://fred.stlouisfed.org/series/TTLCONS", row_num)
    row_num += 1
    entry_Gross_Domestic_Product = create_entry_with_link("Gross Domestic Product:", "https://fred.stlouisfed.org/series/TTLCONS", row_num)

    # Bouton pour effectuer la prédiction
    predict_button = tk.Button(app, text="Prédiction",bg="#8B4513", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5, command=predict_and_show_hpi, width=40, height=2)  # Largeur et hauteur du bouton augmentées
    predict_button.grid(row=row_num + 1, column=0, columnspan=3, pady=(10,0), sticky="s", padx=10)  # Placé en bas et centré

    # Centrer le contenu de la fenêtre
    for i in range(row_num + 1):
        app.grid_rowconfigure(i, weight=1)
    for j in range(3):
        app.grid_columnconfigure(j, weight=1)

    # Ajuster la taille de la fenêtre
    app.geometry("800x750")

    # Lancer l'interface Tkinter
    app.mainloop()

