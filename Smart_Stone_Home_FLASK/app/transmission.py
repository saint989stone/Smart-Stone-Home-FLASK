"""
Модуль по с функциями по отправки запросов и ответов http

Attributes
----------

Methods
-------
initElem()
    функция получает строковые значения Asst, Locl, Type, Name инициализрует элемент и записывает в БД элемент
initElemDict()
    функция перебирает список словарей с элементами и записывает и в БД функцией initElem
jsonAsst()
    функция получает строковые значения Asst и возвращает элементы с их значениями в виде json
"""
import requests

def rqstLocl (asstLocl: str, ip: str, dictElem: dict):
    """Функция получает строковые значения locl, ip и словарь и передает соотвествуещему контролеру"""
    url = 'http://' + ip + '/' + asstLocl #подготовливам строку вида http://192.168.2.20/lghtHall
    rsps = requests.post(url, str(dictElem))
    rspsStts = rsps.status_code
    print(url)
    print(rspsStts)
