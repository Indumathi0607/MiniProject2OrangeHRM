import allure
import pytest

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
import utilities.constants as const


class TestLeaveAssignment:

    @pytest.mark.smoke
    @allure.title("TC9: Assign leave to an employee and verify assignment")
    def test_leave_assignment(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request.node)

        lp = LoginPage(driver)
        dp = DashboardPage(driver)

        with allure.step("Perform login"):
            lp.perform_login(const.ADMIN_USERNAME, const.ADMIN_PASSWORD)
            capture_screen.capture_screenshot("Perform_login")

        with allure.step("Select leave menu item"):
            dp.select_leave_menu_option()
            capture_screen.capture_screenshot("Select leave menu option")

        with allure.step("Assign leave to an employee"):
            dp.select_assign_leave_tab()
            dp.enter_employee_name()
            dp.select_leave_type()
            dp.select_from_date(3)
            dp.enter_comments_leave(const.LEAVE_COMMENT)
            dp.click_assign_button()
            capture_screen.capture_screenshot("leave_assignment")

        with allure.step("verify confirmation for leave assignment"):
            assert dp.is_leave_confirm_popup_shown(), f"Leave confirmation is not shown"
            dp.confirm_leave_assignment()
            capture_screen.capture_screenshot("Confirming_leave_assignment")

        with allure.step("Search for leave assignment in leave list"):
            dp.select_leave_list_submenu()
            dp.re_enter_employee_name()
            dp.select_leave_status()
            dp.click_leave_search_button()
            capture_screen.capture_screenshot("Search_for_leave_assignment")

        with allure.step("Verify the leave assignment found in leave list"):

            dp.scroll_to_leave_list()
            leave_type_in_search_result = dp.get_leave_type_search_result()
            emp_name_in_search_result = dp.get_emp_name_search_result()

            assert leave_type_in_search_result == const.LEAVE_TYPE, f"Expected {const.LEAVE_TYPE}, actual {leave_type_in_search_result}"
            assert emp_name_in_search_result == const.EMPLOYEE_NAME, f"Expected {const.EMPLOYEE_NAME}, actual {emp_name_in_search_result}"
            capture_screen.capture_screenshot("Validating_leave_assignment")
