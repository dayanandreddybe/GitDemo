import os

import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",                # Store the provided string value
        default="chrome",              # Default browser
        help="Browser to use: chrome or firefox"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")


    if browser_name.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("ignore-certificate-errors")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
    elif browser_name.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--ignore-certificate-errors")
        firefox_options.add_argument("--start-maximized")
        firefox_options.add_argument("ignore-certificate-errors")
        firefox_options.add_argument("--incognito")
        driver = webdriver.Firefox(options=firefox_options)
        driver.implicitly_wait(10)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("File name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)

