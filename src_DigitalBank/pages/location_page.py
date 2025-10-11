from appium.webdriver.common.appiumby import AppiumBy
from config.config import Config


class LocationPage:
    """
    Page Object Model for the 'ATM's NearMe' (Location) screen.
    Works for both Android and iOS based on platform selection.
    """

    def __init__(self, driver):
        self.driver = driver

        # --- Locators (Android) ---
        self.android_locators = {
            "nav_atm_near_me": (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("xyz.digitalbank.demo:id/navigation_bar_item_labels_group").instance(3)',
            ),
            "btn_permission_allow": (
                AppiumBy.ID,
                "com.android.permissioncontroller:id/permission_allow_one_time_button",
            ),
            "checkbox_gps": (AppiumBy.ID, "xyz.digitalbank.demo:id/checkbox1"),
            "checkbox_network": (AppiumBy.ID, "xyz.digitalbank.demo:id/checkbox2"),
            "checkbox_zip": (AppiumBy.ID, "xyz.digitalbank.demo:id/checkbox3"),
            "btn_get_location": (AppiumBy.ACCESSIBILITY_ID, "Get Location"),
            "txt_response": (AppiumBy.ID, "xyz.digitalbank.demo:id/responseTextView"),
            "label_zip_search": (AppiumBy.ID, "xyz.digitalbank.demo:id/atmSearchzip"),
        }

        # --- Locators (iOS) ---
        self.ios_locators = {
            "nav_atm_near_me": (AppiumBy.ACCESSIBILITY_ID, "ATM's NearMe"),
            "btn_permission_allow": (AppiumBy.ACCESSIBILITY_ID, "Allow Once"),
            "checkbox_gps": (AppiumBy.ACCESSIBILITY_ID, "GPS"),
            "checkbox_network": (AppiumBy.ACCESSIBILITY_ID, "Network"),
            "checkbox_zip": (AppiumBy.ACCESSIBILITY_ID, "ZIP"),
            "btn_get_location": (AppiumBy.ACCESSIBILITY_ID, "Get Location"),
            "txt_response": (AppiumBy.ACCESSIBILITY_ID, "responseTextView"),
            "label_zip_search": (AppiumBy.ACCESSIBILITY_ID, "Search by Zip Code"),
        }

    # --- Utility method ---
    def locator(self, name):
        """Return platform-specific locator tuple."""
        if Config.is_android():
            return self.android_locators[name]
        return self.ios_locators[name]

    # --- Actions ---
    def open_atm_near_me_tab(self):
        self.driver.find_element(*self.locator("nav_atm_near_me")).click()

    def allow_permission(self):
        """Handle location permission pop-up if it appears."""
        try:
            self.driver.find_element(*self.locator("btn_permission_allow")).click()
        except Exception:
            pass

    def toggle_gps_checkbox(self):
        self.driver.find_element(*self.locator("checkbox_gps")).click()

    def toggle_network_checkbox(self):
        self.driver.find_element(*self.locator("checkbox_network")).click()

    def toggle_zip_checkbox(self):
        self.driver.find_element(*self.locator("checkbox_zip")).click()

    def click_get_location(self):
        self.driver.find_element(*self.locator("btn_get_location")).click()

    def get_response_text(self):
        return self.driver.find_element(*self.locator("txt_response")).text

    def click_zip_label(self):
        self.driver.find_element(*self.locator("label_zip_search")).click()
