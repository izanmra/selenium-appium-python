from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

service = Service('C:\edgedriver_win32\msedgedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=service, options=options)

# Open Website
driver.get("https://www.demoblaze.com/")

# Add delay 2 seconds
time.sleep(2)

# Scroll to Samsung Galaxy S6
element = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/a/img')
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)
element.click()

# Add delay 2 seconds
time.sleep(2)

# Add to cart
element = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
element.click()

# Accept alert
alert = driver.switch_to_alert()
alert.dismiss