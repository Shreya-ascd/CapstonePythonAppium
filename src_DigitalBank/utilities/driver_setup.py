# """Driver setup utility for Appium + Perfecto test automation framework."""
#
# from appium import webdriver
# from config.config import Config
# from config.capabilities import Capabilities
#
#
# class DriverSetup:
#     """
#     Driver setup and management utility.
#
#     - Automatically loads Android/iOS capabilities
#     - Supports local Appium or Perfecto cloud
#     - Handles setup and teardown cleanly
#     """
#
#     driver = None
#
#     @staticmethod
#     def initialize_driver():
#         """Initialize the Appium driver based on Config + Capabilities."""
#         capabilities = Capabilities.get_capabilities()
#
#         # Add Perfecto security token if running on cloud
#         if Config.PERFECTO_SECURITY_TOKEN:
#             capabilities["appium:securityToken"] = Config.PERFECTO_SECURITY_TOKEN
#
#         print(f"[INFO] Launching {Config.PLATFORM} driver...")
#         driver = webdriver.Remote(
#             command_executor=Config.APPIUM_SERVER_URL,
#             desired_capabilities=capabilities
#         )
#
#         driver.implicitly_wait(Config.IMPLICIT_WAIT)
#         DriverSetup.driver = driver
#         return driver
#
#     @staticmethod
#     def get_driver():
#         """Return the existing driver instance or initialize a new one."""
#         if DriverSetup.driver is None:
#             DriverSetup.initialize_driver()
#         return DriverSetup.driver
#
#     @staticmethod
#     def quit_driver():
#         """Terminate the driver session safely."""
#         if DriverSetup.driver:
#             print("[INFO] Quitting Appium driver session...")
#             DriverSetup.driver.quit()
#             DriverSetup.driver = None



"""Driver setup utility for Appium + Perfecto test automation framework."""

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from config.config import Config
from config.capabilities import Capabilities


class DriverSetup:
    """Driver setup and management utility."""

    driver = None

    @staticmethod
    def initialize_driver():
        """Initialize the Appium driver based on Config + Capabilities."""
        capabilities = Capabilities.get_capabilities()

        # Add Perfecto security token if applicable
        if Config.PERFECTO_SECURITY_TOKEN:
            capabilities["appium:securityToken"] = Config.PERFECTO_SECURITY_TOKEN

        print(f"[INFO] Launching {Config.PLATFORM} driver...")

        # Choose correct options class based on platform
        if Config.is_android():
            options = UiAutomator2Options().load_capabilities(capabilities)
        elif Config.is_ios():
            options = XCUITestOptions().load_capabilities(capabilities)
        else:
            raise ValueError("Unsupported platform in Config.")

        driver = webdriver.Remote(
            command_executor=Config.APPIUM_SERVER_URL,
            options=options
        )

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        DriverSetup.driver = driver
        return driver

    @staticmethod
    def get_driver():
        """Return existing driver instance or initialize a new one."""
        if DriverSetup.driver is None:
            DriverSetup.initialize_driver()
        return DriverSetup.driver

    @staticmethod
    def quit_driver():
        """Terminate the driver session safely."""
        if DriverSetup.driver:
            print("[INFO] Quitting Appium driver session...")
            DriverSetup.driver.quit()
            DriverSetup.driver = None
