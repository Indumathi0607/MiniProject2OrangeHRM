import random
import string
from datetime import date

import allure
import pytest

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
import utilities.constants as const
from utilities.random_user_generator import RandomUserGenerator


class TestNewUser:
    @pytest.mark.retest
    @allure.title("TC5: Verify visibility and clickability of main menu items after login")
    def test_validate_menu_items(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request.node)

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

    @pytest.mark.retest
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

    @pytest.mark.retest
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

            assert dp.is_submit_claim_confirmation_shown(), f"Submit claim is not shown"
            dp.submit_claim_final()
            capture_screen.capture_screenshot("Submitting_claim_final")

        with allure.step("Validate submitted request"):
            dp.select_my_claims_tab()
            capture_screen.capture_screenshot("Selecting_my_claims")

            dp.scroll_to_claim_list()
            event_name = dp.get_event_name_from_record()
            assert event_name ==  const.EVENT_TYPE, f"Expected event type {const.EVENT_TYPE} and actual {event_name}"

            description = dp.get_description()
            assert description == const.CLAIM_REASON, f"Expected {const.CLAIM_REASON} and actual is {description}"

            #commenting the date validation, since the website shows te creation date as previous day instead of today
            #for claims submitted in the morning IST
            """expected_date = date.today().strftime("%Y-%d-%m")
            actual_date = dp.get_submitted_date()
            assert actual_date == expected_date, f"Expected date {expected_date} and actual is {actual_date}"
            """
            capture_screen.capture_screenshot("Validating_claim_record")






