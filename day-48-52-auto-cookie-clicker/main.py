from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# ------------------------ COOKIE CLICKER BOT ------------------------ #

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
start_time = time.time()
end_time = start_time + 60*5
game_on = True

def check_upgrade():
    if time.time() > end_time:
        global game_on
        game_on = False
        cps = driver.find_element(By.ID, value='cps').text
        print(f"Final {cps}")
    else:
        # Take upgrades and reverse the list
        upgrades = driver.find_elements(By.CSS_SELECTOR, value='#store div')[::-1]
        cps = driver.find_element(By.ID, value='cps').text
        print(cps)
        for upgrade in upgrades:
            classname = upgrade.get_attribute("class")
            if classname != "amount" and classname != "grayed":
                upgrade.click()
                break

while game_on:
    cookie.click()
    current_time = time.time()
    if current_time - start_time > 5:
        check_upgrade()
        start_time = current_time





# ------------------------ WIKIPEDIA CHECKER ------------------------ #

# def search_wikipedia(search_term: str):
#     driver.get("https://nl.wikipedia.org/wiki/Hoofdpagina")
#     article_count = driver.find_element(By.CSS_SELECTOR, value=".hp-statistieken-1 div b")
#     print(f"Aantal artikels (NL): {article_count.text}")

#     search = driver.find_element(By.NAME, value="search")
#     search.send_keys(search_term)
#     search_again = driver.find_element(By.NAME, value="search")
#     search_again.send_keys(Keys.ENTER)
#     list = driver.find_elements(By.CSS_SELECTOR, value="#mw-content-text div ul li")
#     george = list[0].text
#     print(george)

# search_wikipedia("Python")


# ------------------------ FUTBIN PRICE CHECKER ------------------------ #

# def check_futbin_price(player_url: str):
#     driver.get(player_url)
#     price = driver.find_element(By.XPATH, value='//*[@id="ps-lowest-1"]')
#     player_name = driver.find_element(By.XPATH, value='//*[@id="info_content"]/table/tbody/tr[1]/td')
#     version = driver.find_element(By.XPATH, value='//*[@id="info_content"]/table/tbody/tr[16]/td')

#     print(f"{player_name.text} ({version.text}) costs now: {price.text}")

# player_kevin = "https://www.futbin.com/24/player/37/kevin-de-bruyne"
# player_doku_inform = "https://www.futbin.com/24/player/18905/j%C3%A9r%C3%A9my-doku"

# check_futbin_price(player_kevin)
# # # can't check more than 1 player at a time, futbin blocks it :/
# # check_futbin_price(player_doku_inform)




# driver.close() # closes tab
driver.quit() # quits program