import json
from typing import List, Dict, Optional, Any
from datetime import date
from core.models import Revenu, Dépense, BudgetPrevisionnel

class DataHandler:
    def __init__(self, filename="budget_data.json"):
        self.filename = filename

    def sauvegarder_donnees(self, data: Dict[str, Any]):
        """
        Sauvegarde les données, y compris le budget prévisionnel.
        """
        try:
            with open(self.filename, 'w') as f:
                json.dump(self._serialize_data(data), f, indent=4)  # Utilise la méthode de sérialisation
        except IOError as e:
            print(f"Erreur lors de la sauvegarde des données : {e}")

    def charger_donnees(self) -> Dict[str, Any]:
        """
        Charge les données, y compris le budget prévisionnel.
        """
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Fichier {self.filename} non trouvé. Démarrage avec un budget vide.")
            return {"revenus": [], "depenses": [], "budget_previsionnel": None}  # Initialise budget_previsionnel à None
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erreur lors du chargement des données : {e}. Démarrage avec un budget vide.")
            return {"revenus": [], "depenses": [], "budget_previsionnel": None}  # Initialise budget_previsionnel à None

        data = self._deserialize_data(data) # Désérialise les données chargées
        
        # Assure que 'revenus' et 'depenses' sont toujours des listes
        if "revenus" not in data:
            data["revenus"] = []
        if "depenses" not in data:
            data["depenses"] = []
        
        return data

    def _serialize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sérialise les données avant de les écrire dans le fichier JSON.
        """
        serialized_data = {
            "revenus": [self._serialize_revenu(revenu) for revenu in data["revenus"]],
            "depenses": [self._serialize_depense(depense) for depense in data["depenses"]],
        }
        if data.get("budget_previsionnel"):  # Vérifie si le budget prévisionnel existe
            serialized_data["budget_previsionnel"] = self._serialize_budget_previsionnel(data["budget_previsionnel"])
        else:
            serialized_data["budget_previsionnel"] = None
        return serialized_data

    def _deserialize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Désérialise les données lues depuis le fichier JSON.
        """
        deserialized_data = {
            "revenus": [self._deserialize_revenu(item) for item in data.get("revenus", [])],
            "depenses": [self._deserialize_depense(item) for item in data.get("depenses", [])],
            "budget_previsionnel": self._deserialize_budget_previsionnel(data.get("budget_previsionnel")),
        }
        return deserialized_data

    def _serialize_revenu(self, revenu: Revenu) -> Dict:
        return {
            "montant": revenu.montant,
            "source": revenu.source,
            "date": revenu.date.isoformat(),
        }

    def _deserialize_revenu(self, data: Dict) -> Revenu:
        # Vérifie si la clé "date" existe et n'est pas None
        date_str = data.get("date")
        if date_str is not None:
            try:
                return Revenu(
                    montant=data["montant"],
                    source=data["source"],
                    date=date.fromisoformat(date_str),
                )
            except ValueError:
                print(f"Erreur de format de date: {date_str}. Utilisation de la date actuelle.")
                return Revenu(
                    montant=data["montant"],
                    source=data["source"],
                    date=date.today(),
                )
        else:
            # Si la date est manquante ou None, utilise la date actuelle
            print("Date manquante pour un revenu. Utilisation de la date actuelle.")
            return Revenu(
                montant=data["montant"],
                source=data["source"],
                date=date.today(),
            )

    def _serialize_depense(self, depense: Dépense) -> Dict:
        return {
            "montant": depense.montant,
            "categorie": depense.categorie,
            "date": depense.date.isoformat(),
            "description": depense.description,
        }

    def _deserialize_depense(self, data: Dict) -> Dépense:
        # Vérifie si la clé "date" existe et n'est pas None
        date_str = data.get("date")
        if date_str is not None:
            try:
                return Dépense(
                    montant=data["montant"],
                    categorie=data["categorie"],
                    date=date.fromisoformat(date_str),
                    description=data.get("description", ""),
                )
            except ValueError:
                print(f"Erreur de format de date: {date_str}. Utilisation de la date actuelle.")
                return Dépense(
                    montant=data["montant"],
                    categorie=data["categorie"],
                    date=date.today(),
                    description=data.get("description", ""),
                )
        else:
            # Si la date est manquante ou None, utilise la date actuelle
            print("Date manquante pour une dépense. Utilisation de la date actuelle.")
            return Dépense(
                montant=data["montant"],
                categorie=data["categorie"],
                date=date.today(),
                description=data.get("description", ""),
            )
    
    def _serialize_budget_previsionnel(self, budget_previsionnel: BudgetPrevisionnel) -> Dict:
        """Sérialise un objet BudgetPrevisionnel en un dictionnaire."""
        return {
            categorie: montant
            for categorie, montant in budget_previsionnel.montants_par_categorie.items()
        }

    def _deserialize_budget_previsionnel(self, data: Optional[Dict]) -> Optional[BudgetPrevisionnel]:
        """Désérialise un dictionnaire en un objet BudgetPrevisionnel."""
        if data is None:
            return None
        return BudgetPrevisionnel(montants_par_categorie=data)