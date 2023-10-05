import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.com.be/-/nl/Massagepistool-verstelbaar-spiermasseur-verwisselbare-led-touchscreen/dp/B08K3GNCLV/ref=sr_1_5?crid=1AL681XDHX0XP&keywords=massage%2Bgun&qid=1696512049&sprefix=%2Caps%2C65&sr=8-5&th=1"
url_ps5 = "https://www.amazon.com.be/-/nl/Sony-PlayStation-DualSense-draadloze-controller/dp/B08H98GVK8/ref=sr_1_5?crid=1RF50PUZBYJRG&keywords=ps5&qid=1696513278&sprefix=ps5%2Caps%2C123&sr=8-5"

# check these headers via myhttpheader.com
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=url_ps5, headers=headers)
amazon = response.text
soup = BeautifulSoup(amazon, "lxml")
product_title = soup.find(name="span", id="productTitle").getText()[8:-7]
price = soup.find(name="span", class_="a-price-whole").getText()[:-1]
print(f"{product_title}: \n{price} eurootses")

# Send mail when price < your_buy_price
