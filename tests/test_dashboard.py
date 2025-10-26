import allure
import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException, \
    TimeoutException

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
import utilities.constants as const


class TestDashboard:

    # TC4: Verify visibility and clickability of main menu items after login
    @pytest.mark.tested
    @allure.title("Verify visibility and clickability of main menu items after login")
    def test_validate_menu_items(self, driver, request):

        # Defining instance for capture screenshot class
        capture_screen = CaptureScreenshot(driver, request)
        lp = LoginPage(driver)
        dp = DashboardPage(driver)

        with allure.step("Perform login"):
            lp.perform_login(const.ADMIN_USERNAME, const.ADMIN_PASSWORD)
            capture_screen.capture_screenshot("Performing_login")

        with allure.step("Validate login is success for valid credentials"):
            assert dp.get_dashboard_title_text() == "Dashboard", f"Dashboard page is not loaded"
            capture_screen.capture_screenshot("Dashboard_displayed")

        with allure.step("Validate each main menu option"):
            #Defining the menu list
            main_menu_list = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]

            #loop the menu list and validate the title for each menu.
            for menu in main_menu_list:
                if menu == "My Info":
                    expected_title = "PIM"
                else:
                    expected_title = menu.strip()

                is_title_visible = dp.validate_main_menu_list(expected_title)
                assert is_title_visible, "Title not visible"
                capture_screen.capture_screenshot(f"{menu}_is_validated")
