from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(params=["chrome", "mozillafirefox"], scope="class")
def invoke_driver(request):
    global web_driver      #Precondition of test
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    web_driver.get(
        "https://www.zoho.com/crm/signup.html?servicename=ZohoCRM&serviceurl=https%3A%2F%2Fcrm.zoho.com%2Fcrm"
        "%2FShowHomePage.do%3Fref_value%3Ddirect%253Acrm%257Cdirect%253Acrm%257Cdirect%253Acrm%252Chttps%253A"
        "%252F%252Fwww.zoho.com%252Fcrm%252F%252C%252CDesktop%252Chttps%253A%252F%252Fwww.zoho.com%252Fcrm%252F")
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)   #till here preconditions
    yield   # After this post conditions  // Barcha natijalar olingandan keyin jarayon tugaganda yielddan keyingi ish bajariladi 
    web_driver.close()


