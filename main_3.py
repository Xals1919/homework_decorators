from functools import wraps
from datetime import datetime
import requests
from fake_headers import Headers


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main_3.log', 'a') as log_file:
            log_file.write(f'Дата и время вызова {datetime.today()}\nИмя функции: {old_function.__name__}\nАргументы: {args}, {kwargs}\nВозвращает значение: {result}\n\n')
        return result
    return new_function

@logger
def header_gen(os, browser):
        header_gen = Headers(os, browser)
        return header_gen


@logger
def main_html(os, browser):
        URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
        main_hh = requests.get(URL, headers=header_gen(os=os, browser=browser).generate())
        main_hh_html = main_hh.text
        return main_hh_html

header_gen(os='Windows', browser='Chrome')
main_html(os='Windows', browser='Chrome')
