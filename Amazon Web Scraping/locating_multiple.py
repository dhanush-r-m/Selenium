from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"

driver.get("https://www.amazon.in/s?k=laptop&crid=1P0OMW28JPDKY&sprefix={query}%2Caps%2C240&ref=nb_sb_noss_2")
elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(f"{len(elems)} items found")
for elem in elems:
    print(elem.text)

time.sleep(4)
driver.close()
