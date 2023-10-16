import sys
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from main import (
    generate_password as passw,
    generate_user_credentials as user,
    generate_fake_address as address,
    generate_full_name as sample_full_name,
    url,
)
from assertions_types import expanded_folders_style, collapsed_folders_style
from utils import get_elements, click_element
from locators import expanded_folders as folders, expand_folders_button as buttons

class TestCheckbox:
    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Comment this line to open in the browser
        options.add_argument('--window-size=1920x1080')
        driver = webdriver.Chrome(options=options)
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

        def expand_and_assert(button_locator, folder_locator):
            click_element(driver, 'xpath', button_locator)
            assert expanded_folders_style in get_elements(driver, 'xpath', folder_locator)[0].get_attribute("class")

        def collapse_and_assert(button_locator, folder_locator):
            click_element(driver, 'xpath', button_locator)
            assert collapsed_folders_style in get_elements(driver, 'xpath', folder_locator)[0].get_attribute("class")

        with allure.step('Expand and collapse the tree step by step'):
            expand_and_assert(buttons["home_folder"], folders["home_folder"])
            expand_and_assert(buttons["desktop_folder"], folders["desktop_folder"])
            expand_and_assert(buttons["documents_folder"], folders["documents_folder"])
            expand_and_assert(buttons["downloads_folder"], folders["downloads_folder"])
            expand_and_assert(buttons["workspace_folder"], folders["workspace_folder"])
            expand_and_assert(buttons["office_folder"], folders["office_folder"])
            collapse_and_assert(buttons["office_folder"], folders["office_folder"])
            collapse_and_assert(buttons["workspace_folder"], folders["workspace_folder"])
            collapse_and_assert(buttons["downloads_folder"], folders["downloads_folder"])
            collapse_and_assert(buttons["documents_folder"], folders["documents_folder"])
            collapse_and_assert(buttons["desktop_folder"], folders["desktop_folder"])
            collapse_and_assert(buttons["home_folder"], folders["home_folder"])

            # Attach screenshots for each step
            for step_name, button_locator, folder_locator in [
                ('Home folder', buttons["home_folder"], folders["home_folder"]),
                ('Desktop folder', buttons["desktop_folder"], folders["desktop_folder"]),
                ('Documents folder', buttons["documents_folder"], folders["documents_folder"]),
                ('Downloads folder', buttons["downloads_folder"], folders["downloads_folder"]),
                ('Workspace folder', buttons["workspace_folder"], folders["workspace_folder"]),
                ('Office folder', buttons["office_folder"], folders["office_folder"])
            ]:
                allure.attach(driver.get_screenshot_as_png(), name=f'{step_name} screenshot')

# Run the tests
if __name__ == "__main__":
    pytest.main()
