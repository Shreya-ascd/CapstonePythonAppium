"""Login page object."""

from appium.webdriver.common.appiumby import AppiumBy as By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Login page object for Digital Bank App.

    Contains all locators and methods related to login functionality.
    """

    # Android Locators
    ANDROID_EMAIL_FIELD = (
        By.ID,
        "xyz.digitalbank.demo:id/emailInput"
    )
    ANDROID_PASSWORD_FIELD = (
        By.ID,
        "xyz.digitalbank.demo:id/passwordInput"
    )
    ANDROID_LOGIN_BUTTON = (
        By.ID,
        "xyz.digitalbank.demo:id/login"
    )
    ANDROID_SIGNUP_LINK = (
        By.ID,
        "xyz.digitalbank.demo:id/registerTV"
    )
    ANDROID_ERROR_MESSAGE = (
        By.ID,
        "xyz.digitalbank.demo:id/snackbar_text"
    )
    ANDROID_LOGIN_MENU = (
        By.ID,
        "xyz.digitalbank.demo:id/login"
    )

    # iOS Locators
    IOS_EMAIL_FIELD = (
        By.ACCESSIBILITY_ID,
        "Enter UserName"
    )
    IOS_PASSWORD_FIELD = (
        By.ACCESSIBILITY_ID,
        "Enter Password"
    )
    IOS_LOGIN_BUTTON = (
        By.ACCESSIBILITY_ID,
        "LogIn"
    )
    IOS_SIGNUP_LINK = (
        By.ACCESSIBILITY_ID,
        "New User Registration"
    )
    IOS_ERROR_MESSAGE = (
        By.IOS_PREDICATE,
        "label CONTAINS 'Invalid' OR label CONTAINS 'incorrect'"
    )
    IOS_LOGIN_MENU = (
        By.ACCESSIBILITY_ID,
        "LogIn"
    )

    def __init__(self, driver):
        """
        Initialize LoginPage.

        Args:
            driver (webdriver.Remote): Appium driver instance
        """
        super().__init__(driver)

    def enter_email(self, email):
        """Enter email address in the email field."""
        locator = self.get_locator(
            self.ANDROID_EMAIL_FIELD,
            self.IOS_EMAIL_FIELD
        )
        success = self.actions.send_keys(locator, email)
        if success:
            self.logger.info(f"Entered email: {email}")
        return success

    def enter_password(self, password):
        """Enter password in the password field."""
        locator = self.get_locator(
            self.ANDROID_PASSWORD_FIELD,
            self.IOS_PASSWORD_FIELD
        )
        success = self.actions.send_keys(locator, password)
        if success:
            self.logger.info("Entered password")
        return success

    def click_login_button(self):
        """Click the login button."""
        locator = self.get_locator(
            self.ANDROID_LOGIN_BUTTON,
            self.IOS_LOGIN_BUTTON
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Clicked Login button")
        return success

    def click_signup_link(self):
        """Click the 'Sign Up Here' link."""
        locator = self.get_locator(
            self.ANDROID_SIGNUP_LINK,
            self.IOS_SIGNUP_LINK
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Clicked Sign Up link")
        return success

    def login(self, email, password):
        """Perform complete login flow."""
        self.logger.info(f"Attempting login with email: {email}")

        if not self.enter_email(email):
            return False

        if not self.enter_password(password):
            return False

        if not self.click_login_button():
            return False

        self.actions.hide_keyboard()
        self.logger.info("Login flow completed")
        return True

    def is_error_displayed(self):
        """
        Check if error message is displayed after failed login.

        Returns:
            bool: True if error message is visible, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_ERROR_MESSAGE,
            self.IOS_ERROR_MESSAGE
        )
        is_visible = self.actions.is_visible(locator)
        self.logger.info(f"Error message displayed: {is_visible}")
        return is_visible

    def get_error_message(self):
        """
        Get the text of the displayed error message.

        Returns:
            str: Error message text, or empty string if not visible
        """
        locator = self.get_locator(
            self.ANDROID_ERROR_MESSAGE,
            self.IOS_ERROR_MESSAGE
        )
        message = self.actions.get_text(locator)
        if message:
            self.logger.info(f"Error message text: {message}")
        else:
            self.logger.warning("No error message text found")
        return message or ""

    def navigate_to_login(self):
        """
        Navigate back to the login screen (if logged out or from another page).

        Returns:
            bool: True if navigation successful, False otherwise
        """
        locator = self.get_locator(
            self.ANDROID_LOGIN_MENU,
            self.IOS_LOGIN_MENU
        )
        success = self.actions.click(locator)
        if success:
            self.logger.info("Navigated to login screen")
        else:
            self.logger.warning("Failed to navigate to login screen")
        return success

    def logout(self):
        """
        Perform logout action.

        Returns:
            bool: True if logout was successful, False otherwise.
        """
        try:
            # These are placeholders for logout menu and confirmation
            ANDROID_LOGOUT_BUTTON = (
                By.ID,
                "xyz.digitalbank.demo:id/logout"
            )
            IOS_LOGOUT_BUTTON = (
                By.ACCESSIBILITY_ID,
                "Logout"
            )

            locator = self.get_locator(
                ANDROID_LOGOUT_BUTTON,
                IOS_LOGOUT_BUTTON
            )

            # Tap logout button
            clicked = self.actions.click(locator)
            if not clicked:
                self.logger.warning("Logout button not found or not clickable.")
                return False

            self.logger.info("Clicked Logout button successfully.")

            # Optionally verify that login menu is visible again (post-logout state)
            locator_login_menu = self.get_locator(
                self.ANDROID_LOGIN_MENU,
                self.IOS_LOGIN_MENU
            )
            is_visible = self.actions.is_visible(locator_login_menu)
            self.logger.info(f"Login menu visible after logout: {is_visible}")

            return is_visible
        except Exception as e:
            self.logger.error(f"Logout failed: {e}")
            return False
