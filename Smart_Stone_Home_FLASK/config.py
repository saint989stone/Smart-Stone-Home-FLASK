"""
Модуль конфигурации приложения, где переменные определяются,
как ключи словаря

Attributes
----------
basedir : str
    путь к основному каталогу приложения

Methods
-------

"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Класс Config используется для хранение переменных конфигурации в виде словаря
    Attributes
    ----------
    SQLALCHEMY_DATABASE_URI : str
        путь к основному каталогу приложения в котором хранится фаил базы данных
    SQLALCHEMY_TRACK_MODIFICATIONS : boolean
        параметр который отключает функцию, которая сигнализирует о изменениях в базе данных

    Methods
    -------
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ssh.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
