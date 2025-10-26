import time
import allure
from allure_commons.types import AttachmentType

class CaptureScreenshot:
    def __init__(self, driver, request=None):
        """
        driver: Selenium WebDriver instance
        request: pytest request fixture used for HTML report attachment
        """
        self.driver = driver
        self.request = request

    def capture_screenshot(self, name):
        """Capture screenshot and attach to both Allure and pytest-html"""
        # Capture PNG for Allure
        png = self.driver.get_screenshot_as_png()
        allure.attach(png, name=name, attachment_type=AttachmentType.PNG)

        # Capture Base64 for pytest-html
        screenshot_base64 = self.driver.get_screenshot_as_base64()
        if self.request:
            html_plugin = self.request.config.pluginmanager.getplugin("html")
            extra = getattr(self.request.node.rep_call, "extra", [])
            extra.append(html_plugin.extras.image(screenshot_base64, name))
            self.request.node.rep_call.extra = extra

        return screenshot_base64

    @staticmethod
    def capture_screenshot_on_failure(driver, item):
        """Capture screenshot for pytest hook on failure"""
        name = f"Failure_{item.name}_{int(time.time())}"
        png = driver.get_screenshot_as_png()
        allure.attach(png, name=name, attachment_type=AttachmentType.PNG)
        return driver.get_screenshot_as_base64()
