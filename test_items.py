from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


def element_is_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def element_is_present_with_expected_conditions(browser, locator):
    try:
        wait(browser, 10).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        return False
    return True


def test_present_button_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert element_is_present(browser, By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket'), "Element not found"


def test_present_button_add_to_basket_with_expected_conditions(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert element_is_present_with_expected_conditions(browser, (By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket')), \
        "Element not found"
