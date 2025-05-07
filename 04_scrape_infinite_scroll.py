from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up driver
service = Service("C:\\Users\\hp\\Downloads\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# Open site
driver.get("https://quotes.toscrape.com/scroll")
time.sleep(3)

# Loop to the end of the page
while True:
    height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        print("Reached bottom of page")
        break

    # Scrape the quotes and authors
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"quote")))
    quotes = driver.find_elements(By.CLASS_NAME,"text")
    speakers = driver.find_elements(By.CLASS_NAME, "author")

    for quote, speaker in zip(quotes, speakers):
        print(quote.text)
        print(speaker.text)    

driver.quit()