import time
from Selenium2 import Selenium2

selenium = Selenium2('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

print("waiting for page to load")
time.sleep(15)
sign_in_button = selenium.find_one_class("cta-modal__primary-btn ")
if sign_in_button != None:
    sign_in_button.click()

email_box = selenium.find_one_id("username")
if email_box != None:
    email_box.send_keys('')
else:
    time.sleep(10)
    quit()
    
password_box = selenium.find_one_id("password")
if password_box != None:
    password_box.send_keys('')
else:
    time.sleep(10)
    quit()
    
sign_in_button2 = selenium.find_one_class('btn__primary--large')
if sign_in_button2 != None:
    sign_in_button2.click()
else:
    time.sleep(10)
    quit()

print("looking for job list")
job_list = selenium.find_all_css(".job-card-container")

for job in job_list:
    job_name = job.text.split('\n')[0]
    print(f"clicking on {job_name}")
    job.click()
    save_job_button = selenium.find_one_class("jobs-save-button")
    if save_job_button != None:
        save_job_button.click()
        time.sleep(2)
        toast_close_button = selenium.find_one_css(".artdeco-toast-item button")
        toast_close_button.click()
        time.sleep(3)
    