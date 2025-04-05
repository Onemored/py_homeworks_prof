import json
import time
from pprint import pprint
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
options = ChromeOptions()
options.add_argument('--headless')
browser = Chrome(service=service, options=options)
# browser = Chrome(service=service)


def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None


browser.get('https://dtf.ru/games')

time.sleep(3)

# article_list = soup.find_all('div', class_='content--short')
article_list = browser.find_elements(by=By.CLASS_NAME, value='content--short')
time.sleep(3)

links = []
for article in article_list:
    #     article_link = ('https://dtf.ru/games' +
    #                     article.find('a', class_='content__link')['href'])
    #     article_link = article.find_element(By.CSS_SELECTOR, value='a.content__link') \
    #         .get_attribute('href')
    #     article_link = WebDriverWait(article, 5).until(
    #         expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'a.content__link'))
    #     ).get_attribute('href')
    article_link = wait_element(article, by=By.CSS_SELECTOR, value='a.content__link') \
        .get_attribute('href')
    links.append(article_link)

parsed_data = []
for link in links:
    # response = requests.get(article_link)
    browser.get(link)

    # soup = bs4.BeautifulSoup(response.text, features='lxml')
    # article_title = soup.find('h1').text.strip()
    article_title = wait_element(browser, by=By.TAG_NAME, value='h1').text

    # article_time = soup.find('time')['datetime']
    article_time = wait_element(browser, by=By.TAG_NAME, value='time') \
        .get_attribute('datetime')

    # article_text = soup.find('article', class_='content__blocks').text.strip()
    article_text = wait_element(browser,
                                by=By.CSS_SELECTOR, value='article.content__blocks').text

    parsed_data.append({
        'title': article_title,
        'time': article_time,
        'text': article_text,
        'link': article_link,
    })

with open('article2.json', 'w') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)



