
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class ScraperPageProduit:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        
    def ScrapProduit():
        pass