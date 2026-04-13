class MenuGestionEtudiant:
    
    @staticmethod
    def showMenu():
        print("\n--- MENU DE GESTION ---")
        print("1. Ajouter étudiant")
        print("2. Ajouter note")
        print("3. Afficher étudiants")
        print("4. Afficher moyenne classe")
        print("5. Meilleur étudiant")
        print("6. Quitter")
        
    def inputMenuChoice(choice:int)->function:
        match choice:
            case 1:
                return MenuGestionEtudiant.addEtudiantMenuGestion
            case 2:
                return MenuGestionEtudiant.addNoteMenuGestion
            case 3:
                return MenuGestionEtudiant.showEtudiantMenuGestion
            case 4:
                return MenuGestionEtudiant.showMoyenneListEtudianMenuGestiont
            case 5:
                return MenuGestionEtudiant.showMeilleurEtudiantMenuGestion
            case 6:
                return MenuGestionEtudiant.quitMenuGestionEtudiant
            
            case _:
                raise ValueError("La Valeur Doit etre Comprise Entre 1-6")
            
    @staticmethod
    def addEtudiantMenuGestion():
        pass
    
    @staticmethod
    def addNoteMenuGestion():
        pass
    
    @staticmethod
    def showEtudiantMenuGestion():
        pass
    
    @staticmethod
    def showMeilleurEtudiantMenuGestion():
        pass
    
    @staticmethod 
    def showMoyenneListEtudianMenuGestiont():
        pass
    
    @staticmethod
    def quitMenuGestionEtudiant():
        pass
    
    @staticmethod
    def runMenuGestion():
        pass