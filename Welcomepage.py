"""Unified AccountSummaryPage supporting both Android and iOS, using utilities."""

from appium.webdriver.common.appiumby import AppiumBy
from utilities.mobile_actions import MobileActions
from utilities.mobile_gestures import MobileGestures
from utilities.logger import Logger


class AccountSummaryPage:
    """
    Unified Account Summary Page object for Digital Bank App (Android + iOS).

    All actions go through MobileActions and MobileGestures with proper logging.
    """

    logger = Logger.get_logger(__name__)

    ANDROID_LOCATORS = {
        "welcome_text": (AppiumBy.ID, "xyz.digitalbank.demo:id/welcomeText"),
        "name": (AppiumBy.ID, "xyz.digitalbank.demo:id/name"),
        "account_number_label": (AppiumBy.ID, "xyz.digitalbank.demo:id/accountNumberLabel"),
        "account_number": (AppiumBy.ID, "xyz.digitalbank.demo:id/accountNumber"),
        "account_name_label": (AppiumBy.ID, "xyz.digitalbank.demo:id/accountNameLabel"),
        "account_type_name": (AppiumBy.ID, "xyz.digitalbank.demo:id/accountTypeName"),
        "balance_label": (AppiumBy.ID, "xyz.digitalbank.demo:id/balanceLabel"),
        "balance": (AppiumBy.ID, "xyz.digitalbank.demo:id/balance"),
        "select_account_text": (AppiumBy.ID, "xyz.digitalbank.demo:id/selectAccountText"),
        "dropdown_item": (AppiumBy.ID, "android:id/text1")
    }

    IOS_LOCATORS = {
        "login_button": (AppiumBy.ACCESSIBILITY_ID, "LogIn"),
        "welcome_text": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Welcome"`]'),
        "name": (AppiumBy.ACCESSIBILITY_ID, " Mr. Josh Smith"),
        "account_number_label": (AppiumBy.ACCESSIBILITY_ID, "Account Number:"),
        "account_number": (AppiumBy.ACCESSIBILITY_ID, "486136373"),
        "account_type_label": (AppiumBy.ACCESSIBILITY_ID, "Account Type:"),
        "account_type": (AppiumBy.ACCESSIBILITY_ID, "Individual Savings"),
        "balance_label": (AppiumBy.ACCESSIBILITY_ID, "Balance:"),
        "balance": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "1000393.0"`][1]'),
        "picker_wheel": (AppiumBy.CLASS_NAME, "XCUIElementTypePickerWheel"),
        "amount_entry": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "3000.0"`][2]')
    }

    def __init__(self, driver, platform):
        """
        Initialize the AccountSummaryPage.

        Args:
            driver: Appium driver instance
            platform: 'android' or 'ios'
        """
        self.driver = driver
        self.platform = platform.lower()
        self.actions = MobileActions(driver)
        self.gestures = MobileGestures(driver)
        self.locators = self.IOS_LOCATORS if self.platform == "ios" else self.ANDROID_LOCATORS
        self.logger.info(f"Initialized AccountSummaryPage for platform: {self.platform}")

    def _get_locator(self, name):
        return self.locators[name]

    def click_element(self, name):
        locator = self._get_locator(name)
        self.logger.info(f"Clicking element: {name}")
        return self.actions.click(locator)

    def enter_text(self, name, text):
        locator = self._get_locator(name)
        self.logger.info(f"Entering text '{text}' into element: {name}")
        return self.actions.send_keys(locator, text)

    def select_picker_value(self):
        if self.platform == "ios":
            self.logger.info("Selecting value from picker wheel (iOS)")
            self.click_element("picker_wheel")
            self.click_element("amount_entry")

    def select_account_from_dropdown(self, account_name):
        if self.platform == "android":
            self.logger.info(f"Selecting account from dropdown: {account_name}")
            self.click_element("select_account_text")
            self.click_element("dropdown_item")
            self.actions.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{account_name}")'))

    def verify_transaction(self, label_text, amount_text, balance_text):
        """
        Verify a transaction row based on label, amount, balance.

        Works for both Android and iOS.
        """
        self.logger.info(f"Verifying transaction - Label: {label_text}, Amount: {amount_text}, Balance: {balance_text}")
        if self.platform == "android":
            label = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{label_text}")')
            amount = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{amount_text}")')
            balance = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{balance_text}")')
        else:
            label = (AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypeStaticText[`name == "{label_text}"`][1]')
            amount = (AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypeStaticText[`name == "{amount_text}"`][1]')
            balance = (AppiumBy.ACCESSIBILITY_ID, balance_text)

        self.gestures.swipe_up()
        return all([
            self.click_element(label) if label else True,
            self.click_element(amount) if amount else True,
            self.click_element(balance) if balance else True
        ])
