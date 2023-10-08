import sys
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
from utils import get_elements, click_element

user_credentials = user()
password = passw()
address1 = address()
address2 = address()
full_name = full_name()

class TestCheckbox:
    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Comment this line to open in the browser
        driver = webdriver.Chrome(options=options)
        driver.get(url + 'checkbox')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.epic('Checkbox testing')
    @allure.title('User can expand and collapse the tree')
    @allure.description("User can expand all levels subfolders and then collapse them")
    def test_expand_collapse_tree(self, setup):
        driver = setup

        with allure.step('Expand full tree of the folders'):
            click_element(driver, 'xpath', '//button[@aria-label="Expand all"]')

            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.rct-node-leaf'))
            )

            expanded_subfolders = get_elements(driver, 'css', '.rct-node-leaf')
            assert len(expanded_subfolders) > 0
            assert len(expanded_subfolders) == 11

        allure.attach(driver.get_screenshot_as_png(), name='Expanded tree')

        with allure.step('Collapse full tree of the folders'):
            collapse_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Collapse all"]'))
            )
            collapse_button.click()

            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, '.rct-node-leaf'))
            )

            assert not driver.find_elements(By.CSS_SELECTOR, '.rct-node-leaf')

        allure.attach(driver.get_screenshot_as_png(), name='Collapsed tree')
