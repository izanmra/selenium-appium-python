from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:\edgedriver_win32 (1)\msedgedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

# Open Segari Delta
driver.get("https://www.shafiq.id/")

# Add delay 1 seconds
time.sleep(1)

# Click banner
element = driver.find_element(By.XPATH, '//*[@id="home-slider"]/div/a/picture/img')
element.click()

# Add delay 1 seconds
time.sleep(1)

# Click login CTA
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div/div[2]/p/a')
element.click()

# Add delay 1 seconds
time.sleep(1)

# Input email
element = driver.find_element(By.XPATH, '//*[@id="email"]')
element.send_keys("rezananda12@gmail.com")

# Input password
element = driver.find_element(By.XPATH, '//*[@id="password"]')
element.send_keys("1234Lupa")

# Add delay 10 seconds for solving CAPTCHA manually
time.sleep(10)

# Click login button
element = driver.find_element(By.XPATH, '//*[@id="signup_form"]/div/div/div/div[3]/div[1]/button')
element.click()

# Add delay 1 second
time.sleep(1)

# Click tipe pemodal
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/aside/div/div/div[1]/div[2]/div[2]/div[3]/a/img')
element.click()

# Add delay 1 second
time.sleep(1)

# Scroll & click "Invest Sekarang"
element = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[7]/div[2]/div[2]/div')
button = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[8]/a/button')
driver.execute_script("arguments[0].scrollIntoView();", element)
button.click()

# Add delay 5 second
time.sleep(5)

# Input keyword
element = driver.find_element(By.XPATH, '//*[@id="portfolio-feed-panel"]/div/div[1]/div/input')
element.send_keys("Pengadaan Denim dan Apparel Brand Pride n Joy")

# Click search button
element = driver.find_element(By.XPATH, '//*[@id="portfolio-feed-panel"]/div/div[1]/div/div/button')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Click detail sukuk
element = driver.find_element(By.XPATH, '//*[@id="campaign-gallery"]/div/div[1]/img')
element.click()

# Add delay 1 second
time.sleep(1)

# Click carousel arrow
element = driver.find_element(By.XPATH, '//*[@id="campaign-gallery"]/button[1]')
element.click()

# Click carousel arrow
element = driver.find_element(By.XPATH, '//*[@id="campaign-gallery"]/button[1]')
element.click()

# Click drop down menu
element = driver.find_element(By.XPATH, '//*[@id="offcanvas"]/div[2]/div/button')
element.click()

# Click logout
element = driver.find_element(By.XPATH, '//*[@id="offcanvas"]/div[2]/div/div/a[2]')
element.click()
