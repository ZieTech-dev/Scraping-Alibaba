from categorie_souscategorieController import Scraper

if __name__ == "__main__":
  # Initialisation
  URL = "https://alibaba.com"
  CATEGORY_CSS = '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]'
  SUBCATEGORY_CSS = '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]'
  
  scraper = Scraper(URL)

  # Ouverture de la page
  scraper.open_page()

  # Survole des éléments de la barre de navigation
  scraper.hover_element(CATEGORY_CSS)
  scraper.hover_element(SUBCATEGORY_CSS)

  # Récupération des catégories et sous-catégories
  DATA = scraper.get_categories("div.panel-content.secondary-cate-content a", "div.final-cate.has-more span")
  print(F"{DATA}")

  # Fermeture du navigateur
  scraper.close_driver()


