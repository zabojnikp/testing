import pytest

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium

def test_case_2(selenium, base_url, variables):
    # setup browser
    selenium = selenium
    selenium.get(base_url)

    step_2_1_2(selenium)
    step_2_1_3(selenium, variables)
    step_2_1_4(selenium)
    step_2_1_5(selenium)
    step_2_1_6(selenium)


def step_2_1_2 (selenium):
    # click log in
    element = selenium.find_element_by_id('login_link')
    element.click()

def step_2_1_3 (selenium, variables):
    # input log in details
    username = selenium.find_element_by_id('id_login-username').send_keys(variables['username'])
    password = selenium.find_element_by_id("id_login-password").send_keys(variables['invalid_password'])

def step_2_1_4 (selenium):
    # click log in button
    login = selenium.find_element_by_name("login_submit").click()

def step_2_1_5 (selenium):
    # page contains warning msg 1
    element = selenium.find_element_by_xpath("//form[@id='login_form']/div[@class='alert alert-danger'][1]")
    assert "Oops! We found some errors - please check the error messages below and try again" in element.text
    # page contains warning msg 2
    element = selenium.find_element_by_xpath("//form[@id='login_form']/div[@class='alert alert-danger'][2]")
    assert "Please enter a correct username and password. Note that both fields may be case-sensitive." in element.text

def step_2_1_6 (selenium):
    # page contains logout link
    login = selenium.find_element_by_name("login_submit").click()
