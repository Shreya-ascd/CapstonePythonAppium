"""Page Object Model for Sign-Up Page in the Digital Bank App."""

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage:
    """Encapsulates locators and actions for the Sign-Up Page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # ---------- Locators ----------
        self.sign_up_here_btn = (AppiumBy.ACCESSIBILITY_ID, "Sign Up Here")
        self.first_name_field = (AppiumBy.ACCESSIBILITY_ID, "First Name")
        self.last_name_field = (AppiumBy.ACCESSIBILITY_ID, "Last Name")
        self.email_field = (AppiumBy.ACCESSIBILITY_ID, "Email Address")
        self.password_field = (AppiumBy.ACCESSIBILITY_ID, "Password")
        self.submit_btn = (AppiumBy.ACCESSIBILITY_ID, "Create a new account")
        self.success_message = (
            AppiumBy.XPATH,
            "//android.widget.Toast[@text='Account created successfully']"
        )
        self.error_message = (
            AppiumBy.XPATH,
            "//android.widget.Toast[contains(@text,'Error')]"
        )

    # ---------- Actions ----------
    def tap_sign_up_here(self):
        """Tap on the 'Sign Up Here' button."""
        el = self.wait.until(EC.element_to_be_clickable(self.sign_up_here_btn))
        el.click()
        print("[ACTION] Navigated to Sign-Up page")

    def enter_first_name(self, first_name):
        """Enter First Name."""
        el = self.wait.until(EC.element_to_be_clickable(self.first_name_field))
        el.clear()
        el.send_keys(first_name)
        print(f"[ACTION] Entered First Name: {first_name}")

    def enter_last_name(self, last_name):
        """Enter Last Name."""
        el = self.wait.until(EC.element_to_be_clickable(self.last_name_field))
        el.clear()
        el.send_keys(last_name)
        print(f"[ACTION] Entered Last Name: {last_name}")

    def enter_email(self, email):
        """Enter Email."""
        el = self.wait.until(EC.element_to_be_clickable(self.email_field))
        el.clear()
        el.send_keys(email)
        print(f"[ACTION] Entered Email: {email}")

    def enter_password(self, password):
        """Enter Password."""
        el = self.wait.until(EC.element_to_be_clickable(self.password_field))
        el.clear()
        el.send_keys(password)
        print(f"[ACTION] Entered Password")

    def submit_form(self):
        """Click on Create Account button."""
        el = self.wait.until(EC.element_to_be_clickable(self.submit_btn))
        el.click()
        print("[ACTION] Submitted Sign-Up form")

    # ---------- Validations ----------
    def get_success_message(self):
        """Get success toast message."""
        try:
            toast = self.wait.until(EC.presence_of_element_located(self.success_message))
            toast_text = toast.get_attribute("text")
            print(f"[ASSERTION DATA] Success Toast: {toast_text}")
            return toast_text
        except Exception:
            return ""

    def get_error_message(self):
        """Get error toast message."""
        try:
            toast = self.wait.until(EC.presence_of_element_located(self.error_message))
            toast_text = toast.get_attribute("text")
            print(f"[ASSERTION DATA] Error Toast: {toast_text}")
            return toast_text
        except Exception:
            return ""
