"""Configuration management for the Appium test automation framework."""

import os
from enum import Enum


class Platform(Enum):
    """Supported mobile platforms."""
    ANDROID = "android"
    IOS = "ios"


class Config:
    """
    Central configuration for Appium + Perfecto test framework.

    Handles environment variables, device settings, and app identifiers.
    """

    # Appium Server (local or Perfecto cloud)
    # Change these URLs depending on where your Appium server runs
    APPIUM_SERVER_URL = os.getenv(
        "APPIUM_SERVER_URL",
        "http://127.0.0.1:4723/wd/hub"   # Default: local Appium
        # Example for Perfecto:
        # "https://<YOUR_CLOUD_NAME>.perfectomobile.com/nexperience/perfectomobile/wd/hub"
    )

    # Perfecto Authentication (if applicable)
    PERFECTO_SECURITY_TOKEN = os.getenv("PERFECTO_SECURITY_TOKEN", "")

    # Platform Selection
    PLATFORM = os.getenv("PLATFORM", Platform.IOS.value)  # or 'android'

    # Timeouts
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    COMMAND_TIMEOUT = int(os.getenv("COMMAND_TIMEOUT", "120"))

    # Android App / Device Info
    ANDROID_APP_PACKAGE = "xyz.digitalbank.demo"
    ANDROID_APP_ACTIVITY = "com.digitalbank.activities.MainActivity"
    ANDROID_DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "R3CW60ABQBB")
    ANDROID_PLATFORM_VERSION = os.getenv("ANDROID_PLATFORM_VERSION", "14")

    # iOS App / Device Info
    IOS_BUNDLE_ID = "demoddbank.perforce.com"
    IOS_DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "iPhone 11")
    IOS_PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "17.3.1")
    IOS_UDID = os.getenv("IOS_UDID", "00008030-001824812E28802E")
    IOS_XCODE_SIGNING_ID = os.getenv("IOS_XCODE_SIGNING_ID", "iPhone Developer")

    # Test Data (example)
    TEST_USERNAME = os.getenv("TEST_USERNAME", "demo_user@example.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "Password123")

    # Directories
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"

    @classmethod
    def get_platform(cls):
        """Return the current platform enum."""
        return Platform(cls.PLATFORM.lower())

    @classmethod
    def is_android(cls):
        """True if running Android tests."""
        return cls.get_platform() == Platform.ANDROID

    @classmethod
    def is_ios(cls):
        """True if running iOS tests."""
        return cls.get_platform() == Platform.IOS
