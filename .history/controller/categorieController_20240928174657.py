from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

class CategorieScraper:
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
        Survole un élément en utilisant son XPATH.
        """
        element = self.driver.find_element(By.XPATH, xpath)
        self.action.move_to_element(element).perform()
        if element.text:
            print(f"{element.text} survolé ...")
        time.sleep(3)

    def get_categories(self, category_css):
        """
        Récupère les catégories en fonction du CSS selector.
        """
        categories_data = {}
        categories = self.driver.find_elements(By.CSS_SELECTOR, category_css)

        for category in categories:
            self.action.move_to_element(category).perform()
            print(f"- Catégorie : {category.text}")
            categories_data[category.text] = {
                'url': category.get_attribute("href")
            }
            time.sleep(2)  # Temporisation pour laisser le temps de charger
        return categories_data

    def close_driver(self):
        self.driver.quit()
