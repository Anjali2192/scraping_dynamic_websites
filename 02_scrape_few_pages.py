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

# Open website
driver.get("http://quotes.toscrape.com/login")

# Enter Login details
user_name = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div/input").send_keys("admin")
password = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/input").send_keys("admin\n")

# Function to scrap current page
def scrape_current_page(page_num):
    print(f"scraping page {page_num}")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"quote")))             # You're waiting for the new content (quotes) to fully load before trying to scrape. Prevents scraping data from the previous page. Makes your scraper stable and accurate.
    quotes = driver.find_elements(By.CLASS_NAME,"text")
    for quote in quotes:
        print(quote.text)

# Scrap frist page
scrape_current_page(1)

# Loop to click "Next" and scrap next 4 pages
for i in range(4):
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".next a")))
        next_button.click()
        time.sleep(3)
        scrape_current_page(i + 2)
    except:
        print("No more pages.")
        break

driver.quit()