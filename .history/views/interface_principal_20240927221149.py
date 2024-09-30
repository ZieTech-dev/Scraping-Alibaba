import os
import time

def clear_console():
    time.sleep(1)
    os.system('cls')


def gestion_erreur(message, fonction_validation):
    while True:
        try:
            # Demander une entrée utilisateur avec le message personnalisé
            user_input = input(message)
            
            # Valider l'entrée via la fonction passée en paramètre
            if fonction_validation(user_input):
                return user_input
            else:
                print("❌ Entrée invalide. Veuillez réessayer.")
        except Exception as e:
            # Attraper toutes les exceptions et afficher le message d'erreur
            print(f"⚠️ Une erreur s'est produite : {e}")
            print("Veuillez réessayer.\n")

# Exemple de fonction pour valider si l'entrée est un nombre entier valide
def valider_choix(option):
    return option.isdigit() and int(option) in [1, 2, 3]

# Utilisation de la fonction de gestion d'erreur dans un menu
def afficher_menu():
    print("""
    ╔═════════════════════╗
    ║   Menu Principal    ║
    ╚═════════════════════╝
    1. 🕸️ Lancer le scraping de la page entière 
    2. ⚙️ Options de scraping 
    3. 🚪 Quitter
    """)

    choix = gestion_erreur("➤ Sélectionnez une option : ", valider_choix)
    return int(choix)

# Exemple d'utilisation dans le programme principal
def programme_principal():
    while True:
        choix = afficher_menu()
        
        if choix == 1:
            print("Lancement du scraping... 🕸️")
            # Logique de scraping ici
        elif choix == 2:
            print("Ouverture des options de scraping... ⚙️")
            # Logique pour afficher/modifier les options
        elif choix == 3:
            print("Quitter le programme... 🚪")
            break  # Sortir de la boucle principale et quitter

# Exécution du programme principal
programme_principal()
