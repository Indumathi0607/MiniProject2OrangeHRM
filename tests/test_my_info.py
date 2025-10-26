import allure
import pytest

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
import utilities.constants as const


class TestMyInfo:

    @pytest.mark.tested
    @allure.title("TC8: Validate the presence of menu items under My Info")
    def test_myinfo_menu_items(self, driver, request):
        capture_screen = CaptureScreenshot(driver, request)

        lp = LoginPage(driver)
        dp = DashboardPage(driver)

        with allure.step("Perform login"):
            lp.perform_login(const.ADMIN_USERNAME, const.ADMIN_PASSWORD)
            capture_screen.capture_screenshot("Perform_login")

        with allure.step("Select My Info menu item"):
            dp.click_my_info_menu()

        # Defining list of sub menu items
        sub_menu_dict = {"Personal Details": "Personal Details",
                         "Contact Details": "Contact Details",
                         "Emergency Contacts": "Assigned Emergency Contacts",
                         "Dependents": "Assigned Dependents",
                         "Immigration": "Assigned Immigration Records",
                         "Job": "Job Details",
                         "Salary": "Assigned Salary Components",
                         "Report-to": "Report to",
                         "Qualifications": "Qualifications",
                         "Memberships": "Assigned Memberships"
                         }

        with allure.step("Validating the title of each sub menu under My Info"):
            for menu_name, expected_text in sub_menu_dict.items():
                with allure.step(f"Validate {menu_name} in my info"):
                    dp.select_myinfo_submenu_by_value(menu_name)
                    actual_title = dp.get_submenu_title_text()
                    assert actual_title == expected_text, f"Expected title {expected_text} and actual text is {actual_title}"
                    capture_screen.capture_screenshot("Validating_submenu_title")
