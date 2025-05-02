import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import messagebox
from tkinter import messagebox

class AddExpenseWindow(tk.Toplevel):
    def __init__(self, parent, budget_manager, update_callback):
        super().__init__(parent)
        self.title("Ajouter une Dépense")
        self.geometry("350x300")
        self.resizable(False, False)
        self.budget_manager = budget_manager
        self.update_callback = update_callback
        self.categories = ["Alimentation", "Logement", "Transport", "Loisirs", "Santé", "Autres"]

        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Label et entrée pour le montant
        amount_label = ttk.Label(main_frame, text="Montant (€):", font=('Segoe UI', 10))
        amount_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.amount_entry = ttk.Entry(main_frame, font=('Segoe UI', 10))
        self.amount_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.amount_entry.focus()

        # Label et Combobox pour la catégorie
        category_label = ttk.Label(main_frame, text="Catégorie:", font=('Segoe UI', 10))
        category_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.category_combo = ttk.Combobox(main_frame, values=self.categories, font=('Segoe UI', 10))
        self.category_combo.set(self.categories[0])
        self.category_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # Label et entrée pour la description (optionnel)
        description_label = ttk.Label(main_frame, text="Description (facultatif):", font=('Segoe UI', 10))
        description_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.description_entry = ttk.Entry(main_frame, font=('Segoe UI', 10))
        self.description_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # Label et DateEntry pour la date
        date_label = ttk.Label(main_frame, text="Date:", font=('Segoe UI', 10))
        date_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.date_entry = DateEntry(main_frame, date_pattern='d/m/Y', font=('Segoe UI', 10))
        self.date_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

        # Boutons Ajouter et Annuler
        add_button = ttk.Button(main_frame, text="Ajouter", command=self.add_expense_action, style='TButton')
        add_button.grid(row=4, column=0, columnspan=2, pady=15)

        cancel_button = ttk.Button(main_frame, text="Annuler", command=self.destroy, style='TButton')
        cancel_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Configuration du redimensionnement des colonnes dans le cadre principal
        main_frame.columnconfigure(1, weight=1)

    def add_expense_action(self):
        try:
            montant = float(self.amount_entry.get())
            categorie = self.category_combo.get()
            description = self.description_entry.get()
            date_obj = self.date_entry.get_date()

            if montant > 0:
                self.budget_manager.ajouter_depense(montant, categorie, date_obj, description)
                self.update_callback()
                messagebox.showinfo("Dépense Ajoutée", "La dépense a été ajoutée avec succès.") # Message de succès
                self.destroy()
            else:
                messagebox.showerror("Erreur de saisie", "Le montant doit être positif.")
        except ValueError:
            messagebox.showerror("Erreur de saisie", "Veuillez entrer un montant valide.")

if __name__ == "__main__":
    root = tk.Tk()
    class FakeBudgetManager:
        def ajouter_depense(self, montant, categorie, date, description=""):
            print(f"Dépense (factice) ajoutée : Montant={montant}, Catégorie={categorie}, Description='{description}', Date={date}")
    fake_budget_manager = FakeBudgetManager()
    def fake_update_callback():
        print("Callback de mise à jour (factice) appelé.")
    app = AddExpenseWindow(root, fake_budget_manager, fake_update_callback)
    root.mainloop()