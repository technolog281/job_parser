import requests
from lxml import html

url = 'https://kurgan.hh.ru/search/vacancy'
params = {'text': 'python junior',
          'items_on_page': 100
          }  # Query Параметры запроса, упрощает URL и работу с ним

session = requests.session()  # Функция автоматически генерирует cookies

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
}  # Заголовки, вытаскиваются из запроса браузера к сайту
# (для Chrome - F12 - Network - Headers - Request Headers)

hh_req = session.get(url, headers=headers, params=params)

parsed = html.fromstring(hh_req.text)

print(parsed.xpath('//div[@data-qa="pager-block"]/span/span/a/@href'))
# Эта хуета при помощи xpath и lxml вытаскивает данные из html, но на hh не работает