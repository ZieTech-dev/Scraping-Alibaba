import os
import time
import sys
from models.categorieModel import CategorieModel
from models.souscategorieModel import SousCategorieModel

class InterfacePrincipale:
    def __init__(self,DATA):
        self.DATA = DATA

    def clear_console(self):
        time.sleep(1)
        os.system('cls')
        
    def afficher_texte_couleur(texte, couleur):
        couleurs = {
            'bleu': '\033[94m',
            'rouge': '\033[91m',
            'cyan': '\033[96m'
        }
        
        couleur_code = couleurs.get(couleur, '\033[0m')
        print(f"{couleur_code}{texte}\033[0m")
        
    def afficher_chargement(duree):
        chargement = ['|', '/', '-', '\\']
        fin = time.time() + duree
        couleur = '\033[96m' 
        reset = '\033[0m'  

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

    
    def afficher_categories(self,categories):
        """Affiche les catégories avec des index."""
        self.afficher_texte_couleur("\nCatégories disponibles :",'bleu')
        for index, categorie in enumerate(categories.keys()):
            self.afficher_texte_couleur(f"{index + 1}. {categorie}",'cyan')
            
    def afficher_sous_categories(self,sous_categories):
        """Affiche les sous-catégories avec des index."""
        print("\nSous-catégories disponibles :")
        for index, sous_categorie in enumerate(sous_categories.keys()):
            print(f"{index + 1}. {sous_categorie}")
            
    def selectionner_choix(self,choix_max):
        """Permet à l'utilisateur de sélectionner des choix multiples."""
        choix = input(f"Entrez les numéros des options que vous souhaitez sélectionner (ex: 1,3) : ")
        choix_list = [int(c) for c in choix.split(',') if c.isdigit() and 1 <= int(c) <= choix_max]
        return choix_list
    
    def programme_option_scraping(self,categories):
        """Programme principal pour permettre la sélection des catégories et sous-catégories, et stocker les choix."""
        # Initialisation de la variable DATA
        DATA = {}

        # Étape 1: Sélection des catégories
        self.afficher_categories(categories)
        choix_categories = self.selectionner_choix(len(categories))

        # Étape 2: Sélection des sous-catégories et stockage des choix
        for index in choix_categories:
            categorie = list(categories.keys())[index - 1]
            print(f"\nSélection de la catégorie : {categorie}")
            
            sous_categories = categories[categorie]["SousCategorie"]
            self.afficher_sous_categories(sous_categories)
            
            choix_sous_categories = self.selectionner_choix(len(sous_categories))

            # Stocker les choix dans DATA
            DATA[categorie] = {
                "url": categories[categorie]["url"],
                "SousCategorie": {}
            }

            for choix_sous_cat in choix_sous_categories:
                sous_categorie = list(sous_categories.keys())[choix_sous_cat - 1]
                DATA[categorie]["SousCategorie"][sous_categorie] = sous_categories[sous_categorie]

        # Afficher les choix de l'utilisateur
        print("\nVos choix stockés dans DATA :")
        for categorie, details in DATA.items():
            print(f"Catégorie : {categorie}")
            print("Sous-catégories sélectionnées :")
            for sous_categorie in details["SousCategorie"]:
                print(f"  - {sous_categorie}")

        return DATA
    
    
    def programme_principal(self):
        while True:
            self.clear_console()
            choix = self.afficher_menu()
            
            if choix == 1:
                print("\033[5;92mLancement du scraping par défaut... 🕸️\033[0m")
                DATA = self.DATA
                # Chemin du dossier Data
                chemin_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Data')
                # Créer le dossier Data s'il n'existe pas
                os.makedirs(chemin_data, exist_ok=True)
                # Créer les catégories et sous-catégories
                for nom_categorie, details in DATA.items():
                    categorie = CategorieModel(nom_categorie, details['url'])
                    
                    for nom_sous_categorie, sous_details in details['SousCategorie'].items():
                        sous_categorie = SousCategorieModel(nom_sous_categorie, sous_details['url'])
                        categorie.ajouter_sous_categorie(sous_categorie)
                    
                    # Créer le dossier pour la catégorie et ses sous-catégories
                    categorie.creer_dossier(chemin_data)

                print("Les dossiers ont été créés avec succès.")
                
                
            elif choix == 2:
                print("\033[5;92mOuverture des options de scraping... ⚙️\033[0m")
                DATA = self.programme_option_scraping(self.DATA)
                print(f"{DATA}")
                # Chemin du dossier Data
                chemin_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Data')
                # Créer le dossier Data s'il n'existe pas
                os.makedirs(chemin_data, exist_ok=True)

                # Créer les catégories et sous-catégories
                for nom_categorie, details in DATA.items():
                    categorie = CategorieModel(nom_categorie, details['url'])
                    
                    for nom_sous_categorie, sous_details in details['SousCategorie'].items():
                        sous_categorie = SousCategorieModel(nom_sous_categorie, sous_details['url'])
                        categorie.ajouter_sous_categorie(sous_categorie)
                    
                    # Créer le dossier pour la catégorie et ses sous-catégories
                    categorie.creer_dossier(chemin_data)

                print("Les dossiers ont été créés avec succès.")
                                
            elif choix == 3:
                print("\033[5;92mÀ bientôt... 🚪\033[0m")
                break


# categories_data = {
#     "Apparel & Accessories": {
#         "url": "https://www.alibaba.com/Apparel-Accessories_p3",
#         "SousCategorie": {
#             "Apparel Stock": {
#                 "url": "https://www.alibaba.com/Apparel-Accessories_p3"
#             },
#             "Women's Sweater Dress": {
#                 "url": "https://www.alibaba.com/Apparel-Accessories_p3"
#             },
#             "Bra & Brief Sets": {
#                 "url": "https://www.alibaba.com/Apparel-Accessories_p3"
#             },
#             "Women's Tank Tops": {
#                 "url": "https://www.alibaba.com/Apparel-Accessories_p3"
#             }
#         }
#     },
#     "Consumer Electronics": {
#         "url": "https://www.alibaba.com/Consumer-Electronics_p44",
#         "SousCategorie": {
#             "Used Mobile Phones": {
#                 "url": "https://www.alibaba.com/Consumer-Electronics_p44"
#             },
#             "Other Mobile Phone Accessories": {
#                 "url": "https://www.alibaba.com/Consumer-Electronics_p44"
#             },
#             "Set-top Box": {
#                 "url": "https://www.alibaba.com/Consumer-Electronics_p44"
#             },
#             "Used Laptops": {
#                 "url": "https://www.alibaba.com/Consumer-Electronics_p44"
#             },
#             "Selfie Sticks": {
#                 "url": "https://www.alibaba.com/Consumer-Electronics_p44"
#             },
#             "Photographic Lighting": {
#                 "url": "https://www.alibaba.com/Consumer-Electronics_p44"
#             },
#         }
#     }
# }
# if __name__ == "__main__":
    
#     interface_principale = InterfacePrincipale(categories_data)
#     InterfacePrincipale.afficher_chargement(5)
#     interface_principale.programme_principal()
