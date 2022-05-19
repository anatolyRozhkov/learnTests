from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import PageElements
from pytest import mark


@mark.dev
def test_basic():
    # Chrome settings
    chrome_service = Service(executable_path=ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)


    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)



    page = PageElements(driver)
    page.go("https://selenium-python.readthedocs.io/waits.html")
    page.installation_button.perform_click()
