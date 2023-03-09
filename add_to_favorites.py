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
driver.get("https://segari.id/")

# Add delay 10 seconds
time.sleep(10)

# Close homepage pop up
try:
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div')
    element.click()

except:
    pass

# Go to account
element = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[5]/div/a')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Click login
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[3]/div')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Input phone number
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/form/input')
element.send_keys('085779628379')

# Click lanjut
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div/button')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Input PIN
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/input[1]')
element.send_keys('0')

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/input[2]')
element.send_keys('7')

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/input[3]')
element.send_keys('1')

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/input[4]')
element.send_keys('4')

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/input[5]')
element.send_keys('9')

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[1]/div[1]/input[6]')
element.send_keys('3')

# Click verifikasi
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div/div[2]/button')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Click home
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div[1]/div/a/a/div/i')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Close homepage pop up
try:
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div')
    element.click()

except:
    pass

# Add delay 2 seconds
time.sleep(3)

# Close testimony pop up
try:
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[1]/div/div')
    element.click()

except:
    pass

# Add delay 2 seconds
time.sleep(2)

# Click search bar
element = driver.find_element(By.XPATH, '//*[@id="searchbox"]/input')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Search jeruk
element = driver.find_element(By.XPATH, '//*[@id="searchbox"]/input')
element.send_keys('Jeruk Sunkist Valencia')
element.send_keys(Keys.RETURN)

# Add delay 2 seconds
time.sleep(2)

# Click product card
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div/div/div/div[1]/div[1]/a[1]/div/div[1]/img')
element.click()

# Add delay 2 seconds
time.sleep(2)

# Click add to favorites
element = driver.find_element(By.XPATH, '//div[@class="ProductDetailsFooter_favoriteButton__15yoA FavoriteButton_heartUnfavoritedV2__2QFYV"]//*[name()="svg"]')
element.click()

# Add delay 1 seconds
time.sleep(1)

# Go to favorites
element = driver.find_element(By.XPATH, '//div[@class="FavoriteButton_toastCtaText__1dPqt"]')
element.click()