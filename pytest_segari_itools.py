import pytest
import pynput
from pynput.keyboard import Key, Controller
import pyautogui
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time


def test_segari_itools_create_order_limiter():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    # Open Internal Tools Page
    driver.get("https://internal-charlie.segari.id/login/")

    # Input username
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[1]/input')
    element.send_keys("mreza")

    # Input password
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[2]/div/input')
    element.send_keys("123456")

    # Click "Login" button
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/button')
    element.click()

    # Wait for success bar
    time.sleep(2)

    # Close success bar
    element = driver.find_element(By.XPATH, "//div[@id='root']/div[@role='alert']//span[.='×']")
    element.click()

    # Scroll to SDD Order Limiter
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/ol/li[15]/ul/li[9]/a')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    # Add delay 1 seconds
    time.sleep(1)

    # Click "Singular Upload"
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/div/div[1]/div/div[2]/div/button[1]')
    element.click()

    # Input delivery date
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[1]/div/input')
    current_date = datetime.now().strftime("%d/%m/%Y")
    element.send_keys(current_date)

    # Click WH selector
    wh_dropdown_element = driver.find_element(By.XPATH,
                                              '/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/div[2]')
    wh_dropdown_element.click()

    # Select WH Tangerang
    element = driver.find_element(By.ID, 'react-select-5-option-5')
    element.click()

    # Click variant selector
    var_dropdown_element = driver.find_element(By.XPATH,
                                               '/html/body/div[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div')
    var_dropdown_element.click()

    # Select variant Turbo
    turbo_element = driver.find_element(By.XPATH,
                                        "/html/body/div[@role='dialog']/div[@class='modal-dialog']/div[@class='modal-content']//form[@action='#']/div[1]/div[3]/div[@class='col']/div/div/div[1]/div[.='Turbo']")
    turbo_element.click()

    # Click range selector
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[4]/div/div/div')
    element.click()

    # Select all hour range
    element = driver.find_element(By.XPATH,
                                  "/html/body/div[@role='dialog']/div[@class='modal-dialog']//form[@action='#']/div[1]/div[4]/div[@class='col']/div/div/div[1]/div[.='All Hour Range (00:00 - 23:59)']")
    element.click()

    # Input limiter qty
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[5]/div/input')
    element.send_keys("1000")

    # Click "Upload"
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/button')
    element.click()

    # Add delay 1 seconds
    time.sleep(1)

    # If confirmation pop up displayed, click "Confirm"
    try:
        confirmation_button = driver.find_element(By.XPATH, "/html/body/div[5]//button[@class='btn btn-danger']")
        driver.execute_script("arguments[0].scrollIntoView();", confirmation_button)
        element = driver.find_element(By.XPATH, "/html/body/div[5]//button[@class='btn btn-danger']")
        element.click()

    # If confirmation pop up doesn't exist
    except:
        pass

    # Wait for success bar
    time.sleep(1)

    # Close success bar
    element = driver.find_element(By.XPATH, "//div[@id='root']/div[@role='alert']//span[.='×']")
    element.click()

    # Close config popup
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/button/span[1]')
    element.click()

    # Add delay 1 seconds
    time.sleep(1)

    # Close Browser
    driver.quit()

    print("Pass")


def test_segari_itools_edit_price():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    # Open Internal Tools Page
    driver.get("https://internal-charlie.segari.id/login/")

    # Input username
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[1]/input')
    element.send_keys("mreza")

    # Input password
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[2]/div/input')
    element.send_keys("123456")

    # Click "Login" button
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/button')
    element.click()

    # Wait for success bar
    time.sleep(2)

    # Close success bar
    element = driver.find_element(By.XPATH, "//div[@id='root']/div[@role='alert']//span[.='×']")
    element.click()

    # Scroll to Configure Price Group Products
    element = driver.find_element(By.XPATH, "//a[normalize-space()='/price-group-products/configure']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    # Wait for loading
    time.sleep(18)

    # Input SKU name
    element = driver.find_element(By.XPATH, "//*[@id='react-select-5-input']")
    element.send_keys('Daging Impor Ekonomis Potong Sup')
    time.sleep(5)

    # Click enter
    element = driver.find_element(By.XPATH, "//*[@id='react-select-5-input']")
    element.send_keys(Keys.RETURN)

    time.sleep(2)

    # Click filter data
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Filter Data']")
    element.click()

    time.sleep(3)

    # Click edit
    element = driver.find_element(By.XPATH, "//div[8]//span[1]")
    element.click()

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys(Keys.BACKSPACE)

    # Input Price
    element = driver.find_element(By.XPATH, "//input[@name='price']")
    element.send_keys('111111')

    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys(Keys.BACKSPACE)

    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys(Keys.BACKSPACE)

    # Input Price Before
    element = driver.find_element(By.XPATH, "//input[@name='priceBefore']")
    element.send_keys('222222')

    # Scroll to Label
    element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[9]/select")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    # Select Promo
    element = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[9]/select/option[2]")
    element.click()

    # Scroll to Save Changes
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Save Changes']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)

    # Close Browser
    driver.quit()

    print("Pass")


def test_segari_itools_add_keyword():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    # Open Internal Tools Page
    driver.get("https://internal-charlie.segari.id/login/")

    # Input username
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[1]/input')
    element.send_keys("mreza")

    # Input password
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/div[2]/div/input')
    element.send_keys("123456")

    # Click "Login" button
    element = driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/form/button')
    element.click()

    # Wait for success bar
    time.sleep(2)

    # Close success bar
    element = driver.find_element(By.XPATH, "//div[@id='root']/div[@role='alert']//span[.='×']")
    element.click()

    # Scroll to Search Autocomplete
    element = driver.find_element(By.XPATH, "//a[normalize-space()='/search-autocomplete']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(2)

    # Input Keyword
    element = driver.find_element(By.XPATH, "//input[@placeholder='Masukkan Keyword Baru']")
    element.send_keys('Kopi Luwak')

    # Input Popularity Value
    element = driver.find_element(By.XPATH, "//input[@name='popularity']")
    element.send_keys('321')

    # Click Add
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    element.click()

    time.sleep(3)

    # Search Keyword
    element = driver.find_element(By.XPATH, "//input[@placeholder='Masukkan Keyword']")
    element.send_keys('Kopi Luwak')

    time.sleep(3)

    # Close Browser
    driver.quit()

    print("Pass")
