import pytest
from test_login import test_case_2 as _login

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium

def test_case_3(selenium, base_url, variables):
    # setup browser
    selenium = selenium
    selenium.get(base_url)

    _login(selenium, base_url, variables)
    display_products(selenium)
    search_product(selenium)
    open_product(selenium)
    add_to_basket(selenium)

def display_products(selenium):
    element = selenium.find_element_by_xpath("//div[@class='page-header action']/h1")
    assert "All products" in element.text

def search_product(selenium):
    element = selenium.find_element_by_id('id_q')
    element.click()
    element.send_keys("Django shirt")
    search = selenium.find_element_by_xpath("//input[@class='btn btn-default']")
    search.click()

def open_product(selenium):
    element = selenium.find_element_by_xpath("//article[@class='product_pod']/h3/a")
    element.click()
    #title of the product
    element = selenium.find_element_by_xpath("//div[@class='col-sm-6 product_main']/h1")
    assert "Django T-shirt" in element.text

    #breadcrumb
    element = selenium.find_element_by_xpath("//ul[@class='breadcrumb']/li[@class='active']")
    assert "Django T-shirt" in element.text

def add_to_basket(selenium):
    element = selenium.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    element.click()

    #confirmation about adding to basket
    element = selenium.find_element_by_xpath("//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]/div[@class='alertinner ']")
    assert "Django T-shirt has been added to your basket." in element.text

    #amount in basket
    element = selenium.find_element_by_xpath("//div[@class='alertinner ']/p[1]")
    assert "Your basket total is now" in element.text

    #view basket
    element = selenium.find_element_by_xpath("//div[@class='alertinner ']/p[2]/a[@class='btn btn-info'][1]")
    assert "View basket" in element.text

    #checkout basket
    element = selenium.find_element_by_xpath("//div[@class='alertinner ']/p[2]/a[@class='btn btn-info'][2]")
    assert "Checkout now" in element.text
