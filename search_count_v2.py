import requests
from lxml import html
import re

sof_url = 'https://stackoverflow.com/jobs'
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


def search_count(city: str, search_text: str) -> str:
    params = {
        'q': search_text,
        'l': city
    }

    def jobs_counter(params):
        sof_req = session.get(sof_url, params=params, headers=headers)
        parsed_page = html.fromstring(sof_req.text)
        page_count_list = parsed_page.xpath('.//div[@class="grid--cell js-search-title -header seo-header"]/span/text()')
        result = re.findall('([0-9]+)', str(page_count_list))
        full_res = ''.join(result)
        return full_res

    return int(jobs_counter((params)))

# res = search_count(city='',search_text='')
# result = re.findall('([0-9]+)', res)
# full_res = ''.join(result)
# print(full_res)