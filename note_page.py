from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NotePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    create_note_button = (AppiumBy.ACCESSIBILITY_ID, "New note")
    note_title = (AppiumBy.ID, "com.atomczak.notepat:id/textNoteTitleEdit")
    title_field = (AppiumBy.ID, "com.atomczak.notepat:id/textNoteTitleEdit")
    content_field = (AppiumBy.ID, "com.atomczak.notepat:id/textNoteContentEdit")
    save_button = (AppiumBy.ID, "com.atomczak.notepat:id/action_save_note")
    search_button = (AppiumBy.ACCESSIBILITY_ID, "Search")
    search_input = (AppiumBy.ID, "com.atomczak.notepat:id/search_src_text")
    delete_button = (AppiumBy.ACCESSIBILITY_ID, "Delete")
    confirm_delete_button = (AppiumBy.ID, "android:id/button1")
    navigate_up_button = (AppiumBy.ACCESSIBILITY_ID, "Kembali ke atas")
    back_from_search_result = (AppiumBy.ACCESSIBILITY_ID, "Ciutkan")
    first_note_entry  = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.LinearLayout\").instance(4)")

    # Methods
    def standby(self):
        self.wait.until(EC.element_to_be_clickable(self.create_note_button))

    def click_create_note(self):
        self.wait.until(EC.element_to_be_clickable(self.create_note_button)).click()

    def enter_note_title(self, title):
        el = self.wait.until(EC.element_to_be_clickable(self.title_field))
        el.click()
        el.send_keys(title)

    def click_note_title(self):
        self.wait.until(EC.element_to_be_clickable(self.note_title)).click()

    def edit_note_title(self, title):
        el = self.wait.until(EC.element_to_be_clickable(self.title_field))
        el.click()
        el.clear()
        el.send_keys(title)

    def enter_note_content(self, content):
        el = self.wait.until(EC.element_to_be_clickable(self.content_field))
        el.click()
        el.send_keys(content)

    def edit_note_content(self, content):
        el = self.wait.until(EC.element_to_be_clickable(self.content_field))
        el.click()
        el.clear()
        el.send_keys(content)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def back_to_home(self):
        self.wait.until(EC.element_to_be_clickable(self.navigate_up_button)).click()

    def back_from_search(self):
        self.wait.until(EC.element_to_be_clickable(self.back_from_search_result)).click()

    def search_note(self, query):
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
        search_field = self.wait.until(EC.element_to_be_clickable(self.search_input))
        search_field.click()
        search_field.send_keys(query)
        self.driver.execute_script('mobile: pressKey', {"keycode": 66})  # KeyCode untuk ENTER

    def edit_note(self):
        self.wait.until(EC.element_to_be_clickable(self.first_note_entry)).click()

    def select_note(self):
        el = self.wait.until(EC.element_to_be_clickable(self.first_note_entry))
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to(el)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.pause(2)
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    def delete_note(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.confirm_delete_button)).click()

    def terminate_app(self):
        self.driver.terminate_app("com.atomczak.notepat")