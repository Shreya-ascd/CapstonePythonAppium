"""Page Object Model for Deposit Page."""

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DepositPage:
    """Represents the Deposit Page and its actions."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.login_btn = (AppiumBy.ID, "xyz.digitalbank.demo:id/login_button")
        self.dashboard_tab = (AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Dashboard")')
        self.deposit_tab = (AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Deposit")')
        self.debit_option = (AppiumBy.ID, "xyz.digitalbank.demo:id/debit_account")
        self.amount_field = (AppiumBy.ID, "xyz.digitalbank.demo:id/amount")
        self.description_field = (AppiumBy.ID, "xyz.digitalbank.demo:id/description")
        self.submit_button = (AppiumBy.ID, "xyz.digitalbank.demo:id/submit_button")
        self.toast_message = (AppiumBy.XPATH, "//android.widget.Toast[1]")
        self.error_message = (AppiumBy.ID, "xyz.digitalbank.demo:id/error_message")

    # ---------------------- Page Actions ----------------------

    def tap_login(self):
        """Tap on the Login button."""
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_btn))
        login_btn.click()
        print("[ACTION] Tapped Login button")

    def navigate_to_dashboard(self):
        """Navigate to Dashboard tab."""
        dashboard_tab = self.wait.until(EC.element_to_be_clickable(self.dashboard_tab))
        dashboard_tab.click()
        print("[ACTION] Navigated to Dashboard")

    def navigate_to_deposit_tab(self):
        """Navigate to Deposit tab."""
        deposit_tab = self.wait.until(EC.element_to_be_clickable(self.deposit_tab))
        deposit_tab.click()
        print("[ACTION] Navigated to Deposit tab")

    def select_debit(self):
        """Select Debit Account option."""
        debit_option = self.wait.until(EC.element_to_be_clickable(self.debit_option))
        debit_option.click()
        print("[ACTION] Selected debit account")

    def enter_amount(self, amount: str):
        """Enter the deposit amount."""
        field = self.wait.until(EC.element_to_be_clickable(self.amount_field))
        field.clear()
        field.send_keys(amount)
        print(f"[ACTION] Entered amount: {amount}")

    def enter_description(self, description: str):
        """Enter deposit description."""
        field = self.wait.until(EC.element_to_be_clickable(self.description_field))
        field.clear()
        field.send_keys(description)
        print(f"[ACTION] Entered description: {description}")

    def submit_deposit(self):
        """Submit the deposit form."""
        btn = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        btn.click()
        print("[ACTION] Submitted deposit form")

    # ---------------------- Validations ----------------------

    def get_toast_message(self):
        """Fetch toast (success) message text."""
        toast = self.wait.until(EC.presence_of_element_located(self.toast_message))
        toast_text = toast.get_attribute("text")
        print(f"[ASSERTION DATA] Toast message captured: {toast_text}")
        return toast_text

    def get_error_message(self):
        """Fetch error message displayed on screen."""
        try:
            error = self.wait.until(EC.visibility_of_element_located(self.error_message))
            error_text = error.text
            print(f"[ASSERTION DATA] Error message captured: {error_text}")
            return error_text
        except Exception:
            return None
