from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get('https://www.seedbasket.in/Vegetable-seeds/Hybrid-Seeds')

name = []
image_link = []
src = []
price = []

try:
    # Find elements by class name
    elements = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    for div in elements:
        img_elements = div.find_elements(By.TAG_NAME, "img")
        img_src = img_elements[0].get_attribute("src")
        if img_src:
            print("Image src:", img_src)
            image_link.append(img_src)
        
        a_elements = div.find_elements(By.TAG_NAME, "a")
        href = a_elements[0].get_attribute("href")
        if href:
            print("Anchor href:", href)
            src.append(href)

        h4_elements = div.find_elements(By.TAG_NAME, "h4")
        na = h4_elements[0].text
        if na:
            print(na)
            name.append(na)
        
        span_elements = div.find_elements(By.CLASS_NAME, "price")
        nam = span_elements[0].text
        if nam:
            print(nam)
            price.append(nam)
finally:
    # Close the browser window
    driver.quit()
    # pass


df = pd.DataFrame({
    "name":name,"Image_link":image_link,
    "src":src,"Price":price
})

csv_file_path = "herbal.csv"

# Convert DataFrame to CSV and save it
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully at:", csv_file_path)
