import os
import time

class InterfacePrincipale:
    def __init__(self):
        pass

    def clear_console(self):
        time.sleep(1)
        os.system('cls')

    def gestion_erreur(self, message, fonction_validation):
        while True:
            try:
                user_input = input(message)
                
                if fonction_validation(user_input):
                    return user_input
                else:
                    print("\n❌ Entrée invalide. Veuillez réessayer.\n")
            except Exception as e:
                print(f"\n⚠️ Une erreur s'est produite : {e}\n")
                print("Veuillez réessayer.\n")

    def valider_choix(self, option):
        return option.isdigit() and int(option) in [1, 2, 3]

    def afficher_menu(self):
        print("""\
        ╔═════════════════════╗
        ║   Menu Principal    ║
        ╚═════════════════════╝
        
        1. 🕸️ Lancer le scraping de la page entière 
        2. ⚙️ Options de scraping 
        3. 🚪 Quitter
        
        """)

        choix = self.gestion_erreur("➤ Sélectionnez une option : ", self.valider_choix)
        return int(choix)

    def programme_principal(self):
        while True:
            choix = self.afficher_menu()
            
            if choix == 1:
                print("Lancement du scraping... 🕸️")
                # Ici tu peux ajouter l'appel à la fonction de scraping
                
            elif choix == 2:
                print("Ouverture des options de scraping... ⚙️")
                # Ici tu peux ajouter le code pour les options de scraping
                
            elif choix == 3:
                print("Quitter le programme... 🚪")
                break

# Exécution du programme
if __name__ == "__main__":
    interface_principale = InterfacePrincipale()
    interface_principale.programme_principal()
