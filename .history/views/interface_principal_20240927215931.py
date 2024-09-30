import os
import time

def clear_console():
    time.sleep(1)
    os.system('cls')


print("""
    ╔═════════════════════╗
    ║   Menu Principal    ║
    ╚═════════════════════╝
    1. 🕸️ Lancer le scraping de la page entière 
    
    2. ⚙️ Options de scraping
     
    3. 🚪 Quitter
    ➤ Sélectionnez une option : 
""")

clear_console()