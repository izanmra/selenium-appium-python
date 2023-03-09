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

# Scroll to Product Order Limits
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/ol/li[9]/ul/li[1]/a')
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# Add delay 10 seconds
time.sleep(10)

# Click "Bulk Update"
element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/div/div/div/div/div[2]/button[2]')
element.click()

# Select CSV
element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/input')
file_path = "D:\REZA\SELENIUM PYTHON\POL.csv"
element.send_keys(file_path)

# Click "Upload"
element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[3]/button')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Click "Save"
element = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/button')
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()