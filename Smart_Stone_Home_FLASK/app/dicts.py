"""
Модуль cодержит объекты словарей, содержащих элементы

Attributes
----------

Methods
-------

"""

sttsServ={
    "sttsServTextTemp": 0,
    "sttsServTextHmdt": 0
}
swtcServ={
    "swtcServclmtSwtc": 0,
    "swtcServlghtSwtc": 0,
    "swtcServscrtSwtc": 0,
    "swtcServfireSwtc": 0,
    "swtcServwatrSwtc": 0,
    "swtcServmntgSwtc": 1
}
clmtKtch={
    "clmtKtchSwtcSwtc": 0,
    "clmtKtchTextTemp": 0,
    "clmtKtchTextHmdt": 0
}
clmtHall={
    "clmtHallSwtcSwtc": 0,
    "clmtHallTextTemp": 0,
    "clmtHallTextHmdt": 0
}
lghtKtch={
    "lghtKtchSwtcSwtc": 0,
    "lghtKtchSwtcLghW": 0,
    "lghtKtchSwtcWtfl": 0,
    "lghtKtchSwtcSond": 0,
    "lghtKtchSwtcLghT": 0,
    "lghtKtchSwtcLghF": 0,
    "lghtKtchSwtcLghC": 0,
    "lghtKtchSwtcNgSg": 0,
    "lghtKtchSldrLgWR": 0,
    "lghtKtchSldrLgWG": 0,
    "lghtKtchSldrLgWB": 0,
    "lghtKtchSldrLgWW": 0,
    "lghtKtchSldrWtfl": 0
}
lghtHall={
    "lghtHallSwtcSwtc": 0,
    "lghtHallSwtcLghW": 0,
    "lghtHallSwtcLgTV": 0,
    "lghtHallSwtcWtfl": 0,
    "lghtHallSwtcSond": 0,
    "lghtHallSwtcNgSg": 0,
    "lghtHallSldrLgWR": 0,
    "lghtHallSldrLgWG": 0,
    "lghtHallSldrLgWB": 0,
    "lghtHallSldrLgWW": 0,
    "lghtHallSldrLgTR": 0,
    "lghtHallSldrLgTG": 0,
    "lghtHallSldrLgTB": 0,
    "lghtHallSldrLgTW": 0,
    "lghtHallSldrWtfl": 0
}
scrtHall={
    "scrtHallSwtcSwtc": 0,
    "scrtHallAlrmBuzz": 0,
    "scrtHallIndcRoom": 0,
    "scrtHallIndcBalc": 0
}
scrtKtch={
    "scrtKtchSwtcSwtc": 0,
    "scrtKtchAlrmBuzz": 0,
    "scrtKtchIndc1111": 0,
    "scrtKtchIndc2222": 0
}
fireHall={
    "fireHallSwtcSwtc": 0,
    "fireHallAlrmBuzz": 0,
    "fireHallIndcRoom": 0
}
fireKtch={
    "fireKtchSwtcSwtc": 0,
    "fireKtchAlrmBuzz": 0,
    "fireKtchIndcRoom": 0,
    "fireKtchIndcCkng": 0
}
watrKtch={
    "watrKtchSwtcSwtc": 0,
    "watrKtchAlrmBuzz": 0,
    "watrKtchIndc1111": 0,
    "watrKtchIndc2222": 0
}
mntgHall={
    "mntgHallSwtcSwtc": 1,
    "mntgHallAlrmBuzz": 1,
    "mntgHallIndcHall": 1
}
mntgKtch={
    "mntgKtchSwtcSwtc": 1,
    "mntgKtchAlrmBuzz": 1,
    "mntgKtchIndcKtch": 1
}

listDict = [sttsServ, swtcServ,
            clmtKtch, clmtHall,
            lghtKtch, lghtHall,
            scrtKtch, scrtHall,
            fireKtch, fireHall,
            watrKtch,
            mntgKtch, mntgHall]