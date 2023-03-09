from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:\edgedriver_win32\msedgedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

# Open Internal Tools Page
driver.get("https://internal-delta.segari.id/login/")

# Input username
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[1]/input')
element.send_keys("mreza")

# Input password
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[2]/div/input')
element.send_keys("123456")

# Click "Login" button
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/button')
element.click()

# Add delay 8 seconds
time.sleep(8)

# Scroll to SDD Turbo Order Limiter
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/ol/li[16]/ul/li[10]/a')
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# Add delay 2 seconds
time.sleep(2)

# Select level selector
element = driver.find_element(By.XPATH, '//div[@id="root"]/div[4]/div[2]/div/div/div/div/form/div/div[2]/div/div')
element.click()

# Select WH BSD
element = driver.find_element(By.XPATH, '//div[@id="react-select-3-option-15"]')
element.click()

# Input delivery date
element = driver.find_element(By.XPATH, '//input[@name="deliveryDate"]')
element.send_keys("27/02/2023")

# Select hour range
element = driver.find_element(By.XPATH, '//div[@id="root"]/div[4]/div[2]/div/div/div/div/form/div[2]/div/div/div/div/div')
element.click()

# Select "All Hour Range"
element = driver.find_element(By.XPATH, '//div[@id="react-select-4-option-1"]')
element.click()

# Input limiter qty
element = driver.find_element(By.XPATH, '//input[@name="maxOrderCount"]')
element.send_keys("1000")

# Click "Submit"
element = driver.find_element(By.XPATH, '//button[@type="submit"]')
element.click()

# Add delay 2 seconds
time.sleep(2)

# If confirmation pop up displayed, click "Confirm"
try:
    confirmation_button = driver.find_element(By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="Cancel"])[1]/following::button[1]')
    driver.execute_script("arguments[0].scrollIntoView();", confirmation_button)
    confirmation_button.click()

# If confirmation pop up doesn't exist
except:
    pass