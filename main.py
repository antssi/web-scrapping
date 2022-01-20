import requests
import re
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

response = requests.get('https://habr.com/ru/all/', headers=headers)
res = response.text
soup = BeautifulSoup(res, 'html.parser')

posts = []
for p in soup.find_all('article', class_="tm-articles-list__item"):
    header = p.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2").text
    link = URL + p.find('a', class_="tm-article-snippet__title-link")['href']
    data = p.find('time')['title']
    description = p.find('div', class_="article-formatted-body").text
    snippet = p.find('span', class_="tm-article-snippet__hubs-item").text

    posts.append(
        {"header": header,
         "link": link,
         "data": data,
         "description": description,
         "snippet": snippet}
)

for post in posts:
    for word in KEYWORDS:
        pattern = re.compile(word, flags=re.IGNORECASE)
        if pattern.search (post['header']) or pattern.search(post['description']) or pattern.search(post['snippet']):
            print(f'Слово "{word}" найдено в посте:')
            print(post['data'], ' - ', post['header'], ' - ', post['link'])