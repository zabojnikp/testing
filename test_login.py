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
    password = selenium.find_element_by_id("id_login-password").send_keys(variables['password'])

def step_2_1_4 (selenium):
    # click log in button
    login = selenium.find_element_by_name("login_submit").click()

def step_2_1_5 (selenium):
    # page contains welcome message
    element = selenium.find_element_by_xpath("//div[@id='messages']//div[@class='alertinner wicon']")
    assert "Welcome back" in element.text

def step_2_1_6 (selenium):
    # page contains logout link
    element = selenium.find_element_by_id("logout_link")
