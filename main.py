from src.classes.etudiant import Etudiant
from src.classes.gestionEtudiant import GestionEtudiant
from src.classes.menuGestionEtudiant import MenuGestionEtudiant as MenuApp

class MainApp:
    
    
    def run():
        MenuApp.showMenu()

if __name__=="__main__":
    MainApp.run()