from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class ScraperPageProduit:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--headless')  # Exécuter en mode headless (sans ouvrir une fenêtre)
        self.options.add_argument('--disable-gpu')  # Nécessaire pour le mode headless sur Windows
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        
    def open_page(self):
        try:
            self.driver.get(self.url)
            time.sleep(2)  # Une pause pour permettre au contenu de charger correctement
        except Exception as e:
            print(f"Erreur lors de l'ouverture de la page : {e}")
        
    def ScrapProduit(self):
        try:
            # Récupération de la liste des produits
            list_produits = self.driver.find_elements(By.CSS_SELECTOR, "div.organic-list.app-organic-search-mb-20.viewtype-gallery div")
            for produit in list_produits:
                try:
                    imgs_src = produit.find_elements(By.CSS_SELECTOR, "img")
                    for img_src in imgs_src:
                        img_src = img_src.get_attribute("src")
                        if img_src:
                            print(f"Image URL: {img_src}")
                except Exception as e:
                    print(f"Erreur lors de la récupération de l'image : {e}")
        except Exception as e:
            print(f"Erreur lors du scraping des produits : {e}")
        finally:
            self.driver.quit()  # Fermer le navigateur après le scraping

if __name__ == "__main__":
    # Initialisation
    scraper = ScraperPageProduit(url='https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.88.381f299aPmdUR2&categoryId=1902&SearchText=Cam%C3%A9ras+vid%C3%A9o&indexArea=product_en&fsb=y&productId=11000017550560')
    scraper.open_page()
    scraper.ScrapProduit()
