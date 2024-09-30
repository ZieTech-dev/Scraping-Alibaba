from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options

class AlibabaScraper:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(2)

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

    def get_categories(self, category_css, subcategory_css):
        # Ma variable qui contient mes Categories:{Sous Categories:{url:...............}}
        DATA={}
        """Récupère et affiche les catégories et sous-catégories."""
        categories = self.driver.find_elements(By.CSS_SELECTOR, category_css)

        for category in categories:
            self.action.move_to_element(category).perform()
            print(f"- Categorie : {category.text}")
            #Ajout de ma categorie comme nouvelle clé dans mon DATA
            # temporisation pour permettre le bon scraping
            time.sleep(2)  

            subcategories = self.driver.find_elements(By.CSS_SELECTOR, subcategory_css)
            for subcategory in subcategories:
                print(f"\t- Sous Categorie: {subcategory.text}")

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    # Initialisation
    scraper = AlibabaScraper(url='https://alibaba.com')

    # Ouverture de la page
    scraper.open_page()

    # Survole des éléments de la barre de navigation
    scraper.hover_element('//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]')
    scraper.hover_element('//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]')

    # Récupération des catégories et sous-catégories
    scraper.get_categories("div.panel-content.secondary-cate-content a", "div.final-cate.has-more span")

    # Fermeture du navigateur
    scraper.close_driver()
