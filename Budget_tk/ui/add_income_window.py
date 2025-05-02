import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import messagebox
from tkinter import messagebox

class AddIncomeWindow(tk.Toplevel):
    def __init__(self, parent, budget_manager, update_callback):
        super().__init__(parent)
        self.title("Ajouter un Revenu")
        self.geometry("350x300")
        self.resizable(False, False)
        self.budget_manager = budget_manager
        self.update_callback = update_callback

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

        # Label et entrée pour la source
        source_label = ttk.Label(main_frame, text="Source:", font=('Segoe UI', 10))
        source_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.source_entry = ttk.Entry(main_frame, font=('Segoe UI', 10))
        self.source_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # Label et DateEntry pour la date
        date_label = ttk.Label(main_frame, text="Date:", font=('Segoe UI', 10))
        date_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.date_entry = DateEntry(main_frame, date_pattern='d/m/Y', font=('Segoe UI', 10))
        self.date_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # Boutons Ajouter et Annuler
        add_button = ttk.Button(main_frame, text="Ajouter", command=self.add_income_action, style='TButton')
        add_button.grid(row=3, column=0, columnspan=2, pady=15)

        cancel_button = ttk.Button(main_frame, text="Annuler", command=self.destroy, style='TButton')
        cancel_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Configuration du redimensionnement des colonnes dans le cadre principal
        main_frame.columnconfigure(1, weight=1)

    def add_income_action(self):
        try:
            montant = float(self.amount_entry.get())
            source = self.source_entry.get()
            date_obj = self.date_entry.get_date()

            if montant > 0 and source:
                self.budget_manager.ajouter_revenu(montant, source, date_obj)
                self.update_callback()
                messagebox.showinfo("Revenu Ajouté", "Le revenu a été ajouté avec succès.") # Message de succès
                self.destroy()
            else:
                messagebox.showerror("Erreur de saisie", "Le montant doit être positif et la source ne peut pas être vide.")
        except ValueError:
            messagebox.showerror("Erreur de saisie", "Veuillez entrer un montant valide.")

if __name__ == "__main__":
    root = tk.Tk()
    class FakeBudgetManager:
        def ajouter_revenu(self, montant, source, date):
            print(f"Revenu (factice) ajouté : Montant={montant}, Source={source}, Date={date}")
    fake_budget_manager = FakeBudgetManager()
    def fake_update_callback():
        print("Callback de mise à jour (factice) appelé.")
    app = AddIncomeWindow(root, fake_budget_manager, fake_update_callback)
    root.mainloop()