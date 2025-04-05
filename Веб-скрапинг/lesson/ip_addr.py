# http://jursite.garant.ru/legal-issues/big-data-and-intellectual-property-a-systematic-study-of-scraping-as-part-of-a-common-internet-law-methodology
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/actions_api/test_wheel.py#L11-L14
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/actions_api/test_mouse.py#L24-L27
# https://iqss.github.io/dss-webscrape/filling-in-web-forms.html
# https://stepik.org/course/575/syllabus
# https://htmlacademy.ru/blog/css/selectors


# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install fake_headers
# pip install selenium
# pip install webdriver-manager

import requests
import bs4

from fake_headers import Headers


response = requests.get('https://yandex.ru/internet',
                        headers=Headers(browser='chrome', os='mac').generate())
# with open('index.html', 'w') as f:
#     f.write(response.text)

soup = bs4.BeautifulSoup(response.text, features='lxml')
ul_tag = soup.find('ul', attrs={'class': 'layout__general-info'})
li_tag = ul_tag.find('li')
div_tags = li_tag.find_all('div')
print(div_tags[1].text)