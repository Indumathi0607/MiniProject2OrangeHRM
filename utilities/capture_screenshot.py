import time
import allure
from allure_commons.types import AttachmentType

class CaptureScreenshot:
    def __init__(self, driver, item =None):
        #driver: Selenium WebDriver instance
        #item: pytest item to be used in pytest html report later
        self.driver = driver
        self.item = item #Will be used in  pytest_runtest_makereport

        #Initializing a list if not exists
        if item is not None:
            if not hasattr(item, "manual_screenshots"):
                item.manual_screenshots = []

    def capture_screenshot(self, name):
        """Capture screenshot and attach to Allure, and store for pytest-html"""
        png = self.driver.get_screenshot_as_png()
        allure.attach(png, name=name, attachment_type=AttachmentType.PNG)

        # capture Base64 for pytest-html
        screenshot_base64_html_report =  self.driver.get_screenshot_as_base64()

        #store for pytest html report
        if self.item is not None:
            self.item.manual_screenshots.append((name, screenshot_base64_html_report))

        return screenshot_base64_html_report


    @staticmethod
    def capture_screenshot_on_failure(driver, item):
        """Capture screenshot on failure for Allure and HTML reports"""
        name = f"Failure_{item.name}_{int(time.time())}"
        png = driver.get_screenshot_as_png()
        allure.attach(png, name=name, attachment_type=AttachmentType.PNG)

        screenshot_base64_html_report = driver.get_screenshot_as_base64()
        return screenshot_base64_html_report
