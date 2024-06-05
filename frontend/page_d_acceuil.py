import tkinter as tk
from tkinter import ttk
import os

from frontend.interface import interface

def interface_principale(prepare_data,predict_hpi):
    def ouvrir_formulaire():
        interface(prepare_data,predict_hpi)

    root = tk.Tk()
    root.title("Smart Real Estate - Service d'Indice des Prix Immobiliers")

    style = ttk.Style()
    style.configure("Container.TFrame", background="white")

    container = ttk.Frame(root, style="Container.TFrame", padding="20")
    container.grid(row=0, column=0, padx=50, pady=50)

    tk.Label(container, text="Smart Real Estate", font=("Arial", 24, "bold"), fg="#333").grid(row=0, column=0, sticky="w", pady=(0, 10))
    tk.Label(container, text="Bienvenue sur notre service d'indice des prix immobiliers (HPI) !\nNotre plateforme utilise des données économiques et démographiques pour générer des indices de prix immobiliers qui fournissent des informations précieuses sur le marché immobilier.", wraplength=600, justify="left").grid(row=1, column=0, sticky="w", pady=(0, 10))
    tk.Label(container, text="À propos du service", font=("Arial", 16, "bold"), fg="#333").grid(row=2, column=0, sticky="w", pady=(0, 10))
    tk.Label(container, text="Notre service vise à fournir des indices de prix immobiliers fiables et informatifs qui peuvent être utilisés par les investisseurs, les professionnels de l'immobilier et les chercheurs pour prendre des décisions éclairées en matière d'investissement immobilier. En utilisant des données historiques et actuelles, ainsi que des techniques d'analyse avancées, nous générons des indices qui reflètent les tendances du marché immobilier et permettent de mieux comprendre son évolution.", wraplength=600, justify="left").grid(row=3, column=0, sticky="w", pady=(0, 10))
    tk.Label(container, text="Comment ça marche", font=("Arial", 16, "bold"), fg="#333").grid(row=4, column=0, sticky="w", pady=(0, 10))
    tk.Label(container, text="Vous pouvez utiliser notre service en accédant à notre formulaire de génération d'indice. Dans ce formulaire, vous pouvez saisir les informations pertinentes sur le marché immobilier des États-Unis, telles que les données économiques, démographiques et immobilières. En utilisant ces données, notre système génère ensuite un indice de prix immobilier (HPI) qui fournit des informations précieuses sur le marché immobilier dans les Etats Unis.", wraplength=600, justify="left").grid(row=5, column=0, sticky="w", pady=(0, 10))

    btn_generer_indice = tk.Button(container, text="Accéder au formulaire de génération d'indice", bg="#8B4513", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5, command=ouvrir_formulaire)
    btn_generer_indice.grid(row=6, column=0, pady=(20, 0))

    root.mainloop()


