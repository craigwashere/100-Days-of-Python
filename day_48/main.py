import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

#///////////////// Init binary & driver
new_driver_path = 'C:/development/python/geckodriver.exe'
new_binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

ops = options()
ops.binary_location = new_binary_path
serv = Service(new_driver_path)
browser1 = webdriver.Firefox(service=serv, options=ops)

driver = webdriver.Firefox()
driver.get('https://www.python.org')
# shrubbery = driver.find_element(By.CLASS_NAME, 'event-widget')
XPATH = "//div[@class='medium-widget event-widget last']/child::div/ul/li/"

print("looking for dates...")
dates = driver.find_elements(By.XPATH, f"{XPATH}time")

print("looking for events...")    
events = driver.find_elements(By.XPATH, f"{XPATH}a")

upcoming_events = [{'time': dates[n].text, 'name': events[n].text} for n in range(len(dates))]
# for n in range(len(dates)):
    # upcoming_events.append({'time': dates[n], 'name': events[n]})
    
print(upcoming_events)
time.sleep(5)

driver.quit()
