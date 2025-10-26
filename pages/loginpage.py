from xml.sax.xmlreader import Locator

from pages.basepage import BasePage
from pages.locators import Locators


class LoginPage(BasePage):
    def is_company_image_visible(self):
        return self.is_element_visible(Locators.company_branding_image)

    def is_login_title_visible(self):
        return self.is_element_visible(Locators.login_title)

    def is_username_label_visible(self):
        return self.is_element_visible(Locators.username_title)

    def is_username_textbox_enabled(self):
        return self.is_element_enabled(Locators.username_input)

    def is_password_label_visible(self):
        return self.is_element_visible(Locators.password_title)

    def is_password_textbox_enabled(self):
        return self.is_element_enabled(Locators.password_input)

    def enter_username(self, username):
        self.enter_text(Locators.username_input, username)

    def enter_password(self, password):
        self.enter_text(Locators.password_input, password)

    def click_login_button(self):
        self.click_element(Locators.login_button)

    def get_login_error_message(self):
        error_text = self.get_element_text(Locators.invalid_credentials_message)
        return error_text

    def get_required_error_message(self):
        error_text = self.get_element_text(Locators.required_error_message)
        return error_text

    def click_forgot_password(self):
        self.click_element(Locators.forgot_password_link)

    def perform_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_fp_title_text(self):
        return self.get_element_text(Locators.fp_title_text)

    def enter_fp_username(self, value):
        self.enter_text(Locators.fp_username_input, value)

    def click_reset_password_button(self):
        self.click_element(Locators.fp_reset_password_button)

    def is_reset_password_sent_visible(self):
        web_element = self.is_element_visible(Locators.fp_reset_link_sent_message)
        return web_element