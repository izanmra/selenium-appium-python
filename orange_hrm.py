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


def test_orangehrm_wrong_login():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    element.send_keys('Admin')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    element.send_keys('admin135')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(2)

    driver.quit()

    print("Pass")


def test_orangehrm_correct_login():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    element.send_keys('Admin')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    element.send_keys('admin123')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(3)

    driver.quit()

    print("Pass")


def test_orangehrm_correct_login_then_logout():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    element.send_keys('Admin')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    element.send_keys('admin123')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(4)

    element = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
    element.click()

    time.sleep(2)

    element = driver.find_element(By.LINK_TEXT, "Logout")
    element.click()

    time.sleep(4)

    driver.quit()

    print("Pass")


def test_orangehrm_create_status():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    element.send_keys('Admin')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    element.send_keys('admin123')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(3)

    element = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Buzz']")
    element.click()

    time.sleep(3)

    element = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@class='oxd-layout-context']/div/div[1]/div/div[1]//form[@class='oxd-form']//textarea[@class='oxd-buzz-post-input']")
    element.send_keys('Hai guys, Reza di sini!')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(3)

    driver.quit()

    print("Pass")


def test_orangehrm_create_admin():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    element.send_keys('Admin')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    element.send_keys('admin123')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(3)

    element = driver.find_element(By.XPATH, "//a[normalize-space()='Admin']")
    element.click()

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    element.click()

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i")
    element.click()

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]")
    element.click()

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i")
    element.click()

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]")
    element.click()

    element = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    element.send_keys('Muhammad Reza Ananda')
    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    element.send_keys(Keys.ARROW_DOWN)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    element.send_keys(Keys.RETURN)

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
    element.send_keys('fernando')

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
    element.send_keys('gombal123')

    element = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
    element.send_keys('gombal123')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(5)

    driver.quit()

    print("Pass")


def test_orangehrm_create_employee():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    options = Options()
    options.add_experimental_option("detach", True)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    element.send_keys('Admin')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    element.send_keys('admin123')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(3)

    element = driver.find_element(By.XPATH, "//a[normalize-space()='PIM']")
    element.click()

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    element.click()

    time.sleep(3)

    element = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    element.send_keys('Muhammad')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
    element.send_keys('Reza')

    element = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    element.send_keys('Fernando')

    element = driver.find_element(By.XPATH, "//button[@type='submit']")
    element.click()

    time.sleep(5)

    driver.quit()

    print("Pass")



