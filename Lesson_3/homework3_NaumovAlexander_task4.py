"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
import requests


class WebPageCash:
    def __init__(self, salt):
        self.salt = salt
        self.url_dict = dict()

    def add_url(self, url):
        content = requests.get(url)
        self.url_dict[hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()] = content.content

    def get_url_content(self, url):
        if hashlib.sha256(url.encode() + self.salt.encode()).hexdigest() in self.url_dict.keys():
            print(self.url_dict[hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()])
        else:
            self.add_url(url)
            print('No such url. It was added into cache.')


url_cache_1 = WebPageCash('salty')
url_cache_1.get_url_content('https://google.ru/')
url_cache_1.get_url_content('https://google.ru/')
