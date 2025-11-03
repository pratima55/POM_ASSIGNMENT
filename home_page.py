from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def add_to_cart(self):
        item1 = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        item1.click()

        item2= self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        item2.click()


    def item_count(self):
        cart_badge = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        cart_count = cart_badge.text
        assert cart_count == "2", f"Expected 2 items in cart, but found {cart_count}"
        print(f"Cart badge shows: {cart_count} items ✓")