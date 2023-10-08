import sys
sys.path.append('/Users/romanbilokinsky/PycharmProjects/TestFolio')
import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from utils import get_elements, click_element, filling_text, press_tab_key
from main import generate_password as passw, generate_user_credentials as user, generate_short_username, generate_long_username, generate_fake_address as address, generate_full_name as full_name, url, random_email

user = user()
passw = passw()
address1 = address()
address2 = address()
full_name = full_name()

class Test_Text_Box_Form:

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url + 'text-box')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield self.driver
        self.driver.quit()

    @allure.epic('Test text box testing')
    @allure.title('User fill in all fields and submit the form')
    @allure.description('User can fill in the input fields and submit the form')
    def test_positive_text_box(self, setup):
        driver = setup

        with allure.step('Fill the "Full Name" field by generated Username'):
            filling_text(driver, 'css', "input[placeholder='Full Name']", full_name)
        with allure.step('Fill the "Email" field by generated email'):
            filling_text(driver, 'css', "input[placeholder='name@example.com']", random_email)
        with allure.step('Fill the "Current Address" field by generated valid data'):
            filling_text(driver, 'id', 'currentAddress', address1)
        with allure.step('Fill the "Permanent Address" field by generated valid data'):
            filling_text(driver, 'id', 'permanentAddress', address2)
        with allure.step('Click on [Submit]'):
            click_element(driver, 'id', "submit")

        driver.execute_script('window.scrollBy(0, 300);')

        with allure.step('Check the displaying entered Full Name'):
            out_full_name = get_elements(driver, 'id', 'name')[0].text
            out_name = out_full_name.split(':')
            if len(out_name) > 1:
                desired_name = out_name[1].strip()
            assert full_name == desired_name
        with allure.step('Check the displaying entered Email'):
            out_full_email = get_elements(driver, 'id', 'email')[0].text
            out_email = out_full_email.split(':')
            if len(out_email) > 1:
                desired_email = out_email[1].strip()
            assert random_email == desired_email
        with allure.step('Check the displaying entered Current address'):
            if 'currentAddress' in driver.page_source:
                out_full_address1 = get_elements(driver, 'id', 'currentAddress')[0].text
                out_address1 = out_full_address1.split(':')
                if len(out_address1) > 1:
                    desired_address1 = out_address1[1].strip()
                else:
                    desired_address1 = None
            else:
                desired_address1 = None

            if desired_address1 is not None:
                assert address1 == desired_address1
        with allure.step('Check the displaying entered Permanent address'):
            if 'permanentAddress' in driver.page_source:
                out_full_address2 = get_elements(driver, 'id', 'permanentAddress')[0].text
                out_address2 = out_full_address2.split(':')
                if len(out_address2) > 1:
                    desired_address2 = out_address2[1].strip()
                else:
                    desired_address2 = None
            else:
                desired_address2 = None

            if desired_address2 is not None:
                assert address2 == desired_address2

        allure.attach(driver.get_screenshot_as_png(), name='Assertion')
