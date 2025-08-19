from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Base screen get elemnt, click, send keys funksiyalarni va shu kabi narsalarni o'zimiz tuzib olishimiz imkonini beradi
class BaseScreen:  # Base Screenga () kerakmas chunki hech qanday classdan inherit olmaydi

    def __int__(self, driver):
        self.driver = driver   # bu yerga keyingi stepsda foydalandgan
        # driverim yani confestpyni driverini o'ziga o'zlashtirsin degan manoda yozilmoqda

    def click(self, locator): # time.sleep(10) qilsang har biri ko'rinsa ko'rinmasa 10 sec kutadi
        var = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)) # A bu esa element 3 sekunda ko'rinib qosayab tezda klik qivordi
        var.click()

    def enter_data(self, locator, text):
        var = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        var.send_keys(text)

    def get_element_text(self, locator):
        var = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        # Mana shu locatorda joylashgan elamentning paydo bo'lib ko'ringunicha kutib olyabmiz
        # va uni aynan o'sha joyidagi locator bilan qabul qilib olgandan keyin varning textini qaytaryabmiz
        return var.text

    def is_element_visible(self, locator): #Javob ha yoki yo'q 1 yo 0 yo True yoki Falsa bo'lishi kerak
        var = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return bool(var)

    def clear_field(self, locator):
        var = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        var.clear()
