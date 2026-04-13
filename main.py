from src.classes.etudiant import Etudiant
from src.classes.gestionEtudiant import GestionEtudiant
from src.classes.menuGestionEtudiant import MenuGestionEtudiant as MenuApp

class MainApp:
    
    
    def run():
        MenuApp.showMenu()
        while True:
            try:
                choice=int(input("Veuillez Selectionner votre Choix en valeur numerique : ".capitalize()))
            except ValueError:
                print("La Valeur entrer ne correspond pas a ce qui est attendu veuillez reessayer Merci")
                continue
            MenuApp.inputMenuChoice(choice)
            
            
if __name__=="__main__":
    MainApp.run()