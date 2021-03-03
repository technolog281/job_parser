import requests
from bs4 import BeautifulSoup

url = 'https://kurgan.hh.ru/search/vacancy'
params = {'text': 'python',
          'items_on_page': 100
          }

session = requests.session()

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.190 Safari/537.36 '
}

hh_req = session.get(url, headers=headers, params=params)  # Запрос к HH.RU страницы с вакансиями

hh_soup = BeautifulSoup(hh_req.text, 'html.parser')  # Вытаскиваем HTML-разметку
page_count = hh_soup.find_all('span', {'class': 'pager-item-not-in-short-range'})  # Находим блок кол-ва страниц

links = []

for page in page_count:
    links.append(int(page.find('a').text))

print(links[-1])
