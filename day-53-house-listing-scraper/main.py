import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


GOOGLE_LOGIN_MAIL = ""
GOOGLE_LOGIN_PASSWORD = ""
IMMO_URL = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&maxPrice=250000&minPrice=180000&postalCodes=BE-9070,BE-9040,9050&isUnderOption=false&minBedroomCount=1&maxBedroomCount=2&epcScores=A++,A,C,A+,B&page=1&orderBy=relevance"
IMMO_PRICIER_URL = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-koop?countries=BE&epcScores=A++,A,C,A+,B&isUnderOption=false&maxBedroomCount=2&maxPrice=275000&minBedroomCount=1&minPrice=200000&postalCodes=9040,9050,9070&page=1&orderBy=relevance"
FORM_URL = "https://forms.gle/Yr3uTdcTVdoUuw2Z7"

# ------------------------ B. SOUP SCRAPER ------------------------ #

response = requests.get(url=IMMO_PRICIER_URL)
immo = response.text
soup = BeautifulSoup(immo, "html.parser")
results = []

list_items = soup.find_all(name="p", class_="card--result__price")
for price_index, item in enumerate(list_items):
    price = json.loads(item.find(name="iw-price").get(":price"))["accessibilityPrice"]
    # add dictionary with the price
    results.append({"price": price})
    #print(f"#{price_index} Prijs: {price}")

rooms_items = soup.find_all(name="p", class_="card__information card--result__information card__information--property")
for rooms_index, rooms in enumerate(rooms_items):
    room = rooms.find_all(name="iw-abbreviation")[0].get(":title")[1:-1]
    # add/update dictionary on the index, with the rooms
    results[rooms_index].update({"rooms": room})
    #print(f"#{rooms_index} Kamers: {room}")

location_items = soup.find_all(name="p", class_="card__information card--results__information--locality card__information--locality")
for location_index, locations in enumerate(location_items):
    location = locations.getText()[25:-21]
    # add/update dictionary on the index, with the location
    results[location_index].update({"location": location})
    #print(f"#{location_index} Location: {location}")

link_items = soup.find_all(name="h2", class_="card__title card--result__title")
for link_index, link_item in enumerate(link_items):
    link = link_item.find_all(name="a")[0].get("href")
    # add/update dictionary on the index, with the url
    results[link_index].update({"link": link})
    #print(f"#{link_index} Url: {link}")

print(results)



# ------------------------ SELENIUM FORM FILLER ------------------------ #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(FORM_URL)

time.sleep(3)

# Login google
input_login_email = driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
input_login_email.send_keys(GOOGLE_LOGIN_MAIL)
input_login_email.send_keys(Keys.ENTER)

time.sleep(3)

input_login_password = driver.find_element(By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
input_login_password.send_keys(GOOGLE_LOGIN_PASSWORD)
input_login_password.send_keys(Keys.ENTER)

time.sleep(15)

def fill_in_form(index: int):
    input_location = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_rooms = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')

    input_location.send_keys(results[index]["location"])
    input_rooms.send_keys(results[index]["rooms"])
    input_price.send_keys(results[index]["price"])
    input_link.send_keys(results[index]["link"])

    send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    send_button.click()

    time.sleep(1)

    another_one_link = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_one_link.click()
    time.sleep(1)

for index in range(len(results)):
    fill_in_form(index)

driver.quit() 
