import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestViceDemoAndroid():
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'appPackage': 'com.vice.viceforandroid',
            'appActivity': 'com.vice.sharedcode.UI.LaunchActivity',
            'platformName': 'Android',
            'deviceName': '1115fbece2ba3503',
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver

    def test_skip(self, driver):
        # Skip the shake feedback dialog
        WebDriverWait(driver, 20).until(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )
        WebDriverWait(driver, 20).until_not(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )

        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "container_skip_btn"))
        )
        skip = driver.find_element_by_id("container_skip_btn")
        skip.click()
        assert not skip.is_displayed()

    def test_watch(self, driver):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "container_skip_btn"))
        )

        # Skip the shake feedback dialog
        WebDriverWait(driver, 20).until(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )
        WebDriverWait(driver, 20).until_not(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )

        skip = driver.find_element_by_id("container_skip_btn")
        skip.click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "nav_watch"))
        )
        watch = driver.find_element_by_id("nav_watch")
        watch.click()
        lede_video_image = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((
                By.ID, "imageview_video_hero_image"))
        )
        assert lede_video_image.is_displayed()

    def test_explore(self, driver):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "container_skip_btn"))
        )

        # Skip the shake feedback dialog
        WebDriverWait(driver, 20).until(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )
        WebDriverWait(driver, 20).until_not(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )

        skip = driver.find_element_by_id("container_skip_btn")
        skip.click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "nav_explore"))
        )
        explore = driver.find_element_by_id("nav_explore")
        explore.click()
        list_heading = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((
                By.ID, "channel_textview_list_heading"))
        )
        assert list_heading.text == "CHANNELS"

    def test_account(self, driver):
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "container_skip_btn"))
        )

        # Skip the shake feedback dialog
        WebDriverWait(driver, 20).until(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )
        WebDriverWait(driver, 20).until_not(
            lambda driver: "instabug_intro_dialog" in driver.page_source
        )

        skip = driver.find_element_by_id("container_skip_btn")
        skip.click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((
                By.ID, "nav_account"))
        )
        account = driver.find_element_by_id("nav_account")
        account.click()
        about_header = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((
                By.ID, "about_section_header"))
        )
        assert about_header.text.upper() == "ABOUT"
        assert about_header.is_displayed()
