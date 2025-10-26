from datetime import date, timedelta

from selenium.common import NoSuchElementException, TimeoutException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import Locators
from utilities.constants import DEFAULT_TIMEOUT


class BasePage:
    # Constructor to initialize driver, timeout window
    def __init__(self, driver):
        self.driver = driver
        self.timeout = DEFAULT_TIMEOUT

    # Method to wait until the page is ready by executing the Javascript property
    # return document.readyState which returns loading, interactive and complete
    def wait_for_page_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == 'complete'
        )

    # Method to find elements
    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as error:
            assert False, f"Error: {error}"

    # Method to verify the element is visible and return True or False
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    # Method to click on an element
    def click_element(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
        except (ElementNotInteractableException, ElementClickInterceptedException) as error:
            assert False, f"Error: {error}"

    # Method to fill in text in a textbox
    def enter_text(self, locator, value):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(value)
        except (ElementNotInteractableException, ElementClickInterceptedException) as error:
            assert False, f"Error: {error}"

    # Method to get the text value of a given element
    def get_element_text(self, locator):
        try:
            element = self.find_element(locator)
            return element.text
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as error:
            assert False, f"Error: {error}"

    # Method to validate current webpage title
    def validate_webpage_title(self, expected_title):
        webpage_title = self.driver.title
        assert webpage_title == expected_title, f'Title mismatch. Expected {expected_title} and Actual: {webpage_title}'

    # Method to validate current URL
    def validate_current_url(self, expected_url):
        webpage_url = self.driver.current_url
        assert webpage_url == expected_url, f'URL mismatch. Expected {expected_url} and Actual {webpage_url}'

    # Method to switch to iFrame
    def switch_to_iframe(self, frame_id):
        iframe_element = self.find_element(frame_id)
        self.driver.switch_to.frame(iframe_element)

    #Method to check a field is enabled
    def is_element_enabled(self, element_locator):
        is_enabled = self.find_element(element_locator).is_enabled()
        return is_enabled


    #Methiod to scroll and click
    def scroll_and_click(self, locator):
        web_element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(web_element).click().perform()

    #Method to scroll and find
    def scroll_and_find_by_value(self, value):
        locator = (By.XPATH, f"//div[text() = '{value}']")
        web_element = self.driver.find_element(locator)
        ActionChains(self.driver).move_to_element(web_element).release().perform()

        is_visible = self.driver.is_element_visible(web_element)
        return is_visible

    #Method to select date
    def select_date(self, date_field_locator, calendar_locator, month_selected_currently, next_arrow, no_of_days):
        #Getting target date = today + no_of_days
        today = date.today()
        target_date = today + timedelta(days = no_of_days)
        target_day = target_date.day
        target_month = target_date.strftime("%B") #Full month name 'October'
        target_year = target_date.year

        self.click_element(date_field_locator) #open the calendar
        self.find_element(calendar_locator) #wait and find the calendar view is loaded

        # Get displayed month and year
        while True:
            displayed_month_year = self.get_element_text(month_selected_currently)
            displayed_month, displayed_year = displayed_month_year.split()
            displayed_year = int(displayed_year)

            if displayed_month == target_month and displayed_year == target_year:
                break
            else:
                # Click next arrow
               self.click_element(next_arrow)

        # Select the day
        day_xpath = f"//div[contains(@class,'oxd-date-input-calendar')]//div[@role='button' and text()='{target_day}']"
        self.click_element(day_xpath)

        print(f"Selected date: {target_date.strftime('%d-%b-%Y')}")
