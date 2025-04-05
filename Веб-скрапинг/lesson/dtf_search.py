import json
import time
from pprint import pprint
from time import sleep
from webbrowser import Chrome

from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_path = ChromeDriverManager().install()
service = Service(executable_path=chrome_path)
browser = Chrome(service=service)


def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None


browser.get('https://dtf.ru/games')

button_search = wait_element(browser, by=By.CSS_SELECTOR, value='button.search__button')
button_search.click()
sleep(3)
field_search = wait_element(browser, by=By.CSS_SELECTOR, value='input.text-input')
field_search.send_keys('pubg')
sleep(3)
field_search.send_keys(Keys.ENTER)
sleep(5)