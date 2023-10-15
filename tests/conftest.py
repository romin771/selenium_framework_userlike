import pytest
from selenium import webdriver
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    if browser == "chrome":
        base_url = "https://www.userlike.com/en/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)
    else:
        baseURL = "https://www.userlike.com/en/"
        driver = webdriver.Firefox()
        driver.get(baseURL)

    #if test class exist
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

@pytest.fixture(scope="class")
def login(request, oneTimeSetUp):
    driver = oneTimeSetUp
    lp = LoginPage(driver)
    lp.login("romin5954@gmail.com", "RominRomin!234!234")
    yield driver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")