from appium import webdriver
from location_page import LocationPage

def test_location_flow():
    desired_caps = {
        "platformName": "iOS",
        "appium:platformVersion": "18.1.1",
        "appium:deviceName": "iPhone-11 Pro",
        "appium:automationName": "XCUITest",
        "appium:udid": "00008030-000425101160802E",
	"appium:bundleId": "demoddbank.perforce.com",
	"appium:xcodeSigningId": "iPhone Developer",
	"appium:noReset": "True"
	}

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    page = LocationPage(driver)

    # Perform actions
    page.click_login()
    page.navigate_to_atm_field()
    page.toggle_switch_on()
    page.toggle_first_switch_off()
    page.toggle_second_switch_off()
    page.click_get_location()
    page.enter_zip_code("522614")
    page.click_ok()
    page.click_ok()

    driver.quit()