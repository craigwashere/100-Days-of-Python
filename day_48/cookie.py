import time
from Selenium2 import Selenium2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


selenium = Selenium2('http://orteil.dashnet.org/experiments/cookie/')
INITIAL_WAIT_TIME = 20
WAIT_FACTOR = 1.5
CURRENT_WAIT_TIME = INITIAL_WAIT_TIME

def find_purchase(elements):
    for element in elements[::-1]:
        element_name = element.text.split('\n')[0]
        print(f"element_name: {element_name}, class: {element.get_attribute('class')}")
        if element.text != "" and element.get_attribute("class") == "":
            print(f"bought {element_name}")
            return element

for n in range(20):
    print("looking for cookie", n)
    cookie = selenium.find_id("cookie")
    if cookie != None:
        print('CURRENT_WAIT_TIME', CURRENT_WAIT_TIME)
        timeout = time.time() + CURRENT_WAIT_TIME
        while True:
            if time.time() > timeout:
                break
            cookie.click()

    print("looking for money")
    money = selenium.find_id("money").text.replace(',', '')
    if money != None:
        print('money', money)

    store = selenium.find_id("store")
    if store != None:
        store_children = store.find_elements(By.XPATH, ".//div")
        element_price = store_children[0].text.split(" - ")[1].split()[0].replace(',', '')
        while int(money) >= int(element_price) and store_children[0].get_attribute("class") == "":
            print("checking store..")
            purchase = find_purchase(store_children)
            if purchase != None:
                purchase.click()
                store = selenium.find_id("store")
                store_children = store.find_elements(By.XPATH, ".//div")
                    
    CURRENT_WAIT_TIME *= WAIT_FACTOR


print(selenium.find_id("cps").text)
time.sleep(5)