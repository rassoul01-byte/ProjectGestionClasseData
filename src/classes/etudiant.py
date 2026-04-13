class Etudiant:
    
    Etudiant.-=(0,20)

    def __init__(self, nom: str, prenom: str, age: int, *notes):
        self._nom = nom
        self._prenom = prenom

        if age > 0:
            self._age = age
        else:
            raise ValueError("La valeur de l'âge doit être positive")

        self._notes = list(notes)
        
        @property
        def nom(self):
            return self._nom
        
        @property
        def prenom(self):
            return self.prenom
        
        @property
        def age(self):
            return self._age
        
        
        

    def _addNote(self,currentNote:float)->bool:
        """_summary_

        Args:
            currentNote (float): _description_

        Raises:
            ValueError: _description_

        Returns:
            bool: _description_
        """
        
        if Etudiant.BARREMNOTE[0]<=currentNote<=Etudiant.BARREMNOTE[1]:
            self._notes.append(round(currentNote,2))
            return True
        else:
            raise ValueError(f"La valeur de la Note a ajouter n'est pas comprise entre [{Etudiant.BARREMNOTE[0]}-{Etudiant.BARREMNOTE[1]}]")
    
    
    def _calculerMoyenne(self)->float:
        """_summary_
            Methode permettant d' effectuer le calcul de la moyenne  de la classe Etudiant
        Returns:
            _type_:float
        """
        if not self._notes:
            return 0
        return sum(self._notes)/len(self._notes)
        # try:
        #     n = int(input(f"Combien de notes pour {self.prenom} {self.nom} ? "))
        #     for i in range(n):
        #         note = float(input(f"Saisissez la note {i+1} : "))
        #         self.notes.append(note) # Correction de self.note -> self.notes
        # except ValueError:
        #     print("Veuillez saisir un nombre valide.")  
        
    def __str__(self):
        moy=round(self._calculerMoyenne(),2)
        return f"--> {self._nom:<10} | {self._prenom:<10} | {self._prenom:<10} | {self.moy:<10} "

    # def afficher_info(self):
    #     moy = self.calculer_moyenne()
    #     print(f"Étudiant : {self.prenom} {self.nom.upper()} | Âge : {self.age} | Moyenne : {moy:.2f}")
