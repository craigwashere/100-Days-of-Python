import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


new_driver_path = 'C:/development/python/geckodriver.exe'
new_binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

ops = options()
ops.binary_location = new_binary_path
serv = Service(new_driver_path)
browser1 = webdriver.Firefox(service=serv, options=ops)
URL = 'http://secure-retreat-92358.herokuapp.com/'
driver = webdriver.Firefox()
driver.get(URL)

try:
    search_term = "fName"
    box = driver.find_element(By.NAME, search_term)
except:
    print(f"Something fucked up looking for {search_term}")
else:
    box.send_keys("jjjj")

try:
    search_term = "lName"
    box = driver.find_element(By.NAME, search_term)
except:
    print(f"Something fucked up looking for {search_term}")
else:
    box.send_keys("rrrrr")

try:
    search_term = "email"
    box = driver.find_element(By.NAME, search_term)
except:
    print(f"Something fucked up looking for {search_term}")
else:
    box.send_keys("sdfsdf@sdfsd.com")

try:
    search_term = "email"
    #box = driver.find_element(By.NAME, search_term)
    box = driver.find_element(By.CLASS_NAME, "btn-primary")
except:
    print(f"Something fucked up looking for {search_term}")
else:
    box.click()

time.sleep(5)
driver.quit()
