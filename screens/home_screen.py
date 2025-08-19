from .base_screen import  BaseScreen
from selenium.webdriver.common.by import By

class HomeScreen(BaseScreen): #classni ichida har bitta driverni ota klassdan chaqrb olishimiz kerak  // Base screen ota klass sifatida test qilamiz
    # POM ni implement qiladigan joyi yani patterni asosiy ildizi mana shu yerda amalga oshiriladi
    screen_title = (By.XPATH, '//div/h1')
    name_field = (By.XPATH, '//input[@id="namefield"]')
    email_field = (By.XPATH, '//input[@id="email"]')
    password_field = (By.XPATH, '//lable[text()="Create Password"]/following-sibling::input')
    number_field = (By.XPATH, '//input[@id="mobile"]')
    agree_checkbox = (By.XPATH, '//input[@id="tos"]')
    sign_up_button = (By.XPATH, '//input[@id="signupbtn"]')

# Base screenda driverni invoke qilib olgandik endi o'sha ota
# klassida chaqiirib olingan driverni biz invoke qivolamiz

    def __int__(self, driver):
        super().__int__(driver)

    def is_homescreen_title_exist(self):
        self.is_element_visible(self.screen_title)

    def name_enter_data(self):
        self.enter_data(self.name_field, "Irodabonu")

    def email_enter_data(self):
        self.enter_data(self.email_field, "kamilovairodabonu@gmail.com")

    def password_enter_data(self):
        self.enter_data(self.password_field, "Irodabonu2004*")

    def number_enter_data(self):
        self.enter_data(self.number_field, "+99893578178")

    def click_check_box_agree(self):
        self.click(self.agree_checkbox)

    def click_sign_up_button(self):
        self.click(self.sign_up_button)
        print("✅ Success page detected!")


