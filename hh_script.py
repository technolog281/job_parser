# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://kurgan.hh.ru/search/vacancy'
# params = {'text': 'python',
#           'items_on_page': 100,
#           'page': 0
#           }  # Query Параметры запроса, упрощает URL и работу с ним
#
# session = requests.session()  # Функция автоматически генерирует cookies
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
#               'application/signed-exchange;v=b3;q=0.9',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'en-RU,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
#     'cache-control': 'max-age=0',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/88.0.4324.190 Safari/537.36 '
# }  # Заголовки, вытаскиваются из запроса браузера к сайту
#
#
# # (для Chrome - F12 - Network - Headers - Request Headers)
#
# def max_page_counter():
#     hh_req = session.get(url, headers=headers, params=params)  # Запрос к HH.RU страницы с вакансиями
#
#     hh_soup = BeautifulSoup(hh_req.text, 'html.parser')  # Вытаскиваем HTML-разметку
#     page_count = hh_soup.find_all('span', {'class': 'pager-item-not-in-short-range'})  # Находим блок кол-ва страниц
#
#     links = []
#
#     for page in page_count:
#         links.append(int(page.find('a').text))  # Тянем из всех ссылок текст и форматируем в integer
#
#     return links[-1]  # Вернули значение функции
#
#
# def extract_job(html):  # Собирает все спарсенные куски в словарь
#     jobs_title = html.find('a').text
#     link = html.find('a')['href']
#     company_name = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).text
#     company_name = company_name.strip()  # Strip - удаляет символы в начале и в конце строки
#     job_city = html.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
#     job_city = job_city.partition(',')[0]
#     return {'job_title': jobs_title, 'company_name': company_name, 'location': job_city, 'link': link}
#
#
# def extract_hh_jobs(last_page):
#     jobs_title = []
#     for page in range(last_page):
#         print(f'Парсинг страницы {page}')
#         result = session.get(url, headers=headers, params=dict(params, page=page))
#         soup = BeautifulSoup(result.text, 'html.parser')
#         results = soup.find_all('div', {'class': 'vacancy-serp-item'})
#         for result in results:
#             vacancy = extract_job(result)
#             jobs_title.append(vacancy)
#     return jobs_title