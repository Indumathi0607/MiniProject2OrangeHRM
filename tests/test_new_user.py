import random
import string

import allure
import pytest

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
import utilities.constants as const
from utilities.random_user_generator import RandomUserGenerator


class TestNewUser:

    @pytest.mark.smoke
    @allure.title("TC5: Verify visibility and clickability of main menu items after login")
    def test_validate_menu_items(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request)

        lp = LoginPage(driver)
        dp = DashboardPage(driver)
        rg = RandomUserGenerator()

        with allure.step("Perform login"):
            lp.perform_login(const.ADMIN_USERNAME, const.ADMIN_PASSWORD)
            capture_screen.capture_screenshot("Perform_login")

        with allure.step("Navigate to add new user window"):
            dp.select_admin_menu()
            dp.click_add_user()
            capture_screen.capture_screenshot("Clicking_add_user")

        with allure.step("Add new user"):
            dp.select_user_role_ess()
            dp.select_status_enabled()
            dp.enter_employee_name()
            dp.enter_new_username(rg.auto_generate_username())
            dp.enter_password(const.EMPLOYEE_PASSWORD)
            dp.enter_confirm_password(const.EMPLOYEE_PASSWORD)
            dp.click_save_button()
            capture_screen.capture_screenshot("Creating_new_user")

        with allure.step("Login using new user id"):
            dp.perform_logout()
            capture_screen.capture_screenshot("Logout_from_current_user")

            lp.perform_login(const.EMPLOYEE_USERNAME, const.EMPLOYEE_PASSWORD)
            capture_screen.capture_screenshot("Login_with_new_user")

            assert dp.get_dashboard_title_text() == "Dashboard", f"Dashboard page is not loaded"
            capture_screen.capture_screenshot("Dashboard_displayed")

    @pytest.mark.tested
    @allure.title("TC6: Validate the newly created user is listed in the admin user list")
    def test_presence_of_new_user_in_user_list(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request)

        lp = LoginPage(driver)
        dp = DashboardPage(driver)

        with allure.step("Perform login"):
            lp.perform_login(const.ADMIN_USERNAME, const.ADMIN_PASSWORD)
            capture_screen.capture_screenshot("Perform_login")

        with allure.step("Navigate to admin window"):
            dp.select_admin_menu()
            capture_screen.capture_screenshot("Clicking_admin_menu")

        with allure.step("Search for newly added user"):
            dp.enter_new_username(const.EMPLOYEE_USERNAME)
            dp.select_user_role_ess()
            dp.select_status_enabled()
            dp.re_enter_employee_name()
            dp.click_save_button()
            capture_screen.capture_screenshot("Search_for_new_user")

        with allure.step("Verify the newly added user is shown in search result"):
            dp.validate_new_user_in_search_list(const.EMPLOYEE_USERNAME)
            capture_screen.capture_screenshot("Validate_new_user_in_search_list")

    @allure.title("TC10: Initiate a claim request")
    def test_claim_submission(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request)

        lp = LoginPage(driver)
        dp = DashboardPage(driver)

        with allure.step("Perform login"):
            lp.perform_login(const.EMPLOYEE_USERNAME, const.EMPLOYEE_PASSWORD)
            capture_screen.capture_screenshot("Perform_employee_login")

        with allure.step("Select Claims menu item"):
            dp.select_claim_main_menu()
            dp.select_submit_claim_tab()
            dp.select_event_type()
            dp.select_currency()
            dp.enter_remarks(const.CLAIM_REASON)
            dp.submit_claim_request()
            capture_screen.capture_screenshot("Submitting_claim_request")

        with allure.step("Validate submitted request"):
            assert dp.is_submit_claim_confirmation_shown(), f"Submit claim is not shown"


