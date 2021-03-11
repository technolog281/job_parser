import requests
import pandas
from lxml import html

sof_url = 'https://stackoverflow.com/jobs'
params = {'q': 'python',
          'l': ''
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


def max_page_counter():
    sof_req = session.get(sof_url, params=params, headers=headers)
    parsed_page = html.fromstring(sof_req.text)
    page_count = parsed_page.xpath('.//div[@class="s-pagination"]/a/span/text()')
    return int(page_count[-2])


def extract_job(parse_html):
    jobs_title = parse_html.xpath('.//div[@class="grid"]/div/h2/a/text()')

    return jobs_title


def extract_hh_jobs(last_page):
    jobs_title = []
    for page in range(last_page):
        print(f'Парсинг страницы {page}')
        result = session.get(sof_url, headers=headers, params=dict(params, pg=page+1))
        results = html.fromstring(result.text)
        for result in results:
            list_of_lists = extract_job(result)
            jobs_title.append(list_of_lists)
    return jobs_title


def listmerge(lstst):
    all = []
    for lst in lstst:
        all.extend(lst)
    return all