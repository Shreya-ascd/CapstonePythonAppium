"""Test suite for Sign-Up Page using Page Object Model."""

import pytest
from utilities.driver_setup import DriverSetup
from pages.sign_up_page import SignUpPage


@pytest.fixture(scope="function")
def driver():
    """Initialize and quit Appium driver for each test."""
    driver = DriverSetup.initialize_driver()
    yield driver
    DriverSetup.quit_driver()


@pytest.mark.signup
def test_valid_sign_up(driver):
    """Test valid user registration."""
    # Arrange
    sign_up = SignUpPage(driver)
    sign_up.tap_sign_up_here()

    # Act
    sign_up.enter_first_name("Shreya")
    sign_up.enter_last_name("Kumar")
    sign_up.enter_email("shreya.test@example.com")
    sign_up.enter_password("Password123")
    sign_up.submit_form()

    # Assert
    success_text = sign_up.get_success_message()
    assert "Account created" in success_text, f"Expected success message not found. Got: {success_text}"


@pytest.mark.signup
def test_missing_email_field(driver):
    """Test sign-up with missing email field."""
    # Arrange
    sign_up = SignUpPage(driver)
    sign_up.tap_sign_up_here()

    # Act
    sign_up.enter_first_name("John")
    sign_up.enter_last_name("Doe")
    sign_up.enter_password("Password123")
    sign_up.submit_form()

    # Assert
    error_text = sign_up.get_error_message()
    assert "Email required" in error_text or error_text != "", "Expected error for missing email."


@pytest.mark.signup
def test_invalid_email_format(driver):
    """Test invalid email format validation."""
    # Arrange
    sign_up = SignUpPage(driver)
    sign_up.tap_sign_up_here()

    # Act
    sign_up.enter_first_name("Lara")
    sign_up.enter_last_name("Singh")
    sign_up.enter_email("invalid_email_format")
    sign_up.enter_password("Password123")
    sign_up.submit_form()

    # Assert
    error_text = sign_up.get_error_message()
    assert "Invalid email" in error_text or error_text != "", "Expected error for invalid email format."
