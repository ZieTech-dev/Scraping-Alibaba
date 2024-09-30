from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

url = 'https://www.alibaba.com'
driver.get(url)

time.sleep(2)
action = ActionChains(driver)

# Survole de toutes les catégories
menu = driver.find_element(By.XPATH, '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[1]')
action.move_to_element(menu).perform()
time.sleep(3)

# Survole de <Mes catégories>
mes_categories = driver.find_element(By.XPATH, '//*[@id="the-new-header"]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]')
action.move_to_element(mes_categories).perform()
time.sleep(3)

# Récupérer les catégories
list_categories = driver.find_elements(By.CSS_SELECTOR, "div.panel-content.secondary-cate-content a")

for categorie in list_categories:
    print(F"{categorie.text}")
    # action.move_to_element(categorie).perform()
    # print(f"- {categorie.text}")
    # list_sous_categorie = driver.find_elements(By.CSS_SELECTOR, "div.final-cate.has-more > a > ul > li > a > span")
    # for sous_categorie in list_sous_categorie:
    #     print(f"\t -{sous_categorie.text}")

# print(f"{list_categories}")

driver.quit()
