
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class ScraperPageProduit:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        
    def ScrapProduit(self):
        # Recuperation de ma liste des produits 
        
        list_produits = self.driver.find_elements(By.CSS_SELECTOR , "div.organic-list.app-organic-search-mb-20.viewtype-gallery div")
        for produit in list_produits:
            img_src = produit.find_element(By. CSS_SELECTOR , "img").get_attribute("src")
            print(f"{img_src}")
            
            
            
if __name__ == "__main__":
    # Initialisation
    scraper = ScraperPageProduit(url='https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.88.381f299aPmdUR2&categoryId=1902&SearchText=Cam%C3%A9ras+vid%C3%A9o&indexArea=product_en&fsb=y&productId=11000017550560')
    scraper.ScrapProduit()