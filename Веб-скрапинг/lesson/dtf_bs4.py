import json

import requests
import bs4

from fake_headers import Headers

response = requests.get('https://dtf.ru/games',
                        headers=Headers(browser='chrome', os='mac').generate())

soup = bs4.BeautifulSoup(response.text, features='lxml')
none_tag = soup.find('h1', class_='h111111')
article_list = soup.find_all('div', class_='content--short')
# article_list = soup.find_all('div', attrs={'class': 'content--short'})
# article_list = soup.select('div.content--short')

parsed_data = []
for article in article_list:
    article_link = ('https://dtf.ru/games' +
                    article.find('a', class_='content__link')['href'])

    response = requests.get(article_link)
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    article_title = soup.find('h1').text.strip()
    article_time = soup.find('time')['datetime']
    article_text = soup.find('article', class_='content__blocks').text.strip()
    parsed_data.append({
        'title': article_title,
        'time': article_time,
        'text': article_text,
        'link': article_link,
    })

with open('article.json', 'w') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)

