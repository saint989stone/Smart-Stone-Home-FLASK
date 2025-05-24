"""
Модуль моделей объектов и функций по работе с ними

Attributes
----------
asstLocl : db.
    Таблица ассоциаций между объектами locl и asst

Methods
-------
initAttrElemDict()
    функция перебирает список словарей с элементами и записывает атрибуты и элементы БД функцией initElem
initAttr()
    функция получает строковые значения Asst, Locl, Type и проверяет их в случае отсутствия делает запись в соотвествующей таблице БД
initElem()
    функция получает строковые значения Asst, Locl, Type, Name и делает запись в Таблице Elem
initAsstLocl()
    функция перебирает объекты Elem и определяет связь между объектами Asst и Locl, делает запись в таблице ассоциаций
querId_AsstLoclType()
    функция получает строковые значения Asst, Locl, Type и возвращает их id в виде списка
querElem_AsstLocl()
    функция получает строковые значения Asst, Locl и возвращает список соотвествующих элементов
querElem_Locl()
    функция получает строковые значения Locl и возвращает список соотвествующих элементов
"""

from app import db

asstLocl = db.Table('asstLocl',
                    db.Column('id_asst', db.Integer, db.ForeignKey('asst.id')), #создаем колонку, которая ссылается на id объектов asst
                    db.Column('id_locl', db.Integer, db.ForeignKey('locl.id'))  #создаем колонку, которая ссылается на id объектов locl
                    )

bindElem = db.Table('bindElem',
                    db.Column('id_folr', db.Integer, db.ForeignKey('elem.id')), #создаем колонку, которая ссылается на id oбъектов elem, которая указывает на (follower) следит за многими elem (подписчики elem)
                    db.Column('id_fold', db.Integer, db.ForeignKey('elem.id'))  #создаем колонку, которая ссылается на id oбъектов elem, которая указывает на (followed) имеет много связанных elem (подписанные elem)
                    )

class Asst(db.Model):
    """
    Класс Assigment (Предназначение) элемента: lght, scrt, fire и т.д.

    Attributes
    ----------
    id : integer
        первичный ключ
    name : str
        название предназначения
    elem :
        указывает на Elem, который представляет сторону отношения «много» и определяет имя поля asst, которое будет добавлено к объектам класса Elem, который указывает на объект «один»

    Methods
    -------
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4), index=True, unique=True)
    elem = db.relationship('Elem', backref='asst', lazy='dynamic')
    locl = db.relationship('Locl', secondary=asstLocl, backref=db.backref('locl', lazy='dynamic'))

class Locl(db.Model):
    """
    Класс Location (Нахождение) элемента, указывает к какому устройству принадлежит элемент. Например: Ktch, Hall

    Attributes
    ----------
    id : integer
        первичный ключ
    name : str
        название предназначения
    elem :
        указывает на Elem, который представляет сторону отношения «много» и определяет имя поля locl, которое будет добавлено к объектам класса Elem, который указывает на объект «один»
    ip : str
        ip адрес устройства. Например: 192.168.002.020
    asst :
        указывает на Asst в таблице ассоциаций, и определяет отношения «многие ко многим» и определяет связь между объектами locl и asst

    Methods
    -------
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4), index=True, unique=True)
    elem = db.relationship('Elem', backref='locl', lazy='dynamic')
    ip = db.Column(db.String(15), index=True, unique=True)
    asst = db.relationship('Asst', secondary=asstLocl, backref=db.backref('asst', lazy='dynamic'))

class Type(db.Model):
    """
    Класс Type (Тип) элемента, указывает к какому типу принадлежит элемент. Например: Swtc, Sldr, Indc

    Attributes
    ----------
    id : integer
        первичный ключ
    name : str
        название типа
    elem :
        указывает на Elem, который представляет сторону отношения «много» и определяет имя поля type, которое будет добавлено к объектам класса Elem, который указывает на объект «один»

    Methods
    -------
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4), index=True, unique=True)
    elem = db.relationship('Elem', backref='type', lazy='dynamic')

class Elem(db.Model):
    """
    Класс Element элемента, хранит связи с таблицами Asst, Locl, Type

    Attributes
    ----------
    id : integer
        первичный ключ
    id_asst : integer
        внешний ключ для связи с Таблицей Asst
    id_locl : integer
        внешний ключ для связи с Таблицей Locl
    id_type : integer
        внешний ключ для связи с Таблицей Type
    name : str
        название елемента например LghW
    nameFull : str
        полное название элемента
    value: Integer
        значение элемента

    Methods
    -------
    """
    id = db.Column(db.Integer, primary_key=True)
    id_asst = db.Column(db.Integer, db.ForeignKey('asst.id'))
    id_locl = db.Column(db.Integer, db.ForeignKey('locl.id'))
    id_type = db.Column(db.Integer, db.ForeignKey('type.id'))
    name = db.Column(db.String(4), index=True)
    nameFull = db.Column(db.String(16), index=True, unique=True)
    value = db.Column(db.Integer, index=True)
    fold = db.relationship('Elem', secondary=bindElem, #правая сторона связи (левая сторона — это родительский класс). Поскольку это самореферентное отношение, я должен использовать тот же класс с обеих сторон.
                           primaryjoin=(bindElem.c.id_folr == id), # указывает условие, которое связывает объект левой стороны (follower user) с таблицей ассоциаций. Условием объединения для левой стороны связи является идентификатор пользователя, соответствующий полю follower_id таблицы ассоциаций. Выражение followers.c.follower_id ссылается на столбец follower_id таблицы ассоциаций.
                           secondaryjoin=(bindElem.c.id_fold == id), #кофигурирует таблицу ассоциаций, которая используется для этой связи, которую я определил прямо над этим классом.
                           backref=db.backref('bindElem', lazy='dynamic'), lazy='dynamic')

    def folwElem(self, elem):
        if not self.is_folgElem(elem):
            self.fold.append(elem)

    def un_folwElem(self, elem):
        if not self.is_folgElem(elem):
            self.fold.remove(elem)

    def is_folgElem(self, elem):
        return self.fold.filter(bindElem.c.id_fold == elem.id).count() > 0 #формирует запрос на проверку отношений существует ли связь между elem


#Блок функций по инициализации объектов базы данных на основе словарей
# def initDB (listDict: list):
#     """Функция по инициализации БД """
#     print('Begin initialization')
#     print('Start initialization attributes')
#     initAttrElemDict(listDict, mode="attr")
#     print('Finish initialization attributes')
#     print('Start initialization elements')
#     initAttrElemDict(listDict, mode="elem")
#     print('Finish initialization attributes')
#     print('Start initialization associative table "Assignment & Location"')
#     initAsstLocl()
#     print('Finish')
#
# def initAttrElemDict (list: list, mode: str) -> '':
#     """Функция перебирает список словарей с элементами и записывает атрибуты и элементы БД функцией initElem
#     Attributes
#     ----------
#     mode - в зависимости от значения записывает атрибуты или элементы
#     """
#     if mode == 'attr':
#         for i in list: #перебираем словари в списке
#             for y in i: #перебираем ключи в словаре
#                 initAttr(y[0:4], y[4:8], y[8:12]) #вызываем функцию записи атрибутов элементов в соотвествующих таблицах
#     elif mode == 'elem':
#         for i in list:
#             for y in i:
#                 initElem(y[0:4], y[4:8], y[8:12], y[12:17]) #вызываем функцию записи элементов
#
# def initAttr(asst, locl, type):
#     """Функция получает строковые значения Asst, Locl, Type и проверяет их в случае отсутствия делает запись в соотвествующей таблице БД"""
#     querIdList = querId_AsstLoclType(asst, locl, type) #проверяем наличие id у атрибутов
#     if querIdList[0] is None or querIdList[1] is None or querIdList[2] is None: #осуществляем проверку записей на предмет отсутствия в таблицах
#         dictQuer = {Asst: [querIdList[0], asst], Locl: [querIdList[1], locl], Type: [querIdList[2], type]} #формируем словарь где ключи объекты БД, а значения список соответсвующих запросов и строковых представлений
#         listEntr = list() #пустой список для добавления отсутствующих записей
#         for i in dictQuer: #перебираем словарь
#             if dictQuer[i][0] is None: #проверяем запросы на отсутствующие значения
#                 entr = i(name=dictQuer[i][1]) #формируем соотвествующую запись
#                 listEntr.append(entr) #добавляем сформированную запись в список
#         db.session.add_all(listEntr)
#         db.session.commit()
#
# def initElem(asst, locl, type, name):
#     """Функция получает строковые значения Asst, Locl, Type, Name и делает запись в Таблице Elem """
#     listQuer = querId_AsstLoclType(asst, locl, type) #проверяем наличие id у атрибутов
#     entrElem = Elem(id_asst=listQuer[0].id, id_locl=listQuer[1].id, id_type=listQuer[2].id,
#                     name=name, nameFull=asst + locl + type + name, value=0,
#                     asst=listQuer[0], locl=listQuer[1], type=listQuer[2])  # записываем объект элемента с соотвествующими записями
#     db.session.add(entrElem)
#     db.session.commit()
#
# def initAsstLocl():
#     """Функция перебирает объекты Elem и определяет связь между объектами Asst и Locl, делает запись в таблице ассоциаций"""
#     querElem = Elem.query.all() #получаем список всех элементов
#     listEntr = list() #пустой список для добавления записей
#     for elem in querElem: #перебираем элементы в списке
#         querLocl = Locl.query.get(elem.locl.id) #получаем locl по id полученному из аттрибута элемента
#         entr = querLocl.asst.append(elem.asst) #делаем запись с добавлением в аттрибут asst объекта полученного из элемента
#         listEntr.append(entr) #добавляем запись в словарь
#     db.session.add_all(listEntr)
#     db.session.commit()
#
# def jsonAsst (*asst):
#     """Функция получает строковые значения Asst в виде списка и возвращает соответствующие элементы с их значениями в виде json"""
#     dictElem = dict() #пустой словарь для добавления элементов
#     for i in asst:
#         querAsst = Asst.query.filter_by(name=i).first() #осуществляем поиск в таблице Asst назначения по name
#         querElem = Elem.query.filter_by(id_asst=querAsst.id).all() #осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id
#         dictElemTemp = {i.nameFull: i.value for i in querElem} #запускаем генератор временного словаря, где ключ это nameFull, а значение это value
#         dictElem.update(dictElemTemp) #добавляем временный словарь в основной
#     return jsonify(dictElem) #возвращаем словарь преобразованный в формат json
#
# def jsonAsstLocl (*asstLocl: list) -> 'json':
#     """Функция получает строковые значения Asst и Locl возвращает соответствующие элементы с их значениями в виде json"""
#     dictElem = dict()
#     for i in asstLocl:
#         asst = i[0:4] #получаем строковое значение Предназаначения
#         locl = i[4:8] #получаем строковое значение Нахождения
#         querAsst = Asst.query.filter_by(name=asst).first() #осуществляем поиск в таблице Asst назначения по name
#         querLocl = Locl.query.filter_by(name=locl).first() #осуществляем поиск в таблице Locl назначения по name
#         querElem = Elem.query.filter_by(id_asst=querAsst.id, id_locl=querLocl.id).all() #осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id и в столбце id_locl по id
#         dictElemTemp = {i.nameFull: i.value for i in querElem}  #запускаем генератор временного словаря, где ключ это nameFull, а значение это value
#         dictElem.update(dictElemTemp) #добавляем временный словарь в основной
#         #transmit.rqstLocl(i, querLocl.ip, dictElemTemp) #отправляем словарь с элементами соотвествующему контроллеру
#     return jsonify(dictElem) #возвращаем словарь преобразованный в формат json
#
# def parsJson (dicts: dict, asstLoclName: str = None, loclName: str = None):
#     listElem = list()
#     if asstLoclName != None:
#         listElem.extend(querElem_AsstLocl(asstLoclName[0:4], asstLoclName[4:8]))
#     if loclName != None:
#         for asst in ('clmt', 'scrt', 'fire', 'watr'):
#             listElem.extend(querElem_AsstLocl(asst, loclName))
#     for elem in listElem:
#         print(elem.nameFull, elem.value)
#
# def parsJsonLocl (locl: dict, loclName: str):
#     querElemList = querElem_Locl(loclName)
#     listEnry = list() #пустой список для добавления записей изменения значения элементов
#     for key in locl: #перебираем ключи в словаре
#         for elem in querElemList: #перебираем элементы в списке
#             if key == elem.nameFull: #если ключ совпадает с именем элемента
#                 if elem.value != locl[key]: #если значение ключа не совпадает со значением из словаря
#                     elem.value = locl[key] #изменяем значение элемента
#                     print(key)
#                 listEnry.append(elem) #добавляем соотвествующую запись в словарь
#     db.session.add_all(listEnry)
#     db.session.commit()
#
#     #for key in test:
#     #    print(key, test[key])
#
# def parsJsonAsstLocl (asstLocl: dict):
#     """Функция принимает словарь co значениями asstLocl в формата Json парсит его и записывает значения в базу данных"""
#     asstLoclName = list(asstLocl.keys())[0]
#     querElemList = querElem_AsstLocl(asstLoclName[0:4], asstLoclName[4:8]) #получаем список элементов соотвествующих asst и locl
#     listEnry = list() #пустой список для добавления записей изменения значения элементов
#     for key in asstLocl: #перебираем ключи в словаре
#         for elem in querElemList: #перебираем элементы в списке
#             if key == elem.nameFull: #если ключ совпадает с именем элемента
#                 if elem.value != asstLocl[key]: #если значение ключа не совпадает со значением из словаря
#                     elem.value = asstLocl[key] #изменяем значение элемента
#                 listEnry.append(elem) #добавляем соотвествующую запись в словарь
#     db.session.add_all(listEnry)
#     db.session.commit()
#
# def querId_AsstLoclType(asst: str, locl: str, type: str) -> list:
#     """Функция получает строковые значения Asst, Locl, Type и возвращает их id в виде списка"""
#     querAsst = Asst.query.filter_by(name=asst).first() #осуществляем поиск в таблице Asst назначения по name
#     querLocl = Locl.query.filter_by(name=locl).first() #осуществляем поиск в таблице Locl назначения по name
#     querType = Type.query.filter_by(name=type).first() #осуществляем поиск в таблице Type назначения по name
#     return [querAsst, querLocl, querType]
#
# def querElem_AsstLocl(asst: str, locl: str) -> list:
#     """Функция получает строковые значения Asst, Locl и возвращает список соотвествующих элементов"""
#     querAsst = Asst.query.filter_by(name=asst).first()  # осуществляем поиск в таблице Asst назначения по name
#     querLocl = Locl.query.filter_by(name=locl).first()  # осуществляем поиск в таблице Locl назначения по name
#     return Elem.query.filter_by(id_asst=querAsst.id, id_locl=querLocl.id).all()  # осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id и в столбце id_locl по id
#
# def querElem_Locl(locl: str) -> list:
#     """Функция получает строковые значения Locl и возвращает список соотвествующих элементов"""
#     querLocl = Locl.query.filter_by(name=locl).first()
#     return Elem.query.filter_by(id_locl=querLocl.id).all()
