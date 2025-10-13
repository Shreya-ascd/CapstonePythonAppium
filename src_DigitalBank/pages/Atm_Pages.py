"""ATM page object using MobileActions and MobileGestures utilities."""

from appium.webdriver.common.appiumby import AppiumBy
from utilities.mobile_actions import MobileActions
from utilities.mobile_gestures import MobileGestures
from utilities.logger import Logger


class AtmPage:
    """Page object for ATM features in Digital Bank App."""

    logger = Logger.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.actions = MobileActions(driver)
        self.gestures = MobileGestures(driver)

        # Locators
        self.switch_on = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`value == "1"`]')
        self.switch_off_1 = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`value == "0"`][2]')
        self.switch_off_2 = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`value == "0"`][2]')
        self.get_location_button = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Get Location"`]')
        self.zipcode_field = (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeAlert[`name == "Enter Zip Code"`]'
            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'
            '/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther'
            '/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell'
            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'
        )
        self.ok_button = (AppiumBy.ACCESSIBILITY_ID, "OK")

    # Actions
    def toggle_switch_on(self):
        self.logger.info("Toggling ON switch")
        return self.actions.click(self.switch_on)

    def toggle_switch_off_first(self):
        self.logger.info("Toggling first OFF switch")
        return self.actions.click(self.switch_off_1)

    def toggle_switch_off_second(self):
        self.logger.info("Toggling second OFF switch")
        return self.actions.click(self.switch_off_2)

    def click_get_location(self):
        self.logger.info("Clicking Get Location button")
        self.gestures.swipe_up()
        return self.actions.click(self.get_location_button)

    def enter_zip_code(self, zip_code):
        self.logger.info(f"Entering Zip Code: {zip_code}")
        return self.actions.send_keys(self.zipcode_field, zip_code)

    def click_ok(self):
        self.logger.info("Clicking OK button")
        return self.actions.click(self.ok_button)
