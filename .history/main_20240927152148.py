from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'https://www.alibaba.com'

driver.get(url)

time.sleep(3)

action = ActionChains(driver)

#Survole de toutes les categiries
menu=driver.find_element(By.XPATH, '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]')
time.sleep(3)
action.move_to_element(menu).perform()
time.sleep(3)

#Survole de < Mes catégories >
mes_categories=driver.find_element(By.XPATH, '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]')
time.sleep(3)
action.move_to_element(mes_categories).perform()
time.sleep(3)

#Recuperer les categories
list_categorie = driver.find_elements(By.CSS_SELECTOR , "div.panel-wrapper.secondary-cate div.panel-content.secondary-cate-content")

for categorie in list_categorie:
    action.move_to_element(categorie).perform
print(f"{list_categorie}")





driver.quit()






























# # Scraper le menu


# # Fermer le navigateur

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# class CategorieControler:
#     def _init_(self, driver):
#         self.driver = driver

#     def open_page(self, url):
#         # Accéder à la page web
#         self.driver.get(url)
#         time.sleep(3)  # Attendre que la page se charge

#     def scrape_menu(self):
#         # Trouver le menu par son XPATH
#         try:
#             menu = self.driver.find_element(By.XPATH, '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]')
#             # Utiliser ActionChains pour interagir avec le menu
#             action = ActionChains(self.driver)
#             action.move_to_element(menu).perform()
#             time.sleep(3)
#         except Exception as e:
#             print(f"Erreur lors du scrapping du menu : {e}")

#     def close_browser(self):
#         # Fermer le navigateur
#         self.driver.quit()
