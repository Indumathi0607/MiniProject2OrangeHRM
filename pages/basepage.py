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
