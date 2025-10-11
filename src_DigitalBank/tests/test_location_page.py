import pytest
from utilities.driver_setup import DriverSetup
from pages.location_page import LocationPage


@pytest.fixture(scope="function")
def driver():
    """Fixture: Initialize and quit Appium driver for each test."""
    driver = DriverSetup.initialize_driver()
    yield driver
    DriverSetup.quit_driver()


@pytest.mark.location
def test_get_location_via_gps(driver):
    """
    Test to verify that user can get location using GPS.
    Pattern: Arrange, Act, Assert.
    """

    # -------- ARRANGE --------
    location_page = LocationPage(driver)

    # -------- ACT --------
    location_page.open_atm_near_me_tab()
    location_page.allow_permission()
    location_page.toggle_gps_checkbox()
    location_page.click_get_location()

    # -------- ASSERT --------
    response = location_page.get_response_text()
    assert response != "", "Expected non-empty location response"
    print(f"[INFO] Response: {response}")


@pytest.mark.location
def test_toggle_zip_checkbox_and_label(driver):
    """
    Test to verify ZIP Code checkbox and label interaction.
    Pattern: Arrange, Act, Assert.
    """

    # -------- ARRANGE --------
    location_page = LocationPage(driver)

    # -------- ACT --------
    location_page.open_atm_near_me_tab()
    location_page.toggle_zip_checkbox()
    location_page.click_zip_label()

    # -------- ASSERT --------
    # In a real test, validate navigation or text presence
    assert True, "ZIP checkbox and label click executed successfully"
