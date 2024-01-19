import time
import json
import requests
from bs4 import BeautifulSoup
from Selenium2 import Selenium2

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Cookie':'PHPSESSID=14l57oslt9262j95nbmb8aje71',
    'Dnt':'1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    }
    
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

# Write your code below this line 👇

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
test = soup.findAll("script", attrs={"type": "application/json"})
rent_data = test[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")

rent_data = json.loads(rent_data)
rental_data = []
for x in rent_data["cat1"]["searchResults"]["listResults"]:
    detailURL = f"https://www.zillow.com{x['detailUrl']}"
    address = x['address']
    try:
        price = x["price"]
    except KeyError:
        price = x["units"][0]["price"]
    rental_data.append([address, price, detailURL])

selenium = Selenium2("https://docs.google.com/forms/d/e/1FAIpQLScGwfL3oafjwvcGF_lnLZOXCDNZE0GF6JsnloeZdVamyMR7-Q/viewform?usp=sf_link")
print("looking for inputs")
for listing in rental_data:
    for n in range (3):
        input = selenium.find_one_xpath(f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[{n+1}]/div/div/div[2]/div/div[1]/div/div[1]/input")
        input.send_keys(listing[n])

    submit_button = selenium.find_one_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    if submit_button == None:
        quit()
    submit_button.click()

    next_button = selenium.find_one_link("Submit another response")
    next_button.click()

time.sleep(5)