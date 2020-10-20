import pytest
from selenium import webdriver
from datetime import datetime, date, time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':

        feature_request = item.funcargs['request']

        driver = feature_request.getfixturevalue('browser')
        driver.save_screenshot('/home/aslan/gitProjects/Testing-informsec-/reports/' + timestamp + '.png')

        extra.append(pytest_html.extras.image('/home/aslan/gitProjects/Testing-informsec-/reports/'
                                              + timestamp + '.png'))

        # always add url to report
        extra.append(pytest_html.extras.url('https://itsecurity.ru/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.image('/home/aslan/gitProjects/Testing-informsec-/reports/'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
