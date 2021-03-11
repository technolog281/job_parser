from search_count import search_count

print('Введите локацию:')
location = input()
city = location.replace(' ', '+')
print('Введите текст для поиска:')
text = input()
search_text = text.replace(' ', '+')

params = {
    'q': search_text,
    'l': city
}

print(search_count(params))
