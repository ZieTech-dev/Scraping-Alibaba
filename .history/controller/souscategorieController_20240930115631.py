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
            time.sleep(2)  
        return subcategories_data
    
    
    def hover_element(self, xpath):
        """
        Dans cette methode,
        on survole un élément en utilisant son XPATH.
        """
        element = self.driver.find_element(By.XPATH, xpath)
        self.action.move_to_element(element).perform()
        # Attendre pour permettre le chargement des menus
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

        for category in categories[:5]:
            self.action.move_to_element(category).perform()
            print(f"- Categorie : {category.text}")
            
            all_data[category.text]={}
            
            all_data[category.text]['url']=category.get_attribute("href")
            
            time.sleep(4)  

            
            all_data[category.text]["SousCategorie"]={}
            subcategories = self.driver.find_elements(By.CSS_SELECTOR, subcategory_css)
            del subcategories[0]
            for subcategory in subcategories[:len(subcategories)-1]:
                print(f"\t- Sous Categorie: {subcategory.text}")
                
                all_data[category.text]["SousCategorie"][subcategory.text]={}
                all_data[category.text]["SousCategorie"][subcategory.text]['url']=subcategory.get_attribute("href")
        return all_data