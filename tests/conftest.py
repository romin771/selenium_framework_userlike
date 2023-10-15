import pytest
from selenium import webdriver
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    base_url = "https://www.userlike.com/en/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(3)

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
    lp.login("romin.parvardeh@gmail.com", "RominRomin!234!234")
    yield driver


