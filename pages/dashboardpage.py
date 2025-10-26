import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.basepage import BasePage
from pages.locators import Locators
import utilities.constants as const


class DashboardPage(BasePage):
    def get_dashboard_title_text(self):
        title_text = self.get_element_text(Locators.dashboard_title)
        return title_text

    def perform_logout(self):
        self.click_element(Locators.user_dropdown)
        self.click_element(Locators.logout_option)

    def validate_main_menu_list(self, value):
        web_element = (By.XPATH, f"//a[@class = 'oxd-main-menu-item']/span[text() = '{value}']")
        self.is_element_visible(web_element)
        self.click_element(web_element)

        expected_element = (By.XPATH, f"//h6[text()='{value}']")
        is_visible = self.is_element_visible(expected_element)
        return is_visible

    def select_admin_menu(self):
        self.click_element(Locators.admin_menu_option)

    def click_add_user(self):
        self.click_element(Locators.add_user_button)

    def select_user_role_ess(self):
        self.click_element(Locators.user_role_dropdown)
        self.click_element(Locators.ess_user_role)

    def select_status_enabled(self):
        self.click_element(Locators.status_dropdown)
        self.click_element(Locators.status_enabled)

    def enter_employee_name(self):
        search_name = random.choices(string.ascii_lowercase, k=1)
        self.enter_text(Locators.employee_name_input, search_name)
        const.EMPLOYEE_NAME = self.get_element_text(Locators.employee_name_suggestion_list)
        self.click_element(Locators.employee_name_suggestion_list)

    def re_enter_employee_name(self):
        self.enter_text(Locators.employee_name_input, const.EMPLOYEE_NAME)
        name_element = (By.XPATH, f"//div[@role='listbox']//span[text() = '{const.EMPLOYEE_NAME}']")
        self.click_element(name_element)

    def enter_new_username(self, value):
        self.enter_text(Locators.new_username_input, value)

    def enter_password(self, value):
        self.enter_text(Locators.new_password_input, value)

    def enter_confirm_password(self, value):
        self.enter_text(Locators.confirm_password_input, value)

    def click_save_button(self):
        self.click_element(Locators.save_button)

    def click_user_management(self):
        self.click_element(Locators.user_management_tab)

    def validate_new_user_in_search_list(self, value):
        element_path = (By.XPATH, f"//div[@class = 'oxd-table-cell oxd-padding-cell']//div[text() = '{value}']")
        is_visible = self.is_element_visible(element_path)
        return is_visible

    def click_my_info_menu(self):
        self.click_element(Locators.my_info_menu_option)

    def select_myinfo_submenu_by_value(self, value):
        element = (By.XPATH, f"//div[@role = 'tab']/a[text() = '{value}']")
        self.is_element_visible(element)
        self.click_element(element)

    def get_submenu_title_text(self):
        title_text = self.get_element_text(Locators.my_info_submenu_title)
        return title_text

    def select_leave_menu_option(self):
        self.click_element(Locators.leave_menu_option)

    def select_assign_leave_tab(self):
        self.click_element(Locators.assign_leave_tab)

    def select_leave_type(self):
        self.click_element(Locators.leave_type_dropdown)
        self.click_element(Locators.leave_option)

    #Methods to access claim info.
    def select_claim_main_menu(self):
        self.click_element(Locators.claim_menu_option)

    def select_submit_claim_tab(self):
        self.click_element(Locators.submit_claim_tab)

    def select_event_type(self):
        self.click_element(Locators.event_drop_down)
        const.EVENT_TYPE = self.get_element_text(Locators.event_option)
        self.click_element(Locators.event_option)

    def select_currency(self):
        self.click_element(Locators.currency_drop_down)
        self.scroll_and_click(Locators.currency_option)

    def enter_remarks(self, value):
        self.enter_text(Locators.remarks_input, value)

    def submit_claim_request(self):
        self.click_element(Locators.create_button)

    def is_submit_claim_confirmation_shown(self):
        is_element_visible = self.is_element_visible(Locators.submit_claim_confirmation)
        return is_element_visible

