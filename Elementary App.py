# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UiAutomator2",
	"appium:platformName": "Android",
	"appium:platformVersion": "13",
	"appium:deviceName": "emulator-5554",
	"appium:app": "D:/android/elementary.apk",
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(2)

el1 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/newAccountButton")
el1.click()

time.sleep(2)

el2 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/imageView_arrow")
el2.click()

time.sleep(2)

el3 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/editText_search")
el3.click()

time.sleep(2)

el3.send_keys("indonesia")

time.sleep(2)

el4 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/textView_countryName")
el4.click()

time.sleep(2)

el5 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/createAccountButton")
el5.click()

time.sleep(2)

el6 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el6.click()

time.sleep(2)

el7 = driver.find_element(by=AppiumBy.ID, value="android:id/button2")
el7.click()

time.sleep(2)

el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
el8.click()

time.sleep(2)

el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.elementarypos.client:id/custom_variable_layout\").instance(0)")
el9.click()

time.sleep(2)

el10 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.elementarypos.client:id/settingLayout\").instance(1)")
el10.click()

time.sleep(2)

el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(1)")
el11.click()

time.sleep(2)

el12 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/editItemName")
el12.click()

time.sleep(2)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(291, 566)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(291, 566)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(291, 566)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(291, 566)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

el12.send_keys("Kurma")

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(293, 616)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(281, 614)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

el19 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/editItemSku")
el19.click()

el19.send_keys("123")

driver.execute_script('mobile: hideKeyboard')

time.sleep(2)

el15 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/save")
el15.click()

time.sleep(2)

el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el16.click()

time.sleep(2)

el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el17.click()

time.sleep(2)

el18 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.elementarypos.client:id/custom_variable_layout\").instance(0)")
el18.click()

time.sleep(2)

el19 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/buttonReceipt")
el19.click()

time.sleep(2)

el20 = driver.find_element(by=AppiumBy.ID, value="com.elementarypos.client:id/create_receipt")
el20.click()

time.sleep(2)

driver.quit()