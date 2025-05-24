"""
Модуль ининициализации пакета модулей

Attributes
----------
app : object
    объект приложения как экземпляр класса Flask, импортированного из пакета flask. Переменная __name__, переданная в класс
    Flask, является предопределенной переменной Python, которая задается именем модуля, в котором она используется.
    Flask использует расположение модуля, переданного здесь как отправную точку.
db : object
    объект базы данных
migrate : object
    механизм миграции базы данных

Methods
-------

"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models