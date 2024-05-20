import requests
from bs4 import BeautifulSoup
import csv

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0' } 


def setup():
    print("Setup...")
    URL = "https://www.apartments.com/midland-tx/min-1-bedrooms-pet-friendly-dog/"
    current_page = 1
    pages = 1

    apartments = []

    while True:
        response = requests.get(f"{URL}{current_page}", headers = headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        pages = int(soup.find(class_="pageRange").getText()[-1:])

        soup_apartments = soup.find_all("article")

        for apartment in soup_apartments:
            complex_name = apartment.find(class_="property-title")
            complex_address = apartment.find(class_="property-address")
            complex_url = apartment.find(class_="property-link")
            try:
                apartments.append({"name": complex_name.getText(), "address": complex_address.getText(), "URL": complex_url['href']})
            except:
                pass
            
                
        current_page = current_page + 1
        if current_page > pages:
            break;
        
    print("found {} apartments.".format(len(apartments)))
    return apartments

def get_details(apartment):
    print("Getting details for {}".format(apartment["name"]))
    response = requests.get(apartment["URL"], headers = headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        apartment["rating"] = soup.find(class_="reviewRating").getText()
    except:
        apartment["rating"] = "N/A"
        
    try:
        apartment["price"] = soup.find(class_="rentInfoDetail").getText()
    except:
        apartment["price"] = "N/A"

    section = None
    try:
        section = soup.find(id="feesSection").find("ul").stripped_strings
    except:
        pass

    if section is not None:
        section_array = [repr(string)[1:-1] for string in section]
        for n in range(0, len(section_array), 2):
            apartment[section_array[n]] = section_array[n+1]

apartments = setup()
keys = set()
        
for apartment in apartments:
    get_details(apartment)
    keys |= {s for s in apartment.keys()}

with open('apartments.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = keys,  extrasaction='ignore')
    writer.writeheader()
    writer.writerows(apartments)
