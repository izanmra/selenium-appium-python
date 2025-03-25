import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from memo_page import MemoPage

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
        "appium:newCommandTimeout": 3600,
        "appium:uiautomator2ServerInstallTimeout": 60000
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_create_new_memo(driver):
    memo_page = MemoPage(driver)
    memo_page.click_create_memo()
    memo_page.enter_memo_title("Ini Namanya Note")
    memo_page.enter_memo_content("Ini dia isi notenya, singkat padat yang penting ada isinya.")
    memo_page.click_save()
    memo_page.standby()
    memo_page.terminate_app()
    print("Test Create Memo: Pass")

def test_search_memo(driver):
    memo_page = MemoPage(driver)
    memo_page.search_memo("Ini Namanya Note")
    memo_page.back_to_home()
    memo_page.standby()
    memo_page.terminate_app()
    print("Test Search Memo: Pass")

def test_edit_memo(driver):
    memo_page = MemoPage(driver)
    memo_page.edit_memo()
    memo_page.click_memo_title()
    memo_page.edit_memo_title("Tutorial Ngonten Tanpa Bosen")
    memo_page.edit_memo_content("Ya jangan bosen. Udah itu aja.")
    memo_page.click_save()
    memo_page.standby()
    memo_page.terminate_app()
    print("Test Edit Memo: Pass")

def test_delete_memo(driver):
    memo_page = MemoPage(driver)
    memo_page.select_memo()
    memo_page.delete_memo()
    memo_page.standby()
    memo_page.terminate_app()
    print("Test Delete Memo: Pass")