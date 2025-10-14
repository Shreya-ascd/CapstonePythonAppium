"""Login feature test cases for Digital Bank App."""

import pytest
from config.config import Config
from pages.login_page import LoginPage
from utilities.logger import Logger
from pages.sign_up import SignupPage

logger = Logger.get_logger(__name__)


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """Test suite for login functionality of Digital Bank App."""

    def test_successful_login(self, driver):
        """
        Test successful login with valid credentials.

        """
        logger.info("Starting test: test_successful_login")

        login_page = LoginPage(driver)

        # Perform login with valid credentials
        assert login_page.login(
            Config.TEST_USERNAME,
            Config.TEST_PASSWORD
        ), "Login failed with valid credentials"

        assert not login_page.is_error_displayed(), \
            "Unexpected error message appeared after valid login"

        logger.info("Test passed: test_successful_login")

    def test_login_with_invalid_credentials(self, driver):
        """
        Test login with invalid credentials.

        Steps:
        1. Navigate to login page
        2. Enter invalid email and password
        3. Click login button
        4. Verify error message is displayed

        Expected Result:
        - Error message should appear
        - Login should not be successful
        """
        logger.info("Starting test: test_login_with_invalid_credentials")

        login_page = LoginPage(driver)

        # Attempt login with invalid credentials
        login_page.login("invalid_user@demo.com", "wrongpassword")

        # Verify error is displayed
        assert login_page.is_error_displayed(), \
            "Error message not displayed for invalid credentials"

        error_message = login_page.get_error_message()
        assert "invalid" in error_message.lower() or "incorrect" in error_message.lower(), \
            f"Unexpected error message: {error_message}"

        logger.info(f"Error message displayed correctly: {error_message}")
        logger.info("Test passed: test_login_with_invalid_credentials")

    def test_login_with_empty_email(self, driver):
        """
        Test login attempt with empty email field.

        Steps:
        1. Navigate to login page
        2. Leave email blank
        3. Enter valid password
        4. Click login button
        5. Verify error message

        Expected Result:
        - Login should fail
        - Error message should be displayed
        """
        logger.info("Starting test: test_login_with_empty_email")

        login_page = LoginPage(driver)

        login_page.navigate_to_login()
        login_page.enter_email("")
        login_page.enter_password(Config.TEST_PASSWORD)
        login_page.click_login_button()

        # Verify error is shown
        assert login_page.is_error_displayed(), \
            "Error message not shown when email is empty"

        error_message = login_page.get_error_message()
        logger.info(f"Error displayed for empty email: {error_message}")

        logger.info("Test passed: test_login_with_empty_email")

    def test_login_with_empty_password(self, driver):
        """
        Test login attempt with empty password field.

        Steps:
        1. Navigate to login page
        2. Enter valid email
        3. Leave password empty
        4. Click login button
        5. Verify error message

        Expected Result:
        - Login should fail
        - Error message should be displayed
        """
        logger.info("Starting test: test_login_with_empty_password")

        login_page = LoginPage(driver)

        login_page.navigate_to_login()
        login_page.enter_email(Config.TEST_USERNAME)
        login_page.enter_password("")
        login_page.click_login_button()

        # Verify error message appears
        assert login_page.is_error_displayed(), \
            "Error message not displayed for empty password"

        logger.info("Test passed: test_login_with_empty_password")

    def test_click_signup_link_navigates_to_signup_page(self, driver):
        """
        Verify that clicking on 'Sign Up Here' link from Login page
        successfully navigates to the Signup page.
        """
        # Initialize the login page
        login_page = LoginPage(driver)
        logger.info("Opened Login Page")

        # Click on 'Sign Up Here' link
        result = login_page.click_signup_link()
        assert result, "Failed to click 'Sign Up Here' link"

        # Validate navigation by checking an element unique to Signup Page
        signup_page = SignupPage(driver)
        is_signup_displayed = signup_page.is_element_visible(signup_page.ANDROID_FIRST_NAME_FIELD)

        # Assertion
        assert is_signup_displayed, "Signup page not displayed after clicking 'Sign Up Here' link"

        logger.info("Successfully navigated to Signup Page after clicking 'Sign Up Here'")

    @pytest.mark.regression
    def test_navigate_to_signup(self, driver):
        """
        Verify navigation from login screen to sign-up screen.

        """

        logger.info("Starting test: test_navigate_to_signup")

        login_page = LoginPage(driver)
        assert login_page.click_signup_link(), \
            "Failed to navigate to Sign Up page"

        logger.info("Test passed: test_navigate_to_signup")