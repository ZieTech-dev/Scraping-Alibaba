from controller.souscategorieController import SousCategorieScraper
from views.interface_principal import InterfacePrincipale

if __name__ == "__main__":
  # Initialisation de nos données
  URL = "https://alibaba.com"
  CATEGORY_XPATH = '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]'
  SUBCATEGORY_XPATH = '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]'
  
  scraper = SousCategorieScraper(URL)

  # Ouverture de la page
  scraper.open_page()

  # Survole des éléments de la barre de navigation
  scraper.hover_element(CATEGORY_XPATH)
  scraper.hover_element(SUBCATEGORY_XPATH)

  # Récupération des catégories et sous-catégories
  DATA = scraper.get_categories_with_subcategories("div.panel-content.secondary-cate-content a", "div.final-cate.has-more a")
  # Fermeture du navigateur
  # print(DATA)
  scraper.close_driver()
  
  interface_principale = InterfacePrincipale(DATA)
  InterfacePrincipale.afficher_chargement(5)
  interface_principale.programme_principal()



