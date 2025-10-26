from utilities.constants import BASE_URL

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from utilities.capture_screenshot import CaptureScreenshot


# Using pytest_add option hook method allow browser selection via command line
# The default browser is set to Chrome
# action = "store" this stores the browser name given in commandline
# help text is the explanation shown in the 'pytest --help' output.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browsers supported are: Chrome, Firefox, Edge and Safari(if MACOS)")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()  # Get the browser name from the run command
    driver = None

    # Initialize the webdriver with browser option provided during execution
    if browser == 'chrome':

        #Script to close the chrome native popups, notifications
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-save-password-bubble")  # disable save password popup
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver = (webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install(),  options=options)))  # driver manager install method used to automatically download the correct driver for the given browser.

    elif browser == 'firefox':
        driver = (webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())))

    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    elif browser == 'safari':
        driver = webdriver.Safari()  # this is applicable only for MACOS and the SafariDriver is preinstalled in MAC.

    else:
        raise ValueError(f'Unsupported browser: {browser}')

    # Launch the browser and maximize the window.
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver  # Returns the driver for testcase execution
    driver.quit()  # Closes the browser session after tests execution.


# hook to take screenshot when the testcase fails for Allure and HTML reports.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call':
        # Store result for manual attachment
        setattr(item, "rep_call", rep)

        if rep.failed:
            driver = item.funcargs.get('driver', None)

            # Since the step def are not directly involving the driver fixture, steps to find driver indirectly
            if not driver:
                for fixture_value in item.funcargs.values():
                    if hasattr(fixture_value, 'driver'):
                        driver = fixture_value.driver
                        break

            if driver:
                screenshot_base64= CaptureScreenshot.capture_screenshot_on_failure(driver, item)

                if screenshot_base64:
                    html_plugin = item.config.pluginmanager.getplugin("html")
                    extra = getattr(rep, "extra", [])
                    extra.append(html_plugin.extras.image(screenshot_base64, "Failure Screenshot"))
                    rep.extra = extra


