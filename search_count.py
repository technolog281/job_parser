import requests
from lxml import html

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


def search_count(city: str, search_text: str) -> int:
    params = {
        'q': search_text,
        'l': city
    }

    def max_page_counter(params):
        sof_req = session.get(sof_url, params=params, headers=headers)
        parsed_page = html.fromstring(sof_req.text)
        page_count_list = parsed_page.xpath('.//div[@class="s-pagination"]/a/@title')
        if len(page_count_list) == 0:
            return 0
        else:
            return int(str(page_count_list[0])[10:12])

    def extract_hh_jobs(last_page):
        jobs_title_lol = []
        for page in range(last_page):
            print(f'Парсинг страницы {page}')
            result = session.get(sof_url, headers=headers, params=dict(params, pg=page + 1))
            results = html.fromstring(result.text)
            for result in results:
                job_title = result.xpath('.//div[@class="grid"]/div/h2/a/text()')
                jobs_title_lol.append(job_title)
        all = []
        for lst in jobs_title_lol:
            all.extend(lst)
        return len(all)

    return extract_hh_jobs(max_page_counter(params))