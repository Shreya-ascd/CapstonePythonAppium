"""Test suite for Deposit Page using Page Object Model."""

import pytest
from utilities.driver_setup import DriverSetup
from pages.deposit_page import DepositPage


@pytest.fixture(scope="function")
def driver():
    """Initialize and quit Appium driver for each test."""
    driver = DriverSetup.initialize_driver()
    yield driver
    DriverSetup.quit_driver()


@pytest.mark.deposit
def test_valid_deposit_transaction(driver):
    """Test 1: Valid deposit transaction (Arrange, Act, Assert)."""
    # Arrange
    deposit_page = DepositPage(driver)
    deposit_page.tap_login()
    deposit_page.navigate_to_dashboard()
    deposit_page.navigate_to_deposit_tab()

    # Act
    deposit_page.select_debit()
    deposit_page.enter_amount("500")
    deposit_page.enter_description("Automation deposit")
    deposit_page.submit_deposit()

    # Assert
    success_message = deposit_page.get_toast_message()
    assert "Deposit Successful" in success_message, "Expected success message not shown."


@pytest.mark.deposit
def test_deposit_with_empty_amount(driver):
    """Test 2: Deposit with empty amount (Arrange, Act, Assert)."""
    # Arrange
    deposit_page = DepositPage(driver)
    deposit_page.tap_login()
    deposit_page.navigate_to_dashboard()
    deposit_page.navigate_to_deposit_tab()

    # Act
    deposit_page.select_debit()
    deposit_page.enter_amount("")  # No amount entered
    deposit_page.enter_description("No amount test")
    deposit_page.submit_deposit()

    # Assert
    error_message = deposit_page.get_error_message()
    assert "Please enter an amount" in error_message, "Error for empty amount not shown."


@pytest.mark.deposit
def test_deposit_with_invalid_amount(driver):
    """Test 3: Deposit with invalid amount (non-numeric)."""
    # Arrange
    deposit_page = DepositPage(driver)
    deposit_page.tap_login()
    deposit_page.navigate_to_dashboard()
    deposit_page.navigate_to_deposit_tab()

    # Act
    deposit_page.select_debit()
    deposit_page.enter_amount("abc")  # Invalid input
    deposit_page.enter_description("Invalid amount test")
    deposit_page.submit_deposit()

    # Assert
    error_message = deposit_page.get_error_message()
    assert "Invalid amount" in error_message, "Invalid input validation failed."
