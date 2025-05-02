import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core.budget import BudgetManager
from tkinter import ttk

def afficher_graphique_depenses_par_categorie(parent, budget_manager: BudgetManager):
    """
    Crée et affiche un graphique camembert des dépenses par catégorie.

    Args:
        parent: Le widget parent (Tkinter Frame) dans lequel afficher le graphique.
        budget_manager: Une instance de la classe BudgetManager contenant les données.
    """
    depenses = budget_manager.get_all_depenses()
    if not depenses:
        # Affiche un message si aucune dépense n'est disponible.
        aucun_depense_label = ttk.Label(parent, text="Aucune dépense à afficher.", font=('Segoe UI', 10))
        aucun_depense_label.pack(padx=10, pady=10)
        return

    # Calcule le total des dépenses par catégorie.
    depenses_par_categorie = {}
    for depense in depenses:
        categorie = depense.categorie
        montant = depense.montant
        if categorie in depenses_par_categorie:
            depenses_par_categorie[categorie] += montant
        else:
            depenses_par_categorie[categorie] = montant

    # Prépare les données pour le graphique.
    categories = list(depenses_par_categorie.keys())
    montants = list(depenses_par_categorie.values())
    couleurs = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#b19cd9'] # Quelques couleurs sympa

    # Crée la figure et le graphique camembert.
    figure, ax = plt.subplots(figsize=(5, 4)) # Ajuste la taille si nécessaire
    ax.pie(montants, labels=categories, colors=couleurs, autopct='%1.1f%%', startangle=90)
    ax.set_title('Dépenses par Catégorie', fontdict={'fontsize': 12, 'fontweight': 'bold'})
    # Ajuste la position du titre
    ax.title.set_position([0.5, 1.05])  # Centre le titre au-dessus du graphique
    plt.tight_layout() # Ajuste les paramètres du sous-graphique pour fournir une disposition compacte.

    # Crée un widget Canvas Tkinter pour afficher le graphique dans la fenêtre Tkinter.
    canvas = FigureCanvasTkAgg(figure, master=parent)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True) # Utilise pack ou grid selon ta préférence
    canvas.draw() # Dessine le graphique sur le canvas.

def afficher_graphique_revenus_depenses(parent, budget_manager: BudgetManager):
    """
    Crée et affiche un graphique à barres comparant les revenus et les dépenses.

    Args:
        parent: Le widget parent (Tkinter Frame).
        budget_manager: Une instance de BudgetManager.
    """
    revenus = budget_manager.get_all_revenus()
    depenses = budget_manager.get_all_depenses()

    total_revenus = sum(revenu.montant for revenu in revenus)
    total_depenses = sum(depense.montant for depense in depenses)

    # Prépare les données pour le graphique.
    categories = ['Revenus', 'Dépenses']
    montants = [total_revenus, total_depenses]
    couleurs = ['#86ef7d', '#f472b6']  # Vert pour les revenus, rose pour les dépenses

    # Crée la figure et le graphique à barres.
    figure, ax = plt.subplots(figsize=(5, 4))
    ax.bar(categories, montants, color=couleurs)
    ax.set_title('Comparaison Revenus/Dépenses', fontdict={'fontsize': 12, 'fontweight': 'bold'})
    ax.set_ylabel('Montant (€)', fontdict={'fontsize': 10})
    plt.tight_layout()

    # Crée un widget Canvas Tkinter pour afficher le graphique.
    canvas = FigureCanvasTkAgg(figure, master=parent)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.draw()