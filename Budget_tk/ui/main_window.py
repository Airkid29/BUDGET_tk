import tkinter as tk 
from tkinter import ttk
from ui.add_income_window import AddIncomeWindow
from ui.add_expense_window import AddExpenseWindow
from core.budget import BudgetManager
from datetime import datetime
from ui.graphics import afficher_graphique_depenses_par_categorie, afficher_graphique_revenus_depenses
from ui.define_budget_window import DefineBudgetWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulateur de Budget Étudiant")
        self.budget_manager = BudgetManager()

        # Style personnalisé pour les widgets
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure('TLabel', font=('Segoe UI', 11))
        self.style.configure('TButton', font=('Segoe UI', 10), padding=8)
        self.style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), padding=10)

        self.create_widgets()
        self.update_display()  # Utilise la méthode unifiée pour la mise à jour

        # Gestion de la fermeture de la fenêtre
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def create_widgets(self):
        # Cadre principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Titre de l'application
        title_label = ttk.Label(main_frame, text="Gestion de Budget Étudiant", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Boutons d'action
        income_button = ttk.Button(main_frame, text="Ajouter un Revenu", command=self.open_add_income_window, style='TButton')
        income_button.grid(row=1, column=0, padx=10, pady=5, sticky=(tk.W, tk.E))

        expense_button = ttk.Button(main_frame, text="Ajouter une Dépense", command=self.open_add_expense_window, style='TButton')
        expense_button.grid(row=1, column=1, padx=10, pady=5, sticky=(tk.W, tk.E))

        define_budget_button = ttk.Button(main_frame, text="Définir Budget Prévisionnel", command=self.open_define_budget_window, style='TButton')
        define_budget_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=(tk.W, tk.E))

        # Zone d'affichage du budget
        budget_group = ttk.LabelFrame(main_frame, text="Résumé du Budget", padding=10)
        budget_group.grid(row=3, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        self.budget_label = ttk.Label(budget_group, text="Solde actuel :", style='TLabel')
        self.budget_label.grid(row=0, column=0, sticky=tk.W)
        self.budget_amount = ttk.Label(budget_group, text="0.00 €", style='TLabel', font=('Segoe UI', 12, 'bold'))
        self.budget_amount.grid(row=0, column=1, sticky=tk.E)

        # Affichage du budget prévisionnel et des dépassements
        self.prevision_label = ttk.Label(budget_group, text="Budget Prévisionnel :", style='TLabel')
        self.prevision_label.grid(row=1, column=0, sticky=tk.W)
        self.prevision_amount = ttk.Label(budget_group, text="0.00 €", style='TLabel', font=('Segoe UI', 12, 'bold'))
        self.prevision_amount.grid(row=1, column=1, sticky=tk.E)

        self.depassements_label = ttk.Label(budget_group, text="Dépassements :", style='TLabel')
        self.depassements_label.grid(row=2, column=0, sticky=tk.W)
        self.depassements_text = tk.Text(budget_group, height=3, width=30, font=('Segoe UI', 10))
        self.depassements_text.grid(row=2, column=1, sticky=tk.E)
        self.depassements_text.config(state=tk.DISABLED)

        # Zone d'affichage des transactions
        transactions_group = ttk.LabelFrame(main_frame, text="Dernières Transactions", padding=10)
        transactions_group.grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.revenues_label = ttk.Label(transactions_group, text="Revenus :", font=('Segoe UI', 11, 'bold'))
        self.revenues_label.grid(row=0, column=0, sticky=tk.W)
        self.revenues_list = tk.Listbox(transactions_group, font=('Segoe UI', 10), height=5)
        self.revenues_list.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.expenses_label = ttk.Label(transactions_group, text="Dépenses :", font=('Segoe UI', 11, 'bold'))
        self.expenses_label.grid(row=0, column=1, sticky=tk.W, padx=10)
        self.expenses_list = tk.Listbox(transactions_group, font=('Segoe UI', 10), height=5)
        self.expenses_list.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)

        # Zone d'affichage des graphiques
        self.graphics_notebook = ttk.Notebook(main_frame)
        self.graphics_notebook.grid(row=5, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.depenses_frame = ttk.Frame(self.graphics_notebook)
        self.graphics_notebook.add(self.depenses_frame, text="Dépenses par Catégorie")

        self.revenus_depenses_frame = ttk.Frame(self.graphics_notebook)
        self.graphics_notebook.add(self.revenus_depenses_frame, text="Revenus/Dépenses")

        self.update_graphics()

        # Configuration du redimensionnement
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        budget_group.columnconfigure(1, weight=1)
        transactions_group.columnconfigure(0, weight=1)
        transactions_group.columnconfigure(1, weight=1)
        transactions_group.rowconfigure(1, weight=1)
        self.graphics_notebook.columnconfigure(0, weight=1)

    def open_add_income_window(self):
        AddIncomeWindow(self.root, self.budget_manager, self.update_display)

    def open_add_expense_window(self):
        AddExpenseWindow(self.root, self.budget_manager, self.update_display)

    def open_define_budget_window(self):
        DefineBudgetWindow(self.root, self.budget_manager)

    def update_display(self):
        self.update_budget_display()
        self.update_transactions_display()
        self.update_graphics()

    def update_budget_display(self):
        solde = self.budget_manager.calculer_solde()
        self.budget_amount.config(text=f"{solde:.2f} €")

        budget_previsionnel = self.budget_manager.get_budget_previsionnel()
        if budget_previsionnel:
            total_budget_previsionnel = sum(budget_previsionnel.montants_par_categorie.values())
            self.prevision_amount.config(text=f"{total_budget_previsionnel:.2f} €")
        else:
            self.prevision_amount.config(text="Non défini")

        depassements = self.budget_manager.calculer_depassements_budget()
        self.depassements_text.config(state=tk.NORMAL)
        if depassements:
            depassements_str = "\n".join(f"{categorie}: {depassement:.2f} €" for categorie, depassement in depassements.items())
            self.depassements_text.delete(1.0, tk.END)
            self.depassements_text.insert(tk.END, depassements_str)
        else:
            self.depassements_text.delete(1.0, tk.END)
            self.depassements_text.insert(tk.END, "Aucun dépassement")
        self.depassements_text.config(state=tk.DISABLED)

    def update_transactions_display(self):
        self.revenues_list.delete(0, tk.END)
        for revenu in self.budget_manager.get_all_revenus():
            self.revenues_list.insert(tk.END, f"{revenu.date.strftime('%d/%m/%Y')} - +{revenu.montant:.2f}€ ({revenu.source})")

        self.expenses_list.delete(0, tk.END)
        for depense in self.budget_manager.get_all_depenses():
            self.expenses_list.insert(tk.END, f"{depense.date.strftime('%d/%m/%Y')} - -{depense.montant:.2f}€ ({depense.categorie})")

    def update_graphics(self):
        for child in self.depenses_frame.winfo_children():
            child.destroy()
        for child in self.revenus_depenses_frame.winfo_children():
            child.destroy()
        afficher_graphique_depenses_par_categorie(self.depenses_frame, self.budget_manager)
        afficher_graphique_revenus_depenses(self.revenus_depenses_frame, self.budget_manager)

    def _on_closing(self):
        self.budget_manager._sauvegarder_les_donnees()
        self.root.destroy()
