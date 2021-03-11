import requests
from lxml import html

sof_url = 'https://stackoverflow.com/jobs'
params = {'q': 'python',
          'l': '',
          'pg': 1
          }
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.190 Safari/537.36 '
}

session = requests.session()
sof_req = session.get(sof_url, params=params, headers=headers)

print(sof_req.status_code)

parsed_page = html.fromstring(sof_req.text)

print(parsed_page.xpath('.//div[@class="grid"]/div/h2/a'))

