"""Utility class providing common mobile gestures like swipe and tap."""

from appium.webdriver.common.touch_action import TouchAction
from utilities.logger import Logger


class MobileGestures:
    """Common reusable gestures for mobile automation."""

    logger = Logger.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.action = TouchAction(driver)

    def swipe_up(self, duration=800):
        """Swipe up on the screen."""
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2

        self.logger.info("Performing swipe up gesture")
        self.action.press(x=start_x, y=start_y).wait(duration).move_to(x=start_x, y=end_y).release().perform()

    def swipe_down(self, duration=800):
        """Swipe down on the screen."""
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8

        self.logger.info("Performing swipe down gesture")
        self.action.press(x=start_x, y=start_y).wait(duration).move_to(x=start_x, y=end_y).release().perform()

    def tap(self, x, y):
        """Tap at specific screen coordinates."""
        self.logger.info(f"Tapping at coordinates ({x}, {y})")
        self.action.tap(x=x, y=y).perform()

    def long_press(self, x, y, duration=2000):
        """Perform a long press gesture."""
        self.logger.info(f"Long pressing at ({x}, {y}) for {duration}ms")
        self.action.long_press(x=x, y=y, duration=duration).release().perform()
