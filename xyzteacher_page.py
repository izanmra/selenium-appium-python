from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

class TeacherPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    tool_bar = (By.XPATH, '//*[@id="root"]/div[2]/nav')
    login_entry_point = (By.XPATH, "//a[contains(text(), 'Masuk')]")
    email_field = (By.NAME, 'email')
    password_field = (By.NAME, 'password')
    login_button = (By.XPATH, '//button[@type="submit"]')
    profile_picture = (By.CSS_SELECTOR, "button.rounded-full .rounded-full")
    logout_button = (By.CSS_SELECTOR, 'div.text-red-500 svg.lucide-log-out')
    student_management = (By.XPATH, '//nav[@aria-label="Main"]')
    classes = (By.XPATH, '//a[@class="flex items-center gap-2 p-2 rounded-md hover:bg-accent"]//span[contains(text(),"Kelas")]')
    students = (By.XPATH, '//a[@class="flex items-center gap-2 p-2 rounded-md hover:bg-accent"]//span[contains(text(),"Siswa")]')
    create_new_class_button = (By.XPATH, "//button[contains(text(), 'Tambah Kelas')]")
    create_new_student_button = (By.XPATH, "//button[contains(text(), 'Tambah Siswa')]")
    student_name = (By.NAME, 'name')
    nis = (By.NAME, 'nis')
    date_picker = (By.XPATH, '(//button[@role="combobox" and contains(@class, "flex h-10 w-full")])[1]')
    month_picker = (By.XPATH, '(//button[@role="combobox" and contains(@class, "flex h-10 w-full")])[2]')
    year_picker = (By.XPATH, '(//button[@role="combobox" and contains(@class, "flex h-10 w-full")])[3]')
    gender_picker = (By.XPATH, '(//button[@role="combobox" and contains(@class, "flex h-10 w-full")])[4]')
    class_picker = (By.XPATH, '(//button[@role="combobox" and contains(@class, "flex h-10 w-full")])[5]')
    address_field = (By.NAME, 'address')
    orang_tua = (By.NAME, 'parent_name')
    nomor_orang_tua = (By.NAME, 'phone_number')
    save_new_student_button = (By.XPATH, '//button[@type="submit"]')
    class_name = (By.XPATH, '//input[@id=":r10:-form-item"]')
    class_stage = (By.XPATH, '//input[@id=":r11:-form-item"]')
    class_description = (By.TAG_NAME, 'textarea')
    save_new_class_button = (By.XPATH, '//button[normalize-space()="Simpan"]')

    # Methods
    def standby(self):
        self.wait.until(EC.element_to_be_clickable(self.tool_bar))
        time.sleep(0.3)

    def click_login_entry_point(self):
        self.wait.until(EC.element_to_be_clickable(self.login_entry_point)).click()
        time.sleep(0.3)

    def input_email(self, eml):
        self.wait.until(EC.visibility_of_element_located(self.email_field)).send_keys(eml)
        time.sleep(0.3)

    def input_password(self, pw):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(pw)
        time.sleep(0.3)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def click_profile_picture(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_picture)).click()
        time.sleep(0.3)

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
        time.sleep(0.3)

    def click_student_management(self):
        self.wait.until(EC.element_to_be_clickable(self.student_management)).click()

    def click_classes(self):
        self.wait.until(EC.element_to_be_clickable(self.classes)).click()

    def click_students(self):
        self.wait.until(EC.element_to_be_clickable(self.students)).click()

    def create_new_class(self):
        self.wait.until(EC.element_to_be_clickable(self.create_new_class_button)).click()

    def create_new_student(self):
        self.wait.until(EC.element_to_be_clickable(self.create_new_student_button)).click()
        time.sleep(0.4)

    def input_class_name(self, class_name):
        self.wait.until(EC.visibility_of_element_located(self.class_name)).send_keys(class_name)

    def input_class_stage(self, stage):
        self.wait.until(EC.visibility_of_element_located(self.class_stage)).send_keys(stage)

    def input_student_name(self, nama):
        self.wait.until(EC.visibility_of_element_located(self.student_name)).send_keys(nama)
        time.sleep(0.2)

    def input_class_description(self, description):
        self.wait.until(EC.visibility_of_element_located(self.class_description)).send_keys(description)

    def input_student_nis(self, number):
        self.wait.until(EC.visibility_of_element_located(self.nis)).send_keys(number)
        time.sleep(0.3)

    def click_blank_area(self):
        self.wait.until(EC.element_to_be_clickable(self.blank_area)).click()

    def select_date_of_birth(self, date_input):
        date_map = {date: str(date) for date in range(1, 31)}

        if isinstance(date_input, int):
            date_value = date_map.get(date_input)
        else:
            date_value = str(date_input)

        if not date_value:
            raise ValueError("Input tanggal tidak valid")

        time.sleep(0.3)

        # Pastikan dropdown dibuka setiap saat fungsi ini dipanggil
        dropdown_button = self.wait.until(EC.element_to_be_clickable((self.date_picker)))
        dropdown_button.click()

        # (Opsional) Kasih jeda kecil biar dropdownnya betul-betul kebuka
        time.sleep(0.3)  # Bisa dikurangi/ditambah sesuai performa UI

        # Klik tahun yang dipilih
        option_xpath = f'//*[normalize-space(text())="{date_value}" and not(self::option)]'
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

        time.sleep(0.3)

    def select_month_of_birth(self, month_input):
        # Map angka ke nama bulan
        month_map = {
            1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
            5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
            9: "September", 10: "Oktober", 11: "November", 12: "Desember"
        }

        if isinstance(month_input, int):
            month_name = month_map.get(month_input)
        else:
            month_name = str(month_input).capitalize()

        if not month_name:
            raise ValueError("Input bulan tidak valid")

        # Klik tombol dropdown
        dropdown_button = self.wait.until(EC.element_to_be_clickable((self.month_picker)))
        dropdown_button.click()

        time.sleep(0.3)

        # Cari dan klik elemen visual bulan
        # (asumsi elemen visual bulan adalah <div> atau <li>)
        option_xpath = f'//*[normalize-space(text())="{month_name}" and not(self::option)]'
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

        time.sleep(0.3)

    def select_year_of_birth(self, year_input):
        year_map = {year: str(year) for year in range(1945, 2046)}

        if isinstance(year_input, int):
            year_value = year_map.get(year_input)
        else:
            year_value = str(year_input)

        if not year_value:
            raise ValueError("Input tahun tidak valid")

        # Pastikan dropdown dibuka setiap saat fungsi ini dipanggil
        dropdown_button = self.wait.until(EC.element_to_be_clickable((self.year_picker)))
        dropdown_button.click()

        # (Opsional) Kasih jeda kecil biar dropdownnya betul-betul kebuka
        time.sleep(0.3)  # Bisa dikurangi/ditambah sesuai performa UI

        # Klik tahun yang dipilih
        option_xpath = f'//*[normalize-space(text())="{year_value}" and not(self::option)]'
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

        time.sleep(0.3)

    def select_gender(self, gender_input):
        """
        Memilih jenis kelamin dari dropdown dengan lebih cepat.

        Args:
            gender_input (str): "Laki-laki" atau "Perempuan"
        """
        normalized_gender = str(gender_input).capitalize()

        if normalized_gender == "Laki-laki":
            return  # Skip jika default

        if normalized_gender not in ["Laki-laki", "Perempuan"]:
            raise ValueError("Input harus 'Laki-laki' atau 'Perempuan'")

        # Optimasi 1: Gunakan JavaScript untuk membuka dropdown (lebih cepat dari click())
        dropdown = self.wait.until(EC.presence_of_element_located((self.gender_picker)))
        self.driver.execute_script("arguments[0].click();", dropdown)

        time.sleep(0.3)

        # Optimasi 2: Gunakan Expected Condition khusus untuk opsi dropdown
        option_xpath = f'//*[normalize-space()="{normalized_gender}" and @role="option"]'

        # Tunggu sampai opsi benar-benar interactable (bukan hanya visible)
        option = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )

        # Optimasi 3: Langsung klik via JavaScript (bypass animasi/rendering)
        self.driver.execute_script("arguments[0].click();", option)

        time.sleep(0.3)

    def select_class(self, class_name):
        """
        Memilih kelas dari dropdown.

        Args:
            class_name (str): Nama kelas yang ingin dipilih (contoh: "Kelas 7.6")
        """
        # Normalisasi input (trim whitespace dan pastikan string)
        normalized_class = str(class_name).strip()

        if not normalized_class:
            raise ValueError("Nama kelas tidak boleh kosong")

        # 1. Buka dropdown kelas dengan JavaScript (lebih cepat)
        dropdown = self.wait.until(EC.presence_of_element_located((self.class_picker)))
        self.driver.execute_script("arguments[0].click();", dropdown)

        time.sleep(0.3)

        # 2. XPath untuk mencari opsi kelas yang visible dan bisa diklik
        option_xpath = f'//*[normalize-space()="{normalized_class}" and @role="option"]'

        try:
            # Tunggu maksimal 3 detik dan klik via JavaScript
            option = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, option_xpath))
            )
            self.driver.execute_script("arguments[0].click();", option)
        except TimeoutException:
            # Jika tidak ditemukan, tampilkan error informatif
            available_options = self.driver.find_elements(By.XPATH, '//*[@role="option"]')
            available_classes = [opt.text for opt in available_options if opt.text]
            raise ValueError(
                f"Kelas '{normalized_class}' tidak ditemukan. "
                f"Pilihan yang tersedia: {', '.join(available_classes)}"
            )

        time.sleep(0.3)

    def input_address(self, address):
        self.wait.until(EC.visibility_of_element_located(self.address_field)).send_keys(address)
        time.sleep(0.2)

    def input_parent_name(self, nama_orang_tua):
        self.wait.until(EC.visibility_of_element_located(self.orang_tua)).send_keys(nama_orang_tua)
        time.sleep(0.2)

    def input_parent_phone_number(self, number):
        self.wait.until(EC.visibility_of_element_located(self.nomor_orang_tua)).send_keys(number)
        time.sleep(0.2)

    def save_new_class(self):
        self.wait.until(EC.element_to_be_clickable(self.save_new_class_button)).click()
        time.sleep(0.2)

    def save_new_student(self):
        self.wait.until(EC.element_to_be_clickable(self.save_new_student_button)).click()
        time.sleep(1.5)