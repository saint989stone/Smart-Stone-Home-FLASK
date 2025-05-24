"""
Модуль с функциями по работе с базой данных

Attributes
----------

Methods
-------
initAttrElemDict()
    функция перебирает список словарей с элементами и записывает атрибуты и элементы БД функцией initElem
initAttr()
    функция получает строковые значения Asst, Locl, Type и проверяет их в случае отсутствия делает запись в
    соотвествующей таблице БД
initElem()
    функция получает строковые значения Asst, Locl, Type, Name и делает запись в Таблице Elem
initAsstLocl()
    функция перебирает объекты Elem и определяет связь между объектами Asst и Locl, делает запись в таблице ассоциаций
initElemBind()
    функция перебирает объекты Elem swtcServ и определяет их связь с соотвествющими asstLoclSwtcSwtc, а также определяет
    связь asstLoclSwtcSwtc с соответсвующими asstLoclSwtcName и делает запись в таблице ассоциаций bindElem
jsonAsstLocl(*asstLocl: list) -> 'json':
    функция получает строковые значения Asst и Locl возвращает соответствующие элементы с их значениями в виде json
parsJsonLocl (locl: dict, loclName: str) -> None:
    функция принимает словарь co значениями элементов соотвествующего Locl получает список объектов элементов и
    передают для записи в функцию parsJsonWrtrElem
parsJsonAsstLocl(asstLocl: dict) -> None:
    функция принимает словарь co значениями элементов соотвествующего asstLocl получает список объектов элементов и
    передают для записи в функцию parsJsonWrtrElem
parsJsonWrtrElem (recdElemDict: dict, querElemList: list) -> None:
    функция принимает принятый словарь приобразованный из json-запроса и список элементов для изменения значения в БД
querId_AsstLoclType()
    функция получает строковые значения Asst, Locl, Type и возвращает их id в виде списка
querElem_AsstName(asst: str, name: str) -> list:
    функция получает строковые значения Asst и Name элемента и возвращает список соотвествующих элементов
querElem_AsstLocl(asst: str, name: str) -> list:
    функция получает строковые значения Asst, Locl и возвращает список соотвествующих элементов
querElem_Locl(locl: str) -> list:
    функция получает строковые значения Locl и возвращает список соотвествующих элементов
"""


import app.models as m
import app.transmission as t
from flask import jsonify

#Блок функций по инициализации объектов базы данных на основе словарей
def initDB(listDict: list):
    print('Begin initialization')
    print('Start initialization attributes')
    initAttrElemDict(listDict, mode="attr")
    print('Finish initialization attributes')
    print('Start initialization elements')
    initAttrElemDict(listDict, mode="elem")
    print('Finish initialization attributes')
    print('Start initialization associative table "Assignment & Location"')
    initAsstLocl()
    print('Start initialization associative table "Bind element" for swtcServ')
    initElemBind()
    print('Finish')

def initAttrElemDict (list: list, mode: str) -> '':
    """Функция перебирает список словарей с элементами и записывает атрибуты и элементы БД функцией initElem
    Attributes
    ----------
    mode - в зависимости от значения записывает атрибуты или элементы
    """
    if mode == 'attr':
        for i in list: #перебираем словари в списке
            for y in i: #перебираем ключи в словаре
                initAttr(y[0:4], y[4:8], y[8:12]) #вызываем функцию записи атрибутов элементов в соотвествующих таблицах
        print(' ')
    elif mode == 'elem':
        for i in list:
            for y in i:
                initElem(y[0:4], y[4:8], y[8:12], y[12:17]) #вызываем функцию записи элементов
        print(' ')

def initAttr(asst, locl, type):
    """Функция получает строковые значения Asst, Locl, Type и проверяет их в случае отсутствия делает запись в соотвествующей таблице БД"""
    querIdList = querId_AsstLoclType(asst, locl, type) #проверяем наличие id у атрибутов
    if querIdList[0] is None or querIdList[1] is None or querIdList[2] is None: #осуществляем проверку записей на предмет отсутствия в таблицах
        dictQuer = {m.Asst: [querIdList[0], asst], m.Locl: [querIdList[1], locl], m.Type: [querIdList[2], type]} #формируем словарь где ключи объекты БД, а значения список соответсвующих запросов и строковых представлений
        listEntr = list() #пустой список для добавления отсутствующих записей
        for i in dictQuer: #перебираем словарь
            if dictQuer[i][0] is None: #проверяем запросы на отсутствующие значения
                entr = i(name=dictQuer[i][1]) #формируем соотвествующую запись
                listEntr.append(entr) #добавляем сформированную запись в список
                print('|', end=' ')
        m.db.session.add_all(listEntr)
        m.db.session.commit()

def initElem(asst, locl, type, name):
    """Функция получает строковые значения Asst, Locl, Type, Name и делает запись в Таблице Elem """
    listQuer = querId_AsstLoclType(asst, locl, type) #проверяем наличие id у атрибутов
    entrElem = m.Elem(id_asst=listQuer[0].id, id_locl=listQuer[1].id, id_type=listQuer[2].id,
                    name=name, nameFull=asst + locl + type + name, value=0,
                    asst=listQuer[0], locl=listQuer[1], type=listQuer[2])  # записываем объект элемента с соотвествующими записями
    m.db.session.add(entrElem)
    m.db.session.commit()
    print('|', end='')

def initAsstLocl():
    """Функция перебирает объекты Elem и определяет связь между объектами Asst и Locl, делает запись в таблице ассоциаций asstLocl"""
    querElem = m.Elem.query.all()  # получаем список всех элементов
    for elem in querElem:  # перебираем элементы в списке
        querLocl = m.Locl.query.get(elem.locl.id)  # получаем locl по id полученному из аттрибута элемента
        querAsst = m.Asst.query.get(elem.asst.id)
        querLocl.asst.append(querAsst)  # делаем запись с добавлением в аттрибут asst объекта полученного из элемента
        m.db.session.add(querLocl)
        m.db.session.commit()

def initElemBind():
    """Функция перебирает объекты Elem swtcServ и определяет их связь с соотвествющими asstLoclSwtcSwtc делает запись в таблице ассоциаций bindElem"""
    querElemServ = querElem_Locl('Serv')
    for elemServ in querElemServ: # перебираем элементы Locl Serv
        asst = elemServ.nameFull[8:12] # получаем имя соотвествующего asst
        if asst != 'Text':  # отбрасываем элементы sttsServText
            querElemAsstSwtc = querElem_AsstName(asst, 'Swtc') # получаем список елементов типа SwtcSwtc
            for elemAsstSwtc in querElemAsstSwtc: # перебираем элементы SwtcSwtc
                locl = elemAsstSwtc.nameFull[4:8] # определяем Locl элемента SwtcSwtc
                querElemAsstLoclTypeSwtc = querElem_AsstLoclType(asst, locl, 'Swtc') # получаем список элементов соответсвующих Asst Locl и Type соотвествущих Swtc
                for elemAsstLoclTypeSwtc in querElemAsstLoclTypeSwtc: # перебираем список элементов
                    if elemAsstLoclTypeSwtc.name == 'Swtc': # отбрасываем элементы SwtcSwtc
                        continue
                    elemAsstSwtc.fold.append(elemAsstLoclTypeSwtc) # добавляем элемент Swtc к элементу SwtcSwtc
                    m.db.session.add(elemServ)
                    m.db.session.commit()
                elemServ.fold.append(elemAsstSwtc) # добавляем элемент SwtcSwtc к элементу swtcServ
                m.db.session.add(elemServ)
                m.db.session.commit()

#Блок функций по предоставлению информации из БД в json
def jsonAsst(*asst):
    """Функция получает строковые значения Asst в виде списка и возвращает соответствующие элементы с их значениями в виде json"""
    dictElem = dict()  # пустой словарь для добавления элементов
    for i in asst:
        querAsst = m.Asst.query.filter_by(name=i).first()  # осуществляем поиск в таблице Asst назначения по name
        querElem = m.Elem.query.filter_by(id_asst=querAsst.id).all()  # осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id
        dictElemTemp = {i.nameFull: i.value for i in querElem}  # запускаем генератор временного словаря, где ключ это nameFull, а значение это value
        dictElem.update(dictElemTemp)  # добавляем временный словарь в основной
    return jsonify(dictElem)  # возвращаем словарь преобразованный в формат json

def jsonAsstLocl(*asstLocl: list) -> 'json':
    """Функция получает строковые значения Asst и Locl возвращает соответствующие элементы с их значениями в виде json"""
    dictElem = dict()
    for i in asstLocl:
        asst = i[0:4]  # получаем строковое значение Предназаначения
        locl = i[4:8]  # получаем строковое значение Нахождения
        querAsst = m.Asst.query.filter_by(name=asst).first()  # осуществляем поиск в таблице Asst назначения по name
        querLocl = m.Locl.query.filter_by(name=locl).first()  # осуществляем поиск в таблице Locl назначения по name
        querElem = m.Elem.query.filter_by(id_asst=querAsst.id,
                                        id_locl=querLocl.id).all()  # осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id и в столбце id_locl по id
        dictElemTemp = {i.nameFull: i.value for i in querElem}  # запускаем генератор временного словаря, где ключ это nameFull, а значение это value
        dictElem.update(dictElemTemp)  # добавляем временный словарь в основной

        t.rqstLocl(i, querLocl.ip, dictElemTemp) #отправляем словарь с элементами соотвествующему контроллеру
    return jsonify(dictElem)  # возвращаем словарь преобразованный в формат json

#Блок функций по парсингу json

def parsJsonLocl (locl: dict, loclName: str) -> None:
    """Функция принимает словарь co значениями элементов соотвествующего Locl получает список объектов элементов и передают для записи в функцию parsJsonWrtrElem"""
    querElemList = list() # создаем пустой список элементов
    querLocl = m.Locl.query.filter_by(name=loclName).first() # получаем соотвествующий объект Locl
    querAsst = querLocl.asst # из таблицы ассоциаций получаем список объектов asst соотвествующих объекту Locl
    for asst in querAsst:
        querElemList.extend(m.Elem.query.filter_by(id_asst=asst.id, id_locl=querLocl.id).all()) # формируем список объектов Elem в столбце id_asst по id и в столбце id_locl по id
    parsJsonWrtrElem(locl, querElemList)

def parsJsonAsstLocl(asstLocl: dict) -> None:
    """Функция принимает словарь co значениями элементов соотвествующего asstLocl получает список объектов элементов и передают для записи в функцию parsJsonWrtrElem"""
    asstLoclName = list(asstLocl.keys())[0]
    querElemList = querElem_AsstLocl(asstLoclName[0:4], asstLoclName[4:8])  # получаем список элементов соотвествующих asst и locl
    parsJsonWrtrElem(asstLocl, querElemList)

def parsJsonWrtrElem (recdElemDict: dict, querElemList: list) -> None:
    """Функция принимает принятый словарь приобразованный из json-запроса и список элементов для изменения значения в БД"""
    listEntr = list() # пустой список для добавления записей изменения значения элементов
    for key in recdElemDict: # перебираем ключи в словаре
        for elem in querElemList: # перебираем элементы в списке
            if key == elem.nameFull: # если ключ совпадает с именем элемента
                if elem.value != recdElemDict[key]: # если значение ключа не совпадает со значением из словаря
                    elem.value = recdElemDict[key] # изменяем значение элемента
                    if len(elem.fold.all()) > 0: # проверяем элемент на связь с другими элементами
                        listElemFold = handSwtcElem(elem, recdElemDict[key]) # получаем список связанных элементов с измененными значениями
                        listEntr.extend(listElemFold) # объединяем основной и полученный список
                    pass # перебираем элементы до первого несовпавшего по значению
                listEntr.append(elem) # добавляем соотвествующую запись в словарь
    m.db.session.add_all(listEntr) # добавляем запись в сессию
    m.db.session.commit() # производим запись сессии

def handSwtcElem (elem: object, value: int) -> object:
    listEntr = list() # пустой список для добавления записей изменения значения элементов
    if elem.id_locl == 1: # проверяем на принадлежность к Locl Serv
        for elemFold in elem.fold.all(): # перебираем связанные элементы
            elemFold.value = value # изменяем значение связанных элементов
            if value == 0:
                listElemFoldFold = elemFold.fold.all() # проверяем связанные элементы asstLoclSwtc c элементом asstLoclSwtcSwtc
                if len(listElemFoldFold) > 0:
                    for elemFoldFold in listElemFoldFold:
                        print(elemFoldFold.nameFull)
                        elemFoldFold.value = value
                        listEntr.append(elemFoldFold)
            listEntr.append(elemFold) # добавляем элементы в список
    return (listEntr) # возвращаем полученный список


#Блок функций по работе с запросами к базе данных
def querId_AsstLoclType(asst: str, locl: str, type: str) -> list:
    """Функция получает строковые значения Asst, Locl, Type и возвращает их id в виде списка"""
    querAsst = m.Asst.query.filter_by(name=asst).first() #осуществляем поиск в таблице Asst назначения по name
    querLocl = m.Locl.query.filter_by(name=locl).first() #осуществляем поиск в таблице Locl назначения по name
    querType = m.Type.query.filter_by(name=type).first() #осуществляем поиск в таблице Type назначения по name
    return [querAsst, querLocl, querType]

def querElem(asst: str=None, locl: str=None, type: str=None, name: str=None) -> list:
    return

def querElem_AsstName(asst: str, name: str) -> list:
    """Функция получает строковые значения Asst и Name элемента и возвращает список соотвествующих элементов"""
    querAsst = m.Asst.query.filter_by(name=asst).first() #осуществляем поиск в таблице Asst назначения по name
    return m.Elem.query.filter_by(id_asst=querAsst.id,
                                  name=name).all()  # осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id и в столбце id_locl по id

def querElem_AsstLoclType(asst: str, locl: str, type: str) -> list:
    """Функция получает строковые значения Asst, Locl и возвращает список соотвествующих элементов"""
    querAsst = m.Asst.query.filter_by(name=asst).first() # осуществляем поиск в таблице Asst назначения по name
    querLocl = m.Locl.query.filter_by(name=locl).first() # осуществляем поиск в таблице Locl назначения по name
    querType = m.Type.query.filter_by(name=type).first() # осуществляем поиск в таблице Type назначения по name
    return m.Elem.query.filter_by(id_asst=querAsst.id,
                                  id_locl=querLocl.id,
                                  id_type=querType.id).all()  # осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id и в столбце id_locl по id

def querElem_AsstLocl(asst: str, locl: str) -> list:
    """Функция получает строковые значения Asst, Locl и возвращает список соотвествующих элементов"""
    querAsst = m.Asst.query.filter_by(name=asst).first()  # осуществляем поиск в таблице Asst назначения по name
    querLocl = m.Locl.query.filter_by(name=locl).first()  # осуществляем поиск в таблице Locl назначения по name
    return m.Elem.query.filter_by(id_asst=querAsst.id,
                                  id_locl=querLocl.id).all()  # осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id и в столбце id_locl по id

def querElem_Locl(locl: str) -> list:
    """Функция получает строковые значения Locl и возвращает список соотвествующих элементов"""
    querLocl = m.Locl.query.filter_by(name=locl).first()
    return m.Elem.query.filter_by(id_locl=querLocl.id).all()

def querElem_Asst(asst: str) -> list:
    """Функция получает строковые значения Asst и возвращает список соотвествующих элементов"""
    querAsst = m.Asst.query.filter_by(name=asst).first()
    return m.Elem.query.filter_by(id_asst=querAsst.id).all()