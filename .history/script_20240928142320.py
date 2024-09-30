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
            
            produits_vus = set()  # Pour éviter les doublons
            list_produits = self.driver.find_elements(By.CSS_SELECTOR, "div.organic-list.app-organic-search-mb-20.viewtype-gallery div")
            
            for produit in list_produits:
                # Récupérer et vérifier si le produit a déjà été traité
                try:
                    
                    img_srcs = produit.find_elements(By.CSS_SELECTOR, "div.search-card-e-slider__wrapper img")
                    for img_src in img_srcs:
                        img_src_url = img_src.get_attribute('src')
                        if img_src_url and img_src_url not in produits_vus:
                            produits_vus.add(img_src_url)  # Ajouter l'URL au set pour éviter la répétition
                            print(f"Image URL: {img_src_url}")
                except Exception as e:
                    print(f"Erreur lors de la récupération de l'image : {e}")
                
                # Récupérer et vérifier la description
                try:
                    
                    descriptions = produit.find_elements(By.CSS_SELECTOR, "h2.search-card-e-title span")
                    for description in descriptions:
                        description_text = description.text
                        if description_text and description_text not in produits_vus:
                            produits_vus.add(description_text)  # Ajouter la description au set
                            print(f"Description: {description_text}\n")
                except Exception as e:
                    print(f"Erreur lors de la récupération de la description : {e}")
                
                # Récupérer et vérifier le prix
                try:
                    
                    prixs = produit.find_elements(By.CSS_SELECTOR, "a.search-card-e-detail-wrapper div.search-card-e-price-main")
                    
                    for prix in prixs:
                        prix_text = prix.text
                        if prix_text and prix_text not in produits_vus:
                            produits_vus.add(prix_text)
                            print(f"Prix : {prix_text}\n")
                except Exception as e:
                    print(f"Erreur lors de la récupération de du prix : {e}")
                
                time.sleep(0.5)
        except Exception as e:
            print(f"Erreur lors du scraping des produits : {e}")
        finally:
            self.driver.quit()  # Fermer le navigateur après le scraping

if __name__ == "__main__":
    # Initialisation
    scraper = ScraperPageProduit(url='https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.105.76ab299at3hr9s&categoryId=201932801&SearchText=Ordinateurs+portables+personnels+et+domestiques&indexArea=product_en&fsb=y&productId=1601196644532')
    scraper.open_page()
    scraper.ScrapProduit()
