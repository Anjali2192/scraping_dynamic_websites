from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up driver
service = Service("C:\\Users\\hp\\Downloads\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# Open site
driver.get("https://www.lambdatest.com/selenium-playground/")

# Click the Bootstrap Modals
#first_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/section[2]/div/ul/li[6]/a")))
first_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Bootstrap Modals")))
first_button.click()
time.sleep(3)

# Click the Launch Modal
second_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section[3]/div/div/div/div[1]/button")))
second_button.click()
time.sleep(3)

# Extract title and text from the paragraph
title = driver.find_element(By.XPATH, "/html/body/div[1]/section[3]/div/div/div/div[1]/div[2]/div/div/div[1]/h4")
text = driver.find_element(By.XPATH, "/html/body/div[1]/section[3]/div/div/div/div[1]/div[2]/div/div/div[2]/p")
print(title.text.strip())
print(text.text)

# Enter Close button
close_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section[3]/div/div/div/div[1]/div[2]/div/div/div[3]/button[1]")))
close_button.click()

# Go to input Form
driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
time.sleep(3)

# Enter the details
name = driver.find_element(By.ID, "name").send_keys("admin")
email = driver.find_element(By.ID, "inputEmail4").send_keys("admin@gmail.com")
password = driver.find_element(By.ID, "inputPassword4").send_keys("admin")
company = driver.find_element(By.ID, "company").send_keys("admin")
website = driver.find_element(By.ID, "websitename").send_keys("admin")
city = driver.find_element(By.ID, "inputCity").send_keys("admin")
address1 = driver.find_element(By.ID, "inputAddress1").send_keys("admin")
address2 = driver.find_element(By.ID, "inputAddress2").send_keys("admin")
state = driver.find_element(By.ID, "inputState").send_keys("admin")
zipcode = driver.find_element(By.ID, "inputZip").send_keys("admin")

# Select dropdown
country = Select(driver.find_element(By.NAME, "country")).select_by_visible_text("India")
time.sleep(3)

# Click on Submit
submit = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/section[2]/div/div/div/div/form/div[6]/button")))
submit.click()

# Screenshot of last page
driver.save_screenshot("C:/Users/hp/Downloads/python.png")

driver.quit()