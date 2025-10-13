"""Utility class providing common mobile element actions."""

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from config.config import Config


class MobileActions:
    """Wrapper for common Appium element interactions."""

    logger = Logger.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.IMPLICIT_WAIT)

    # ---------------- Core Actions ----------------
    def find_element(self, locator):
        """Find a single element."""
        by, value = locator
        try:
            self.logger.debug(f"Finding element: {locator}")
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise

    def click(self, locator):
        """Click an element."""
        try:
            element = self.find_element(locator)
            element.click()
            self.logger.info(f"Clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {e}")
            raise

    def send_keys(self, locator, value):
        """Enter text into input field."""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(value)
            self.logger.info(f"Sent keys '{value}' to element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to send keys to element {locator}: {e}")
            raise

    def get_text(self, locator):
        """Get text from an element."""
        try:
            element = self.find_element(locator)
            text = element.text
            self.logger.info(f"Retrieved text from element {locator}: '{text}'")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from element {locator}: {e}")
            raise

    def is_displayed(self, locator):
        """Return True if element is visible."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False
