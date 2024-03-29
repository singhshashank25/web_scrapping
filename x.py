from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get('https://www.seedbasket.in/Buy-Chukkakura-SeedsOnline')

elements = driver.find_elements(By.ID, "tab-description")
for div in elements:
    print(div.text)