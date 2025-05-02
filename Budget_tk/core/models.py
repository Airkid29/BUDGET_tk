from datetime import date
from typing import Dict

class Revenu:
    def __init__(self, montant: float, source: str, date: date):
        self.montant = montant
        self.source = source
        self.date = date

class Dépense:
    def __init__(self, montant: float, categorie: str, date: date, description: str = ""):
        self.montant = montant
        self.categorie = categorie
        self.date = date
        self.description = description

class BudgetPrevisionnel:
    def __init__(self, montants_par_categorie: Dict[str, float]):
        """
        Initialise le budget prévisionnel.

        Args:
            montants_par_categorie: Un dictionnaire où les clés sont les catégories de dépenses
            et les valeurs sont les montants budgétés.
        """
        self.montants_par_categorie = montants_par_categorie