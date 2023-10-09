import sys
sys.path.append('/home/runner/work/TestFolio/TestFolio')
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import main, utils
from utils import get_elements, click_element, filling_text, press_tab_key
from main import (
    generate_password as passw,
    generate_user_credentials as user,
    generate_short_username,
    generate_long_username,
    generate_fake_address as address,
    generate_full_name as full_name,
    url,
    random_email,
)

user = user()
passw = passw()
address1 = address()
address2 = address()
full_name = full_name()


class Test_Text_Box_Form:
    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Comment this line to open in the browser
        driver = webdriver.Chrome(options=options)
        driver.get(url + 'checkbox')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.epic('Test text box testing')
    @allure.title('User fill in all fields and submit the form')
    @allure.description("User can't submit the form with the wrong email")
    def test_email_field_validation(self, setup):
        driver = setup

        with allure.step('Fill the "Full Name" field by generated Username'):
            filling_text(driver, 'css', "input[placeholder='Full Name']", full_name)
        with allure.step('Fill the "Email" field by the wrong email'):
            filling_text(driver, 'css', "input[placeholder='name@example.com']", 'invalid_email@example')
        with allure.step('Fill the "Current Address" field by generated valid data'):
            filling_text(driver, 'id', 'currentAddress', address1)
        with allure.step('Fill the "Permanent Address" field by generated valid data'):
            filling_text(driver, 'id', 'permanentAddress', address2)
        with allure.step('Click on [Submit]'):
            click_element(driver, 'id', "submit")

        with allure.step('Check the existing field-error in class of the email field'):
            assert "field-error" in get_elements(driver, 'id', 'userEmail')[0].get_attribute("class"), "Class 'field-error' not found in the element's class attribute."

        allure.attach(driver.get_screenshot_as_png(), name='Assertion')
