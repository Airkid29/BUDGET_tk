import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DefineBudgetWindow(tk.Toplevel):
    def __init__(self, parent, budget_manager):
        super().__init__(parent)
        self.title("Définir Budget Prévisionnel")
        self.geometry("400x390")
        self.resizable(False, False)
        self.budget_manager = budget_manager
        self.categories = ["Alimentation", "Logement", "Transport", "Loisirs", "Santé", "Autres"]
        self.montants_entries = {} # Pour stocker les entrées pour chaque catégorie

        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="Définir Budget Prévisionnel", font=('Segoe UI', 12, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Crée des labels et des entrées pour chaque catégorie
        for i, categorie in enumerate(self.categories):
            label = ttk.Label(main_frame, text=f"{categorie} (€):", font=('Segoe UI', 10))
            label.grid(row=i+1, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(main_frame, font=('Segoe UI', 10))
            entry.grid(row=i+1, column=1, sticky=(tk.W, tk.E), pady=5)
            self.montants_entries[categorie] = entry # Stocke l'entrée dans le dictionnaire

        definir_button = ttk.Button(main_frame, text="Définir Budget", command=self.definir_budget_action, style='TButton')
        definir_button.grid(row=len(self.categories) + 1, column=0, columnspan=2, pady=15)

        cancel_button = ttk.Button(main_frame, text="Annuler", command=self.destroy, style='TButton')
        cancel_button.grid(row=len(self.categories) + 2, column=0, columnspan=2, pady=5)

        main_frame.columnconfigure(1, weight=1)

    def definir_budget_action(self):
        montants_par_categorie = {}
        try:
            for categorie in self.categories:
                montant = float(self.montants_entries[categorie].get())
                if montant < 0:
                    messagebox.showerror("Erreur de saisie", "Les montants du budget doivent être positifs.")
                    return
                montants_par_categorie[categorie] = montant
        except ValueError:
            messagebox.showerror("Erreur de saisie", "Veuillez entrer des montants valides.")
            return

        self.budget_manager.definir_budget_previsionnel(montants_par_categorie)
        messagebox.showinfo("Budget Défini", "Le budget prévisionnel a été défini avec succès.")
        self.destroy()