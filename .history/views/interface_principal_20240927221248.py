import os
import time

def clear_console():
    time.sleep(1)
    os.system('cls')


def gestion_erreur(message, fonction_validation):
    while True:
        try:
            user_input = input(message)
            
            if fonction_validation(user_input):
                return user_input
            else:
                print("❌ Entrée invalide. Veuillez réessayer.")
        except Exception as e:
            
            print(f"⚠️ Une erreur s'est produite : {e}")
            print("Veuillez réessayer.\n")

def valider_choix(option):
    return option.isdigit() and int(option) in [1, 2, 3]

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

def programme_principal():
    while True:
        choix = afficher_menu()
        
        if choix == 1:
            print("Lancement du scraping... 🕸️")
            
        elif choix == 2:
            print("Ouverture des options de scraping... ⚙️")
            
        elif choix == 3:
            print("Quitter le programme... 🚪")
            break  


programme_principal()
