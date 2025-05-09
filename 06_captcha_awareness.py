from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up driver
service = Service("C:\\Users\\hp\\Downloads\\selenium\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
# Open site
driver.get("https://www.google.com/recaptcha/api2/demo")

# Fillin the details
#driver.find_element(By.ID, "input1").send_keys("admin")
#driver.find_element(By.ID, "input2").send_keys("admin")
#driver.find_element(By.ID, "input3").send_keys("admin@gmail.com")

# Detect if a CAPTCHA is present
if driver.find_elements(By.CLASS_NAME, "g-recaptcha"):
    print("CAPTCHA detected! Human interaction needed.")

# Pause script and solve it manually
input("Solve the CAPTCHA manually, then press Enter to continue...")

# Click the submit button
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/form/fieldset/ul/li[6]/input"))).click()

input("Press Enter to close browser...")
driver.quit()