from .etudiant import Etudiant

class GestionEtudiant:
    
    def __init__(self):
        self._listEtudiants=[]
        
    
    def listEtudiants(self):
        return self._listEtudiants  
    
    
    def addEtudiant(self,currentEtudiant:Etudiant)->bool:
        """_summary_

        Args:
            currentEtudiant (Etudiant): _description_

        Returns:
            bool: _description_
        """
        try:
            self._listEtudiants.append(currentEtudiant)
            return True
        except :
            return False
        
    def showEtudiant(self)->bool:
        """_summary_

        Returns:
            bool: _description_
        """
        if not len(self._listEtudiants):
            return False
        for index,itemEtudiant in self._listEtudiants:
            print(f"Etudiant : {index+1} {itemEtudiant}")
            return True
    
    def classMoyenne(self)->float:
        if not self.listEtudiants:
            return None
        
        return sum([itemEtudiant._calculerMoyenne() for itemEtudiant in self._listEtudiants])/len(self._listEtudiants)

    
    def meilleurEtudiant(self) -> "Etudiant":
        if not self._listEtudiants:
            return None

        return max(
            self._listEtudiants,
            key=lambda etu: etu.calculer_moyenne()
        )