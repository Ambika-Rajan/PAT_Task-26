from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from imdb_search_page import IMDBSearchPage


class IMDBSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "name_search")
        self.search_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_name(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.name_input)
        ).send_keys(name)

    def click_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed
    driver.get("https://www.imdb.com/search/name/")
    yield driver
    driver.quit()

def test_search_name(setup):
    driver = setup
    search_page = IMDBSearchPage(driver)

    # Step 1: Enter a name in the search box
    search_page.enter_name("Tom Hanks")

    # Step 2: Click the search button
    search_page.click_search()

    # Optional: Verify the search results page loads correctly
    assert "Tom Hanks" in driver.title
