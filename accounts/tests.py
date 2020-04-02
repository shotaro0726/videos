from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.selnium = WebDriver(executable_path='/Users/user/chromedriver')

    @classmethod
    def testDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        username_input = self.selnium.find_element_by_name("login")
        username_input.send_keys('')
        password_input = self.selnium.find_element_by_name("password")
        password_input.send_keys('')
        self.selnium.find_element_by_class_name('btn').click()
