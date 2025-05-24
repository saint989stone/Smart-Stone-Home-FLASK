"""
Модуль функции просмотра

Attributes
----------

Methods
-------
index()
    Фунция просмотра главной страницы
"""

from app import app, drives
from flask import redirect, url_for, render_template, request, make_response
import json

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Функция просмотра главной страницы, возвращает фаил главной страницы, которая погружает файлы из static"""
    return render_template('index.html')

@app.route('/loadOnce', methods=['POST'])
def loadOnce():
    """Функция обработки запросов на предоставление данных при загрузке страницы"""
    return drives.jsonAsst('lght')

@app.route('/loadPerd', methods=['POST'])
def loadPerd():
    """Функция обработки запросов на предоставление данных через определенное время"""
    return drives.jsonAsst('swtc', 'stts', 'clmt', 'scrt', 'fire', 'watr', 'mntg')

@app.route('/load/<asstLocl>', methods=['POST'])
def loadAsstLocl(asstLocl):
    """Функция обработки запросов на предоставление данных по запросу"""
    return drives.jsonAsstLocl(asstLocl)

@app.route('/<asstLocl>', methods=['POST'])
def getAsstLocl(asstLocl):
    """Функция обработки запросов при изменении данных на странице"""
    drives.parsJsonAsstLocl(request.get_json())
    return drives.jsonAsstLocl(asstLocl)

@app.route('/locl/<locl>', methods=['POST'])
def getLocl(locl):
    """Функция обработки периодических запросов от locl"""
    drives.parsJsonLocl(request.get_json(), loclName=locl)
    print("Yes hall")
    return make_response('ok')


