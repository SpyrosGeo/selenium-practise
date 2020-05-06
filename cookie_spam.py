from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
PATH = '/home/thatguy/My-repos/Python/selenium_tutorial/chromedriver'

URL = 'https://orteil.dashnet.org/cookieclicker/'
driver = webdriver.Chrome(PATH)

driver.get(URL)

# try:
#     element = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.ID, "bigCookie"))
#     )
#     for i in range(1,10):
#         element.click()
# except:
#     driver.quit()

driver.implicitly_wait(5)
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice"+str(1)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in  range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()