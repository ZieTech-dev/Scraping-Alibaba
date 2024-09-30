import os
from controller.produitController import ScraperPageProduit

class SousCategorieModel:
    def __init__(self, nom, url):
        self.nom = nom
        self.url = url

    def creer_dossier(self, chemin_parent):
        """Créer un dossier pour la sous-catégorie."""
        chemin_sous_categorie = os.path.join(chemin_parent, self.nom)
        os.makedirs(chemin_sous_categorie, exist_ok=True)
        scraper_produit = ScraperPageProduit()
        
        
