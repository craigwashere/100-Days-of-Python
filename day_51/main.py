import time
from Selenium2 import Selenium2

selenium = Selenium2("https://www.speedtest.net/")

print("looking for start button...")
start_button = selenium.find_one_css(".start-text")
if start_button == None:
    quit()
    
start_button.click()

time.sleep(45)

download_speed = selenium.find_one_css(".download-speed")
if download_speed == None:
    quit()

upload_speed = selenium.find_one_css(".upload-speed")
if upload_speed == None:
    quit()
    
print(f"Download: {download_speed.text} Upload: {upload_speed.text}")

#I don't have twitter