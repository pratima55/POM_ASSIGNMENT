from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")


    def enter_username(self, username):
        USERNAME_FIELD = self.wait.until(EC.element_to_be_clickable(self.username_field)) 
        USERNAME_FIELD.clear()
        USERNAME_FIELD.send_keys(username)


    def enter_password(self,password):
        PASSWORD_FIELD= self.wait.until(EC.element_to_be_clickable(self.password_field))
        PASSWORD_FIELD.clear()
        PASSWORD_FIELD.send_keys(password)


    def click_login(self):
        LOGIN_BUTTON = self.wait.until(EC.element_to_be_clickable(self.login_button))
        LOGIN_BUTTON.click()


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
                 