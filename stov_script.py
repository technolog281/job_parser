import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/jobs'
params = {'q': 'python',
          'l': '',
          'pg': 1
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
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.190 Safari/537.36 '
}  # Заголовки, вытаскиваются из запроса браузера к сайту


def max_page_counter():
    sof_req = session.get(url, headers=headers, params=params)  # Запрос к StackOverFlow страницы с вакансиями
    sof_soup = BeautifulSoup(sof_req.text, 'html.parser')  # Вытаскиваем HTML-разметку
    sof_page_count = sof_soup.find_all('a', attrs={'class': 's-pagination--item'})  # Находим блок кол-ва страниц
    links = []
    for page in sof_page_count:
        links.append(page.find('span').text)  # Тянем из всех ссылок текст и форматируем в integer

    return int(links[-2])  # Вернули значение функции


def extract_job(html):  # Собирает все спарсенные куски в словарь
    job_title = html.find('a', {'class': 's-link stretched-link'})
#   link = html.find('a')['href']
#   company_name = html.find('h3', {'class': 'fc-black-700 fs-body1 mb4'})
#   company_name = company_name.strip()  # Strip - удаляет символы в начале и в конце строки
#   job_city = html.find('span', {'span': 'fc-black-500'})
#   job_city = job_city.partition(',')[0]
    return job_title


def extract_hh_jobs(last_page):
    jobs_title = []
    for page in range(1):
        print(f'Парсинг страницы {page}')
        result = session.get(url, headers=headers, params=dict(params, pg=1))
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'grid'})
        for result in results:
            vacancy = extract_job(result)
            jobs_title.append(vacancy)
    return jobs_title
