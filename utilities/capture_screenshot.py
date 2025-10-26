import time
import allure
from allure_commons.types import AttachmentType


class CaptureScreenshot:

    def __init__(self, driver, request=None):
        """
        driver: WebDriver instance
        request: Pytest request fixture used for HTML report attachment
        """
        self.driver = driver
        self.request = request

    # Attaches the screenshot manually to Allure + pytest-html)
    def capture_screenshot(self, screenshot_name):
        # Attach to Allure
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

        # Get base64 for pytest-html
        screenshot_pytest_html = self.driver.get_screenshot_as_base64()

        # Attach to pytest-html (if available)
        if self.request and hasattr(self.request.node, "rep_call"):
            html_plugin = self.request.config.pluginmanager.getplugin("html")
            extra = getattr(self.request.node.rep_call, "extra", [])
            extra.append(html_plugin.extras.image(screenshot_pytest_html, screenshot_name))
            self.request.node.rep_call.extra = extra

        return screenshot_pytest_html

    # Failure Screenshot - auto called by pytest hook
    @staticmethod
    def capture_screenshot_on_failure(driver, item):
        if driver:
            # Attach to Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Failure_{item.name}_{int(time.time())}",
                attachment_type=AttachmentType.PNG
            )
            # Return base64 for pytest-html
            return driver.get_screenshot_as_base64()
