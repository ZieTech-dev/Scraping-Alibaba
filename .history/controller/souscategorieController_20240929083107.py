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
        subcategories = self.driver.find_elements(By.CSS_SELECTOR, subcategory_css)

        for subcategory in subcategories:
            print(f"\t- Sous Catégorie : {subcategory.text}")
            subcategories_data[subcategory.text] = {
                'url': subcategory.get_attribute("href")
            }
            time.sleep(2)  # Temporisation pour laisser le temps de charger
        return subcategories_data

    def get_categories_with_subcategories(self, category_css, subcategory_css):
        """
        Récupère les catégories et leurs sous-catégories.
        """
        all_data = {}
        categories_data = self.get_categories(category_css)

        for category in categories_data:
            print(f"Scraping des sous-catégories pour {category}...")
            all_data[category] = {
                'url': categories_data[category]['url'],
                'SousCategorie': self.get_subcategories(subcategory_css)
            }
        return all_data