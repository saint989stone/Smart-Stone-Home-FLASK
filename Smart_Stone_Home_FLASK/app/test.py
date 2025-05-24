

from app import models
from app import dicts
from app.dicts import listDict
from app import drives

SwtcServ = models.Elem.query.filter_by(nameFull="lghtKtchSwtcSwtc").first()
print(SwtcServ)
p = models.db.session.query(models.bindElem).filter(models.bindElem.c.id_folr == SwtcServ.id)
for i in p:
    print(i)
o = SwtcServ.fold.filter(models.bindElem.c.id_folr == SwtcServ.id)
for i in o:
    print(i)
#funcDB.initDB(listDict)

#f = models.Elem.query.filter_by(nameFull="lghtKtchSwtcSwtc").first()
#for i in f.fold.all():
#    print(i.nameFull)
#funcDB.initElemServBind()
# goo=funcDB.querElem_Locl('Serv')
# for i in goo:
#     asst = i.nameFull[8:12]
#     listEntr = list()
#     if asst != 'Text':
#         foo = funcDB.querElem_AsstName(asst, 'Swtc')
#         for y in foo:
#             print(i.nameFull, y.nameFull)
#             print(y)
#             print(i)
#             i.fold.append(y)
#             models.db.session.add(i)
#             models.db.session.commit()

#servSwtc = models.Elem.query.filter_by(id=7).first()
#goo = servSwtc.fold.all()
#for i in goo:
#    print(i.nameFull)
# print(servSwtc.nameFull)
# ktchSwtc = models.Elem.query.filter_by(id=9).first()
# print(ktchSwtc.nameFull)
# hallSwtc = models.Elem.query.filter_by(id=12).first()
# print(hallSwtc.nameFull)
#servSwtc.fold.append(ktchSwtc)
#servSwtc.folwElem(hallSwtc)
#servSwtc.folwElem(ktchSwtc)
#models.db.session.add(servSwtc)
#models.db.session.commit()
#print(servSwtc.fold.all())

# querElem = models.Elem.query.all()  # получаем список всех элементов
# listEntr = list()  # пустой список для добавления записей
# for elem in querElem:  # перебираем элементы в списке
#      querLocl = models.Locl.query.get(elem.locl.id)  # получаем locl по id полученному из аттрибута элемента
#      querAsst = models.Asst.query.get(elem.asst.id)
#      querLocl.asst.append(querAsst)  # делаем запись с добавлением в аттрибут asst объекта полученного из элемента
#      models.db.session.add(querLocl)
#      models.db.session.commit()
#
#
#
# loclList = models.Locl.query.all()
# for locl in loclList:
#       print (locl.name)
#       for asst in locl.asst:
#           print(asst.name)

#e = models.Locl.query.filter_by(name='Ktch')
###http = urllib3.PoolManager()
#url = 'http://192.168.2.102/lghtHall'
#resp = http.request('GET', url)

#models.initAttrElemDict(dicts.listDict, mode="elem")
#print(type(models.asstLocl))


#
#models.db.session.commit()
#elem = models.Elem.query.get(25)
#print(elem.locl.name)






"""
foo = {'swtcGnrlclmtSwtc': 1, 'swtcGnrllghtSwtc': 1, 'swtcGnrlscrtSwtc': 1, 'swtcGnrlfireSwtc': 1, 'swtcGnrlwatrSwtc': 1,
       'swtcGnrladmrSwtc': 1, 'swtcGnrlAdmrSwtc': 1, 'swtcGnrlClmtSwtc': 1, 'swtcGnrlFireSwtc': 1, 'swtcGnrlLghtSwtc': 1,
       'swtcGnrlScrtSwtc': 1, 'swtcGnrlWatrSwtc': 1}

models.parsJson(foo)

models.initAttrElemDict(dicts.listDict, mode='elem')

print('go')
models.initAttrElemDict(dicts.listDict, mode='elem')

def goo (*asstLocl):
    dictElem = dict()
    for i in asstLocl:
        querAsst = models.Asst.query.filter_by(name=i[0:4]).first()
        querLocl = models.Locl.query.filter_by(name=i[4:8]).first()
        querElem = models.Elem.query.filter_by(id_asst=querAsst.id, id_locl=querLocl.id).all()
        dictElemTemp = {i.nameFull: i.value for i in querElem}  # запускаем генератор временного словаря, где ключ это nameFull, а значение это value
        dictElem.update(dictElemTemp)
    print(dictElem)
goo('admrKtch')

import jsons

def unon(*dicts):
    uninlist = list()
    for i in dicts:
        uninlist += list(i.items())
    return dict(uninlist)
#print(unon(jsons.lghtKtch, jsons.lghtHall, jsons.scrtHall))
#print(jsons.listJson[4:6])
#print(jsons.union(jsons.listJson[4:5]))

from app import app, models, dicts
from flask import jsonify

#models.init_elem(asst='clmt', locl='Ktch', type='Swtc', name='Swtc')
elems = models.Elem.query.all()
for e in elems:
    if e.locl.name == 'Hall':
        print('Yes')
    else:
        print('No')

#jsons.union(jsons.lghtHall, jsons.lghtKtch)

def foo (*asst):
    dictElem = dict() #пустой словарь для добавления элементов
    for i in asst:
        querAsst = models.Asst.query.filter_by(name=i).first() # осуществляем поиск в таблице Asst назначения по name
        querElem = models.Elem.query.filter_by(id_asst=querAsst.id).all() #осуществляем поиск в таблице Elem всех элементов в столбце id_asst по id
        dictElemTemp = {i.nameFull: i.value for i in querElem} #запускаем генератор временного словаря, где ключ это nameFull, а значение это value
        dictElem.update(dictElemTemp) #добавляем временный словарь в основной
    return jsonify(dictElem)
foo('lght', 'clmt')
"""