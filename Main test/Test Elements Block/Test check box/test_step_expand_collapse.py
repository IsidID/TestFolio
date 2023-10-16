import sys
import time

sys.path.append('/home/runner/work/TestFolio/TestFolio')
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from main import (
    generate_password as passw,
    generate_user_credentials as user,
    generate_fake_address as address,
    generate_full_name as full_name,
    url,
)
from assertions_types import expanded_folders_style, collapsed_folders_style
from utils import get_elements, click_element
from locators import expanded_folders as folders, expand_folders_button as buttons

user_credentials = user()
password = passw()
address1 = address()
address2 = address()
full_name = full_name()

class TestCheckbox:
    @pytest.fixture(scope='class')
    def setup(cls):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        driver.get(url + 'checkbox')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.epic('Checkbox expand testing')
    @allure.title('User can expand and collapse tree step by step')
    @allure.description("User can expand and collapse all levels subfolders step by step")
    def test_expand_collapse_tree(self, setup):
        driver = setup

        with allure.step('Expand the first level tree (Home folder)'):
            click_element(driver, 'xpath', buttons["home_folder"])
            assert expanded_folders_style in get_elements(driver, 'xpath', folders["home_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='First level expanded tree (Home folder)')

        with allure.step('Expand the second level tree (Desktop folder)'):
            click_element(driver, 'xpath', buttons["desktop_folder"])
            assert expanded_folders_style in get_elements(driver, 'xpath', folders["desktop_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Second level expanded tree (Desktop folder)')

        with allure.step('Expand the second level tree (Documents folder)'):
            click_element(driver, 'xpath', buttons["documents_folder"])
            assert expanded_folders_style in get_elements(driver, 'xpath', folders["documents_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Second level expanded tree (Documents folder)')

        with allure.step('Expand the second level tree (Downloads folder)'):
            click_element(driver, 'xpath', buttons["downloads_folder"])
            assert expanded_folders_style in get_elements(driver, 'xpath', folders["downloads_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Second level expanded tree (Downloads folder)')

        with allure.step('Expand the third level tree (WorkSpace folder)'):
            click_element(driver, 'xpath', buttons["workspace_folder"])
            assert expanded_folders_style in get_elements(driver, 'xpath', folders["workspace_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Third level expanded tree (WorkSpace folder)')

        with allure.step('Expand the third level tree (Office folder)'):
            click_element(driver, 'xpath', buttons["office_folder"])
            assert expanded_folders_style in get_elements(driver, 'xpath', folders["office_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Third level expanded tree (Office folder)')

        with allure.step('Collapse the third level tree (Office folder)'):
            click_element(driver, 'xpath', buttons["office_folder"])
            assert collapsed_folders_style in get_elements(driver, 'xpath', folders["office_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Third level collapsed tree (Office folder)')

        with allure.step('Collapse the third level tree (WorkSpace folder)'):
            click_element(driver, 'xpath', buttons["workspace_folder"])
            assert collapsed_folders_style in get_elements(driver, 'xpath', folders["workspace_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Third level collapsed tree (WorkSpace folder)')

        with allure.step('Collapse the second level tree (Downloads folder)'):
            click_element(driver, 'xpath', buttons["downloads_folder"])
            assert collapsed_folders_style in get_elements(driver, 'xpath', folders["downloads_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Second level collapsed tree (Downloads folder)')

        with allure.step('Collapse the second level tree (Documents folder)'):
            click_element(driver, 'xpath', buttons["documents_folder"])
            assert collapsed_folders_style in get_elements(driver, 'xpath', folders["documents_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Second level collapsed tree (Documents folder)')

        with allure.step('Collapse the second level tree (Desktop folder)'):
            click_element(driver, 'xpath', buttons["desktop_folder"])
            assert collapsed_folders_style in get_elements(driver, 'xpath', folders["desktop_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='Second level collapsed tree (Desktop folder)')

        with allure.step('Collapse the first level tree (Home folder)'):
            click_element(driver, 'xpath', buttons["home_folder"])
            assert collapsed_folders_style in get_elements(driver, 'xpath', folders["home_folder"])[0].get_attribute("class")
        allure.attach(driver.get_screenshot_as_png(), name='First level collapsed tree (Home folder)')
