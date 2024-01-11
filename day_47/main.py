import requests
from bs4 import BeautifulSoup
import html5lib

URL = f"https://camelcamelcamel.com/product/B06Y1MP2PY"
BUY_PRICE = float(100)

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

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html5lib')

price = float(soup.select_one("div p span span").getText().split('$')[1])

## borrowed the following from udemy comment section
if price < BUY_PRICE:
    message = f"{title} is now ${price}"
 
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user="YOUR EMAIL", password="YOUR PASSWORD")
        connection.sendmail(
            from_addr="SENDER EMAIL",
            to_addrs="RECEIVER EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )

