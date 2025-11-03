from selenium import webdriver
from selenium.webdriver.common.by import By



from login_page import LoginPage
from home_page import HomePage
from cart_page import CartPage

driver = webdriver.Chrome()

driver.implicitly_wait(4)

driver.get("https://www.saucedemo.com/")

login = LoginPage(driver)
login.login("standard_user", "secret_sauce")


home= HomePage(driver)
home.add_to_cart()
home.item_count()


cart = CartPage(driver)
cart.click_cart()
cart.item_check()
