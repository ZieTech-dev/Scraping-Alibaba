import os
from controller.produitController import ScraperPageProduit

class CategorieModel:
    def __init__(self, nom, url):
        self.nom = nom
        self.url = url
        self.sous_categories = []

    def ajouter_sous_categorie(self, sous_categorie):
        """Ajouter une sous-catégorie à la catégorie."""
        self.sous_categories.append(sous_categorie)

    def creer_dossier(self, chemin_data):
        """Créer un dossier pour la catégorie et ses sous-catégories."""
        chemin_categorie = os.path.join(chemin_data, self.nom)
        os.makedirs(chemin_categorie, exist_ok=True)

        # # Créer un fichier pour stocker l'URL de la catégorie
        # with open(os.path.join(chemin_categorie, 'url.txt'), 'w') as file:
        #     file.write(self.url)

        # Créer les dossiers pour les sous-catégories
        for sous_categorie in self.sous_categories:
            chemin_sous_categorie = sous_categorie.creer_dossier(chemin_categorie)
            scraper_produit = ScraperPageProduit(self.url, chemin_sous_categorie)
            scraper_produit.open_page()
            scraper_produit.ScrapProduit()