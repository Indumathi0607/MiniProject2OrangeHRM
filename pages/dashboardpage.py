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


    #Methods to add new user and verify the same
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
        print(f"****************** {const.EMPLOYEE_NAME}")
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


    #Methods to validate My Info sub titles
    def click_my_info_menu(self):
        self.click_element(Locators.my_info_menu_option)

    def select_myinfo_submenu_by_value(self, value):
        element = (By.XPATH, f"//div[@role = 'tab']/a[text() = '{value}']")
        self.is_element_visible(element)
        self.click_element(element)

    def get_submenu_title_text(self):
        title_text = self.get_element_text(Locators.my_info_submenu_title)
        return title_text

    #Methods to perform leave assignment
    def select_leave_menu_option(self):
        self.click_element(Locators.leave_menu_option)

    def select_assign_leave_tab(self):
        self.click_element(Locators.assign_leave_tab)

    def select_leave_type(self):
        self.click_element(Locators.leave_type_dropdown)
        const.LEAVE_TYPE = self.get_element_text(Locators.leave_option)
        self.click_element(Locators.leave_option)

    def select_from_date(self, no_of_days):
        self.select_date(Locators.from_date,
                         Locators.calendar_view,
                         Locators.current_month_shown_in_calendar,
                         Locators.next_month_arrow, no_of_days)

    def enter_comments_leave(self, text):
        self.enter_text(Locators.comments_input, text)

    def click_assign_button(self):
        self.click_element(Locators.assign_button)

    def is_leave_confirm_popup_shown(self):
        return self.is_element_visible(Locators.confirm_leave_assignment_title)

    def confirm_leave_assignment(self):
        self.click_element(Locators.leave_confirm_ok)

    def select_leave_list_submenu(self):
        self.click_element(Locators.leave_list_submenu)

    def search_for_leave_type(self, leave_type):
        self.click_element(Locators.leave_type_dropdown_leave_list)
        leave_type_element = (By.XPATH, f"//div[@role='listbox']//span[text() = {leave_type}]")
        self.click_element(leave_type_element)

    def click_leave_search_button(self):
        self.click_element(Locators.leave_search_button)

    def get_emp_name_search_result(self):
        return self.get_element_text(Locators.leave_search_result_emp_name).strip()

    def get_leave_type_search_result(self):
        return self.get_element_text(Locators.leave_search_result_type).strip()


    # Methods to access claim info.
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

    def submit_claim_final(self):
        self.click_element(Locators.submit_button)

    def is_submit_claim_confirmation_shown(self):
        is_element_visible = self.is_element_visible(Locators.submit_claim_confirmation)
        return is_element_visible

    def select_my_claims_tab(self):
        self.click_element(Locators.my_claims_tab)

    def click_view_details(self):
        self.scroll_and_click(Locators.view_details_button)

    def is_claim_id_visible(self, value):
        return self.scroll_and_find_by_value(value)

    def get_event_name_from_record(self):
        return self.get_element_text(Locators.event_type_submitted_claim)

    def get_description(self):
        return self.get_element_text(Locators.description_submitted_claim)

    def get_submitted_date(self):
        return self.get_element_text(Locators.submitted_date)
