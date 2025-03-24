# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

@pytest.fixture
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:platformVersion": "5.1.1",
        "appium:deviceName": "920121e3e4fc3331",
        "appium:appPackage": "com.samsung.android.app.memo",
        "appium:appActivity": "com.samsung.android.app.memo.Main",
        "appium:noReset": True,
        "appium:forceAppLaunch": True,
        "appium:newCommandTimeout": 3600,
        "appium:uiautomator2ServerInstallTimeout": 60000
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_create_new_memo(driver):
    wait = WebDriverWait(driver, 10)  # Tunggu maksimal 10 detik

    el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create memo")))
    el1.click()

    el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.samsung.android.app.memo:id/editor_title")))
    el2.click()
    el2.send_keys("Ini Namanya Note")

    el3 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.samsung.android.app.memo:id/editText1")))
    el3.click()
    el3.send_keys("Ini dia isi notenya, singkat padat yang penting ada isinya.")

    driver.execute_script('mobile: hideKeyboard')

    el4 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Save")))
    el4.click()

    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create memo")))

    driver.terminate_app("com.samsung.android.app.memo")

    print("Pass")

def test_search_memo(driver):
    wait = WebDriverWait(driver, 10)  # Tunggu maksimal 10 detik

    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search")))
    el5.click()

    el6 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/search_src_text")))
    el6.click()
    el6.send_keys("Ini Namanya Note")

    driver.execute_script('mobile: pressKey', {"keycode": 66})

    el7 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Navigate up")))
    el7.click()

    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create memo")))

    driver.terminate_app("com.samsung.android.app.memo")

    print("Pass")


def test_edit_memo(driver):
    wait = WebDriverWait(driver, 10)  # Tunggu maksimal 10 detik

    el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.RelativeLayout\").instance(1)")))
    el1.click()

    el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.samsung.android.app.memo:id/title")))
    el2.click()

    el3 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.samsung.android.app.memo:id/editor_title")))
    el3.click()
    el3.clear()
    el3.send_keys("Tutorial Ngonten Tanpa Bosen")

    el4 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.samsung.android.app.memo:id/editText1")))
    el4.click()
    el4.clear()
    el4.send_keys("Ya jangan bosen. Udah itu aja.")

    driver.execute_script('mobile: hideKeyboard')

    el4 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Save")))
    el4.click()

    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create memo")))

    driver.terminate_app("com.samsung.android.app.memo")

    print("Pass")


def test_delete_memo(driver):
    wait = WebDriverWait(driver, 10)  # Tunggu maksimal 10 detik

    el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.RelativeLayout\").instance(1)")))
    actions = ActionChains(driver)
    actions.w3c_actions.pointer_action.move_to(el1) # Arahkan ke elemen
    actions.w3c_actions.pointer_action.pointer_down() # Tap elemen
    actions.pause(2) # Hold 2 detik
    actions.w3c_actions.pointer_action.pointer_up() # Lepas
    actions.perform() # Jalankan action

    el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Delete")))
    el2.click()

    el3 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1")))
    el3.click()

    el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create memo")))

    driver.terminate_app("com.samsung.android.app.memo")

    print("Pass")