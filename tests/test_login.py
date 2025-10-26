import allure
import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException, \
    TimeoutException

from pages.dashboardpage import DashboardPage
from pages.loginpage import LoginPage
from utilities.capture_screenshot import CaptureScreenshot
from utilities.read_testdata_file import ReadTestdataFile
from utilities.write_testdata_file import WriteIntoTestDataFile
import utilities.constants as const


class TestLogin:

    # TC1: Verify that the home URL is accessible
    @pytest.mark.tested
    @allure.title("TC1: Verify that the home URL is accessible")
    def test_home_url_is_accessible(self, driver, request):
        # Launching the URL is done from Conftest fixture - driver

        # Defining instance for capture screenshot class
        capture_screen = CaptureScreenshot(driver, request)

        # Defining object for login page
        lp = LoginPage(driver)

        with allure.step("Validating company image in home page"):
            assert lp.is_company_image_visible(), f"Home URL {const.BASE_URL} is not accessible"
            capture_screen.capture_screenshot("Home url is accessible")


    # TC2: Validate presence of login fields
    @pytest.mark.tested
    @allure.title("TC2: Validate presence of login fields")
    def test_login_fields(self, driver, request):
        # Defining instance for capture screenshot class
        capture_screen = CaptureScreenshot(driver, request)

        # Defining object for login page
        lp = LoginPage(driver)

        with allure.step("validating username field"):
            assert lp.is_username_label_visible(), "Username label is not displayed"
            assert lp.is_username_textbox_enabled(), "Username text box is not enabled"
            capture_screen.capture_screenshot("Username_field_validated")

        with allure.step("validating password field"):
            assert lp.is_password_label_visible(), "Password label is not displayed"
            assert lp.is_password_textbox_enabled(), "Password text box is not enabled"
            capture_screen.capture_screenshot("Password_field_validated")

    # TC3: Validating login functionality with valid and invalid credentials
    @pytest.mark.tested
    @allure.title("TC3: Validating login functionality")
    @pytest.mark.parametrize("testcase_name, username, password, expected_condition",
                             ReadTestdataFile.read_testdata_csv("Validating login functionality"))
    def test_login(self, driver, request, testcase_name, username, password, expected_condition):
        """Using Data driven methodology to test login functionality using multiple
         credentials from test data csv file"""

        # Defining instance for capture screenshot class
        capture_screen = CaptureScreenshot(driver, request)
        test_result = "Fail"

        try:
            lp = LoginPage(driver)
            dp = DashboardPage(driver)

            with allure.step("Perform login"):
                lp.perform_login(username, password)
                capture_screen.capture_screenshot("Performing_login")

            with allure.step("Validate login fails for invalid credentials"):
                if expected_condition != "":
                    if username != "" and password != "":
                        actual_error = lp.get_login_error_message()
                        assert actual_error == expected_condition, f"Expected error: {expected_condition}, but actual: {actual_error}"
                    else:
                        actual_error = lp.get_required_error_message()
                        assert actual_error == expected_condition, f"Expected error: {expected_condition}, but actual: {actual_error}"
                    capture_screen.capture_screenshot("Validating_Login_error_message")


                else:
                    with allure.step("Validate login is success for valid credentials"):
                        assert dp.get_dashboard_title_text() == "Dashboard", f"Dashboard page is not loaded"
                        capture_screen.capture_screenshot("Dashboard_displayed")

                        with allure.step("Logout is success"):
                            dp.perform_logout()
                            capture_screen.capture_screenshot("Clicked_logout")

                            # Validate logout is success
                            assert lp.is_company_image_visible(), f"Logout failed"
                            capture_screen.capture_screenshot("Logout_failed")

            test_result = "Pass"  # Test case is executed successfully

        except (
                NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException,
                TimeoutException) as e:
            capture_screen.capture_screenshot("Testcase_failed")
            pytest.fail(f"Test failed due to Selenium exception: {e}")

        finally:
            WriteIntoTestDataFile.write_test_result(testcase_name, username, password, expected_condition, test_result)

    @pytest.mark.tested
    @allure.title("TC7: Verify Forgot Password link functionality")
    def test_forgot_password(self, driver, request):

        #Define objects for capture screenshot, login pages
        lp = LoginPage(driver)
        capture_screen = CaptureScreenshot(driver, request)

        with allure.step("Click on Forgot Password"):
            lp.click_forgot_password()
            capture_screen.capture_screenshot("Clicking_on_forgot_password")

        with allure.step("Submit reset password"):
            expected_title = const.FP_TITLE_TEXT
            actual_title = lp.get_fp_title_text()
            assert actual_title == expected_title, f"Expected: {expected_title} and actual is: {actual_title}"

            lp.enter_fp_username(const.ADMIN_USERNAME)
            lp.click_reset_password_button()
            capture_screen.capture_screenshot("Submit_reset_password")

        with allure.step("Validate reset password confirmation message"):
            assert lp.is_reset_password_sent_visible(), f"Reset password link sent message is not visible"
            capture_screen.capture_screenshot("Validate_password_reset_link_sent")




