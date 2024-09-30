from controller.souscategorieController import SousCategorieScraper

if __name__ == "__main__":
  # Initialisation de nos données
  URL = "https://alibaba.com"
  CATEGORY_CSS = '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]'
  SUBCATEGORY_CSS = '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]'
  scraper = SousCategorieScraper(URL)
  scraper.open_page()
  data = scraper.get_categories_with_subcategories(CATEGORY_CSS, SUBCATEGORY_CSS)
  print(data)
  scraper.close_driver()



