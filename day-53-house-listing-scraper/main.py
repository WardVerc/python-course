import requests
from bs4 import BeautifulSoup
import json

FORM_URL = "https://forms.gle/Yr3uTdcTVdoUuw2Z7"
IMMO_URL = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&maxPrice=250000&minPrice=180000&postalCodes=BE-9070,BE-9040,9050&isUnderOption=false&minBedroomCount=1&maxBedroomCount=2&epcScores=A++,A,C,A+,B&page=1&orderBy=relevance"
IMMO_PRICIER_URL = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&epcScores=A++,A,C,A+,B&isUnderOption=false&maxBedroomCount=2&maxPrice=275000&minBedroomCount=1&minPrice=200000&postalCodes=9040,9050,9070&page=1&orderBy=relevance"

response = requests.get(url=IMMO_URL)
immo = response.text
soup = BeautifulSoup(immo, "html.parser")

list_items = soup.find_all(name="p", class_="card--result__price")
for price_index, item in enumerate(list_items):
    price = json.loads(item.find(name="iw-price").get(":price"))["accessibilityPrice"]
    print(f"#{price_index} Prijs: {price}")

rooms_items = soup.find_all(name="p", class_="card__information card--result__information card__information--property")
for rooms_index, rooms in enumerate(rooms_items):
    room = rooms.find_all(name="iw-abbreviation")[0].get(":title")[1:-1]
    print(f"#{rooms_index} Kamers: {room}")

location_items = soup.find_all(name="p", class_="card__information card--results__information--locality card__information--locality")
for location_index, locations in enumerate(location_items):
    location = locations.getText()[25:-21]
    print(f"#{location_index} Location: {location}")

link_items = soup.find_all(name="h2", class_="card__title card--result__title")
for link_index, link_item in enumerate(link_items):
    link = link_item.find_all(name="a")[0].get("href")
    print(f"#{link_index} Url: {link}")

