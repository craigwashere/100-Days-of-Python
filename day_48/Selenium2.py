from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Selenium2:
    def __init__(self, URL):
        print(f"URL={URL}")
        new_driver_path = 'C:/development/python/geckodriver.exe'
        new_binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

        ops = options()
        ops.binary_location = new_binary_path
        serv = Service(new_driver_path)
        browser1 = webdriver.Firefox(service=serv, options=ops)
        self.driver = webdriver.Firefox()
        self.driver.get(URL)
        
    def find_one(self, search_term, search_type):
        try:
            item = self.driver.find_element(search_type, search_term)
        except:
            print(f"Something fucked up looking for {search_term}")
            return None
        else:
            return item
    
    def find_one_id(self, search_term):
        return self.find_one(search_term, By.ID)
        
    def find_one_css(self, search_term):
        return self.find_one(search_term, By.CSS)
        
    def find_one_class(self, search_term):
        return self.find_one(search_term, By.CLASS)
        
    def __del__(self):
        self.driver.quit()