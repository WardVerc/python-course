from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.decathlon.be/nl/alle-sporten/klimmen/zekeringsen-afdaalapparaten")
decathlon = response.text
soup = BeautifulSoup(decathlon, "html.parser")

list_items = soup.find_all(name="div", class_="vtmn-text-center")
for item in list_items:
    product = item.find(name="h2")
    if product:
        name = product.getText()
        # trim first character (new line) and last 3 characters ("00 ") of the price
        price = item.find(name="span", class_="vtmn-price").getText()[1:-3]
        print(f"{name}: {price}")
    


# in div id="info_content" zit er info, class="info_club"

# with open("dries.html") as file: 
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')

# info_content = soup(name="div", id="info_content")
# traits = soup.find_all(name="div", class_="trait-name-val")

# for trait in traits:
#     print(trait.find(name="a").getText())

# #print(traits)
