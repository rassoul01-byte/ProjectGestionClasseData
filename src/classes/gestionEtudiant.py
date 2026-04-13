import classes.etudiant.Etudiant as Etudiant

class GestionEtudiant:
    
    def __init__(self):
        self.listEtudiants=[]
        
    def addEtudiant(self,currentEtudiant:Etudiant):
        self.listEtudiants.append(currentEtudiant)
    
    