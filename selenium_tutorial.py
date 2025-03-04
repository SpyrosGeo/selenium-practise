from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
PATH = '/home/thatguy/My-repos/Python/selenium_tutorial/chromedriver'

driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

page_title = driver.title
search = driver.find_element_by_name("s")
search.send_keys('test')
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name('article')
    print(articles)
    for article in articles:
        header =article.find_element_by_class_name('entry-summary')
        print(header.text)
finally:
    driver.quit()

