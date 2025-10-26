import allure

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
import utilities.constants as const


class TestLeaveAssignment:

    @allure.title("TC9: Assign leave to an employee and verify assignment")
    def test_leave_assignment(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request)

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
            #yet to add rest of the code.