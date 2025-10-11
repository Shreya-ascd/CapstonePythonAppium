"""Device capabilities configuration for Android and iOS (Perfecto-ready)."""

from config.config import Config


class Capabilities:
    """
    Capabilities manager for Android and iOS devices.
    Supports Perfecto-hosted real devices and local Appium setups.
    """

    @staticmethod
    def get_android_capabilities():
        """
        Get Android device capabilities for Perfecto or local.
        """
        return {
            "platformName": "Android",
            "appium:automationName": "UIAutomator2",
            "appium:platformVersion": Config.ANDROID_PLATFORM_VERSION,
            "appium:deviceName": Config.ANDROID_DEVICE_NAME,
            "appium:deviceId": "R3CW60ABQBB",  # Real device ID in Perfecto
            "appium:appPackage": "xyz.digitalbank.demo",
            "appium:appActivity": "com.digitalbank.activities.MainActivity",  # <-- update if known
            "appium:noReset": True,
            "appium:newCommandTimeout": Config.COMMAND_TIMEOUT,
        }

    @staticmethod
    def get_ios_capabilities():
        """
        Get iOS device capabilities for Perfecto or local.
        """
        return {
            "platformName": "iOS",
            "appium:automationName": "XCUITest",
            "appium:platformVersion": "17.3.1",
            "appium:deviceName": "iPhone 11",
            "appium:udid": "00008030-001824812E28802E",
            "appium:bundleId": "demoddbank.perforce.com",
            "appium:xcodeSigningId": "iPhone Developer",
            "appium:noReset": True,
            "appium:newCommandTimeout": Config.COMMAND_TIMEOUT,
        }

    @staticmethod
    def get_capabilities():
        """Return capabilities based on current platform."""
        if Config.is_android():
            return Capabilities.get_android_capabilities()
        elif Config.is_ios():
            return Capabilities.get_ios_capabilities()
        else:
            raise ValueError("Unsupported platform. Must be 'android' or 'ios'.")
