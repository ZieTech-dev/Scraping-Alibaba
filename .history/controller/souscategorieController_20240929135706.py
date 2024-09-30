from selenium.webdriver.common.by import By
import time
from controller.categorieController import CategorieScraper

class SousCategorieScraper(CategorieScraper):
    def __init__(self, url):
        super().__init__(url)

    def get_subcategories(self, subcategory_css):
        """
        Récupère les sous-catégories associées à chaque catégorie.
        """
        subcategories_data = {}
        time.sleep(2)
        subcategories = self.driver.find_elements(By.CSS_SELECTOR, subcategory_css)

        for subcategory in subcategories:
            print(f"\t- Sous Catégorie : {subcategory.text}")
            subcategories_data[subcategory.text] = {
                'url': subcategory.get_attribute("href")
            }
            time.sleep(2)  # Temporisation pour laisser le temps de charger
        return subcategories_data
    
    
    def hover_element(self, xpath):
        """
        Dans cette methode,
        on survole un élément en utilisant son XPATH.
        """
        element = self.driver.find_element(By.XPATH, xpath)
        self.action.move_to_element(element).perform()
        # temporisation pour permettre le chargement des menus
        if element.text:
            print(f" {element.text} survolé ...")
        time.sleep(3)

    def get_categories_with_subcategories(self, category_css, subcategory_css):
        """
        Récupère les catégories et leurs sous-catégories.
        """
        all_data={}
        """Récupère et affiche les catégories et sous-catégories."""
        categories = self.driver.find_elements(By.CSS_SELECTOR, category_css)

        for category in categories[:1]:
            self.action.move_to_element(category).perform()
            print(f"- Categorie : {category.text}")
            #Ajout de ma categorie comme nouvelle clé dans mon DATA
            all_data[category.text]={}
            #Ajout de l'url de ma categorie
            all_data[category.text]['url']={category.get_attribute("href")}
            # temporisation pour permettre le bon scraping
            time.sleep(4)  

            #Creation de la clé SousCategorie pour regrouper tout les sous categorie de la categorie en question
            all_data[category.text]["SousCategorie"]={}
            subcategories = self.driver.find_elements(By.CSS_SELECTOR, subcategory_css)
            for subcategory in subcategories:
                print(f"\t- Sous Categorie: {subcategory.text}")
                #Ajout de la sous Categorie dans sa categorie comme un clé
                all_data[category.text]["SousCategorie"][subcategory.text]={}
                all_data[category.text]["SousCategorie"][subcategory.text]['url']={category.get_attribute("href")}
        return all_data