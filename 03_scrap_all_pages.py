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

# Open site and Login
driver.get("http://quotes.toscrape.com/login")
user_name = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div/input").send_keys("admin")
password = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/input").send_keys("admin\n")

# Loop through all pages until "next" button disappears
page = 1          # this helps in seeing which page is currently scraping in the terminal and debug easily if page breaks.
while True:
    print(f"Scraping page {page}")

    # Scrap quotes from the current page
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"quote")))             # You're waiting for the new content (quotes) to fully load before trying to scrape. Prevents scraping data from the previous page. Makes your scraper stable and accurate.
    quotes = driver.find_elements(By.CLASS_NAME,"text")
    for quote in quotes:
        print(quote.text)
    # Click next Button
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".next a")))
        next_button.click()
        wait.until(EC.staleness_of(quotes[0]))                           # Wait until old page is gone
        page += 1
    except:
        print("No more pages.")
        break

driver.quit()

# Using while True + try/except to loop until pagination ends
# EC.staleness_of() ensures new content is loaded
# Clean handling of end-of-pagination