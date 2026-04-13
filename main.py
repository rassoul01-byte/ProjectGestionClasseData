class Etudiant:

        def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenoms
        self.age = age
        self.notes = []

    def ajouter_note(self):
        # Correction : gestion des erreurs si l'utilisateur ne tape pas un nombre
        try:
            n = int(input(f"Combien de notes pour {self.prenom} {self.nom} ? "))
            for i in range(n):
                note = float(input(f"Saisissez la note {i+1} : "))
                self.notes.append(note) # Correction de self.note -> self.notes
        except ValueError:
            print("Veuillez saisir un nombre valide.")  

    def calculer_moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

    def afficher_info(self):
        moy = self.calculer_moyenne()
        print(f"Étudiant : {self.prenom} {self.nom.upper()} | Âge : {self.age} | Moyenne : {moy:.2f}")




class MainApp:


    def run():
        print("Bonjour tout le monde")

if __name__=="__main__":
    MainApp.run()