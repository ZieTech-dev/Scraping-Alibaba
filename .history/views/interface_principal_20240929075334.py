import os
import time
import sys

class InterfacePrincipale:
    def __init__(self):
        pass

    def clear_console(self):
        time.sleep(1)
        os.system('cls')
        
    def afficher_texte_couleur(texte, couleur):
        couleurs = {
            'bleu': '\033[94m',
            'rouge': '\033[91m'
        }
        
        couleur_code = couleurs.get(couleur, '\033[0m')
        print(f"{couleur_code}{texte}\033[0m")
        
    def afficher_chargement(duree):
        chargement = ['|', '/', '-', '\\']
        fin = time.time() + duree
        couleur = '\033[96m'  # cyan
        reset = '\033[0m'  # Réinitialisation

        while time.time() < fin:
            for symbole in chargement:
                if time.time() >= fin:
                    break
                sys.stdout.write(f'\r{couleur}Chargement... {symbole}{reset}')
                sys.stdout.flush()
                time.sleep(0.2)

        sys.stdout.write(f'\r{couleur}Chargement terminé!{reset}   \n')


    def gestion_erreur(self, message, fonction_validation):
        while True:
            try:
                user_input = input(message)
                
                if fonction_validation(user_input):
                    return user_input
                else:
                    print("\033[91m\n❌ Entrée invalide. Veuillez réessayer.\033[0m\n")
            except Exception as e:
                print(f"\n⚠️ Une erreur s'est produite : {e}\n")
                print("Veuillez réessayer.\n")

    def valider_choix(self, option):
        return option.isdigit() and int(option) in [1, 2, 3]

    def afficher_menu(self):
        print("\033[94m" + """\
        ╔═════════════════════╗
        ║   Menu Principal    ║
        ╚═════════════════════╝
        
        1. 🕸️ Lancer le scraping par défaut de la page Alibaba.com 
        2. ⚙️ Options de scraping 
        3. 🚪 Quitter
        
        """ + "\033[0m"
        )
        choix = self.gestion_erreur("➤ Sélectionnez une option : ", self.valider_choix)
        return int(choix)

    @staticmethod
    def questionnaire():
        "Cette methode contient les questionnaire avec les reponses de l'utilisateur sous forme de donnée"
        questionnaire = {
            'categorie': ["Quelle(s) categorie(s) voulez-vous scraper ?"],
            'sous_categorie': ["Quelle(s) sous categorie(s) voulez-vous scraper ?"]
        }
        return questionnaire
    
    def programme_principal(self):
        while True:
            self.clear_console()
            choix = self.afficher_menu()
            
            if choix == 1:
                print("\033[5;92mLancement du scraping par défaut... 🕸️\033[0m")
                
                
            elif choix == 2:
                print("\033[5;92mOuverture des options de scraping... ⚙️\033[0m")
                for valeur in self.questionnaire().values():
                    print(valeur[0])
                
                
            elif choix == 3:
                print("\033[5;92mÀ bientôt... 🚪\033[0m")
                break

# Exécution du programme
if __name__ == "__main__":
    
    interface_principale = InterfacePrincipale()
    InterfacePrincipale.afficher_chargement(5)
    interface_principale.programme_principal()
