import os
import time
import sys

class InterfacePrincipale:
    def __init__(self):
        pass

    def clear_console(self):
        time.sleep(1)
        os.system('cls')
        
    def afficher_chargement(duree):
        chargement = ['|', '/', '-', '\\']
        fin = time.time() + duree  # Durée totale
        while time.time() < fin:
            for symbole in chargement:
                if time.time() >= fin:  # Arrête l'animation lorsque le temps est écoulé
                    break
                sys.stdout.write(f'\rChargement... {symbole}')  # Affiche le symbole
                sys.stdout.flush()  # Vide le tampon immédiatement
                time.sleep(0.2)  # Pause de 0.2 secondes entre chaque symbole

        sys.stdout.write('\rChargement terminé!   \n')  # Remplace la ligne finale


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
        
        1. 🕸️ Lancer le scraping par defaut de la page Alibaba.com 
        2. ⚙️ Options de scraping 
        3. 🚪 Quitter
        
        """)

        choix = self.gestion_erreur("➤ Sélectionnez une option : ", self.valider_choix)
        return int(choix)

    def programme_principal(self):
        while True:
            self.clear_console()
            choix = self.afficher_menu()
            
            if choix == 1:
                print("Lancement du scraping... 🕸️")
                
                
            elif choix == 2:
                print("Ouverture des options de scraping... ⚙️")
                
                
            elif choix == 3:
                print("A bientôt... 🚪")
                break

# Exécution du programme
if __name__ == "__main__":
    
    interface_principale = InterfacePrincipale()
    InterfacePrincipale.afficher_chargement(5)
    interface_principale.programme_principal()
