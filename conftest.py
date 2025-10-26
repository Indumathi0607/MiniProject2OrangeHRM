import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from utilities.constants import BASE_URL
from utilities.capture_screenshot import CaptureScreenshot


# Allow browser selection via CLI
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Supported browsers: chrome, firefox, edge, safari (macOS)")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {"credentials_enable_service": False,
                                                  "profile.password_manager_enabled": False})
        drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        drv = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        drv = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "safari":
        drv = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.get(BASE_URL)
    drv.maximize_window()
    drv.implicitly_wait(5)

    yield drv
    drv.quit()


# Hook to attach screenshots for failures to both Allure and pytest-html
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        setattr(item, "rep_call", rep)
        if rep.failed:
            driver = item.funcargs.get("driver", None)
            if not driver:
                for fixture_value in item.funcargs.values():
                    if hasattr(fixture_value, "driver"):
                        driver = fixture_value.driver
                        break
            if driver:
                try:
                    screenshot_base64 = CaptureScreenshot(driver, request=item.funcargs.get("request")).capture_screenshot(item.name)
                    html_plugin = item.config.pluginmanager.getplugin("html")
                    extra = getattr(rep, "extra", [])
                    extra.append(html_plugin.extras.image(screenshot_base64, "Failure Screenshot"))
                    rep.extra = extra
                except Exception as e:
                    print(f"Failed to capture screenshot for {item.name}: {e}")
