from selenium import webdriver                                          
from selenium.webdriver.chrome.service import Service                   
from selenium.webdriver.common.by import By                              
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up driver
service = Service("C:\\Users\\hp\\Downloads\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")    
options = webdriver.ChromeOptions()                                   
options.add_argument("--headless")              
# options.add_argument("--incognito")
# options.add_argument("--disable-extension")
driver = webdriver.Chrome(service=service, options=options)              

# Open website
driver.get("https://quotes.toscrape.com/js/")

# Wait up to 10 seconds for the first quote to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text"))
)

# Scrape quotes and authors
quotes = driver.find_elements(By.CLASS_NAME, "text")
speakers = driver.find_elements(By.CLASS_NAME, "author")

for quote, speaker in zip(quotes, speakers):
    print(quote.text)
    print(speaker.text)

driver.quit()