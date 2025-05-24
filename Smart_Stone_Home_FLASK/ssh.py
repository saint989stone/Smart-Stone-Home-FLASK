"""
Модуль запуска приложения SmartStoneHome верхнего уровня. Импорт экземпляра приложения.

Attributes
----------

Methods
-------

"""

from app import app

if __name__ == "__main__":
    app.run(host='192.168.2.20', port=5005, debug=True) #запуск приложения с определенными значениями конфигурации