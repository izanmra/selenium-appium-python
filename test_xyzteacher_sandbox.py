import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from xyzteacher_page import TeacherPage  # Import class TeacherPage dari file xyzteacher_page.py

@pytest.fixture
def setup_driver():
    # Ganti path ini ke lokasi profil sandbox yang kamu udah setup & isi datanya
    user_data_dir = r"C:\SeleniumProfiles\XYZProfile"
    options = Options()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)  # Supaya browser gak langsung close

    # Inisialisasi driver dengan options
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    driver.get("https://edushine.web.id/")
    yield driver
    driver.quit()

def test_login(setup_driver):
    xyzteacher_page = TeacherPage(setup_driver)
    xyzteacher_page.standby()
    xyzteacher_page.click_login_entry_point()
    xyzteacher_page.input_email('papanem477@ovobri.com')
    xyzteacher_page.input_password('pildunu17')
    xyzteacher_page.click_login_button()
    xyzteacher_page.standby()
    print("Pass")

def test_create_new_class(setup_driver):
    xyzteacher_page = TeacherPage(setup_driver)
    xyzteacher_page.standby()
    xyzteacher_page.click_student_management()
    xyzteacher_page.click_classes()
    xyzteacher_page.create_new_class()
    xyzteacher_page.input_class_name('Kelas 7.7')
    xyzteacher_page.input_class_stage('7')
    xyzteacher_page.input_class_description('Kelas siapa yak')
    xyzteacher_page.save_new_class()
    print("Pass")

def test_create_new_student(setup_driver):
    xyzteacher_page = TeacherPage(setup_driver)
    xyzteacher_page.standby()
    xyzteacher_page.click_student_management()
    xyzteacher_page.click_students()
    xyzteacher_page.create_new_student()
    xyzteacher_page.input_student_name('Anak Cowok')
    xyzteacher_page.input_student_nis('7290207')
    xyzteacher_page.select_date_of_birth("4")
    xyzteacher_page.select_month_of_birth("Maret")
    xyzteacher_page.select_year_of_birth("2016")
    xyzteacher_page.select_gender("Laki-laki")
    xyzteacher_page.select_class("Kelas 7.1")
    xyzteacher_page.input_address('Permata Pamulang Baru')
    xyzteacher_page.input_parent_name('Bapaknya')
    xyzteacher_page.input_parent_phone_number('085618670003')
    xyzteacher_page.save_new_student()
    print("Pass")

def test_logout(setup_driver):
    xyzteacher_page = TeacherPage(setup_driver)
    xyzteacher_page.standby()
    xyzteacher_page.click_profile_picture()
    xyzteacher_page.click_logout()
    xyzteacher_page.standby()
    print("Pass")