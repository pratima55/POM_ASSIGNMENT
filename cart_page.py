from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    def item_check(self):
        cart_items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        assert len(cart_items) == 2, f"Expected 2 items in cart page, but found {len(cart_items)}"

        print(f"Cart page has {len(cart_items)} items ✓")
        print("TEST PASSED: All verifications successful!")