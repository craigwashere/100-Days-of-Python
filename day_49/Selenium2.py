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
        
        print("Starting service")
        serv = Service(new_driver_path)

        print("Starting browser")
        browser1 = webdriver.Firefox(service=serv, options=ops)       
        self.driver = webdriver.Firefox()
        
        print("loading URL")
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
        return self.find_one(search_term, By.CSS_SELECTOR)
        
    def find_one_class(self, search_term):
        return self.find_one(search_term, By.CLASS_NAME)
        
    def find_one_xpath(self, search_term):
        return self.find_one(search_term, By.XPATH)
        
    def find_all(self, search_term, search_type):
        try:
            items = self.driver.find_elements(search_type, search_term)
        except:
            print(f"Something fucked up looking for {search_term}")
            return None
        else:
            return items
    
    def find_all_child(self, element, search_term):
        try:
            items = element.find_elements(By.XPATH, f"./child::{search_term}")
        except:
            print(f"Something fucked up looking for {search_term}")
            return None
        else:
            return items
        
    
    def find_all_tag(self, search_term):
        return self.find_all(search_term, By.TAG_NAME)
        
    def find_all_css(self, search_term):
        return self.find_all(search_term, By.CSS_SELECTOR)
    
    def find_all_class(self, search_term):
        return self.find_all(self, search_term, By.CLASS_NAME)
        
    def __del__(self):
        self.driver.quit()