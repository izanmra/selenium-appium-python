import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from note_page import NotePage

@pytest.fixture(params=[
    {
        "appium:platformVersion": "10",
        "appium:deviceName": "OF5T5XQGXCC6R8CI"
    },
    {
        "appium:platformVersion": "5.0.2",
        "appium:deviceName": "589ff58f"
    }
])
def driver(request):
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:appPackage": "com.atomczak.notepat",
        "appium:appActivity": "com.atomczak.notepat.MainActivity",
        "appium:noReset": True,
        "appium:newCommandTimeout": 3600,
        "appium:uiautomator2ServerInstallTimeout": 60000,
        "appium:platformVersion": request.param["appium:platformVersion"],
        "appium:deviceName": request.param["appium:deviceName"]
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

# Test functions remain the same
def test_create_new_note(driver):
    note_page = NotePage(driver)
    note_page.click_create_note()
    note_page.enter_note_title("Ini Namanya Note")
    note_page.enter_note_content("Ini dia isi notenya, singkat padat yang penting ada isinya.")
    note_page.click_save()
    note_page.back_to_home()
    note_page.standby()
    note_page.terminate_app()
    print(f"Test Create note on {driver.capabilities['deviceName']}: Pass")

def test_search_note(driver):
    note_page = NotePage(driver)
    note_page.search_note("Ini Namanya Note")
    note_page.back_from_search()
    note_page.standby()
    note_page.terminate_app()
    print(f"Test Search note on {driver.capabilities['deviceName']}: Pass")

def test_edit_note(driver):
    note_page = NotePage(driver)
    note_page.edit_note()
    note_page.click_note_title()
    note_page.edit_note_title("Tutorial Ngonten Tanpa Bosen")
    note_page.edit_note_content("Ya jangan bosen. Udah itu aja.")
    note_page.click_save()
    note_page.back_to_home()
    note_page.standby()
    note_page.terminate_app()
    print(f"Test Edit note on {driver.capabilities['deviceName']}: Pass")

def test_delete_note(driver):
    note_page = NotePage(driver)
    note_page.select_note()
    note_page.delete_note()
    note_page.standby()
    note_page.terminate_app()
    print(f"Test Delete note on {driver.capabilities['deviceName']}: Pass")