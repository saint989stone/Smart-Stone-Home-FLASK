function handSwtc (swtcName_HandSwtc, loclElemStrg_HandSwtc){
    swtcArealghtKtch = ["lghtKtchSwtcLghW", "lghtKtchSwtcWtfl", "lghtKtchSwtcSond", "lghtKtchSwtcLghC", "lghtKtchSwtcNgSg",
            "lghtKtchSwtcLghT", "lghtKtchSwtcLghF"]; //создаем массив выключателей которыми управляет главный Swtc
    swtcArealghtHall = ["lghtHallSwtcLghW", "lghtHallSwtcWtfl", "lghtHallSwtcSond", "lghtHallSwtcLgTV", "lghtHallSwtcNgSg"]; //создаем массив выключателей которыми управляет главный Swtc
    if (swtcName_HandSwtc.slice(8) == "SwtcSwtc"){ //проверка SwtcSwtc на значение SwtcServ если SwtcServ = 0, то соответсвующий SwtcSwtc не активен
        if (window["swtcServ"]["swtcServ"+swtcName_HandSwtc.slice(0, 4)+"Swtc"] == 0){
            window[loclElemStrg_HandSwtc][swtcName_HandSwtc] = 0;
        }
    }
    if (loclElemStrg_HandSwtc == "swtcServ"){
        swtcAreaServ = []; //создаем пустой массив для передачи в Функцию управления
        loclElem = ["Ktch", "Hall"]; //массив содержащий все Locl
        for (i = 0; i <= loclElem.length - 1; i ++){ //цикл формирующий массив из Элементов SwtcSwtc
            swtcAreaServ.push(swtcName_HandSwtc.slice(8, 12) + loclElem[i] + "SwtcSwtc"); //формируем массив из элементов типа lghtHallSwtcSwtc
        }
        handSwtcServ(swtcName_HandSwtc, swtcAreaServ);
    }
    else if (loclElemStrg_HandSwtc == "lghtHall"){ //проверяем расположение элемента выключателя
        if (lghtHall["lghtHallSwtcSwtc"] == 0 || swtcServ["swtcServlghtSwtc"] == 0){
            handSwtcOnOf("lghtHallSwtcSwtc", swtcArealghtHall);
        }
        else {
            swtcArealghtHallLghW = swtcArealghtHall.slice(0, 3); //массив Swtc по управлению режимами подсветки Окно
            swtcArealghtHallLgTV = swtcArealghtHall.slice(1, 4); //массив Swtc по управлению режимами подсветки ТВ
            if (swtcArealghtHallLghW.indexOf(swtcName_HandSwtc) != -1){ //проверяем входит ли Swtc в массив управляемых Swtc`ов
                handSwtcSvrl(swtcName_HandSwtc, swtcArealghtHallLghW);
            }
            if (swtcArealghtHallLgTV.indexOf(swtcName_HandSwtc) != -1) {
                handSwtcSvrl(swtcName_HandSwtc, swtcArealghtHallLgTV);
            }
        }
    }
    else if (loclElemStrg_HandSwtc == "lghtKtch"){
        if (lghtKtch["lghtKtchSwtcSwtc"] == 0 || swtcServ["swtcServlghtSwtc"] == 0){ //проверяем состояние главного Swtc`а
            handSwtcOnOf("lghtKtchSwtcSwtc", swtcArealghtKtch);
        }
        else {
            swtcArealghtKtchLghW = swtcArealghtKtch.slice(0, 3); //массив Swtc по управлению режимами подсветки Окно ["lghtKtchSwtcLghW", "lghtKtchSwtcWtfl", "lghtKtchSwtcSond"];
            swtcArealghtKtchLghC = swtcArealghtKtch.slice(1, 5); //массив Swtc по управлению режимами подсветки Пола ["lghtKtchSwtcWtfl", "lghtKtchSwtcSond", "lghtKtchSwtcLghC", "lghtKtchSwtcNgSg"]
            swtcArealghtKtchLghF = swtcArealghtKtch.slice(1, 3); //массив Swtc по управлению режимами подсветки Потолка ["lghtKtchSwtcWtfl", "lghtKtchSwtcSond"]
            swtcArealghtKtchLghF.push(swtcArealghtKtch[6]);
            if (swtcArealghtKtchLghW.indexOf(swtcName_HandSwtc) != -1){
                handSwtcSvrl(swtcName_HandSwtc, swtcArealghtKtchLghW);
            }
            if (swtcArealghtKtchLghC.indexOf(swtcName_HandSwtc) != -1){
                handSwtcSvrl(swtcName_HandSwtc, swtcArealghtKtchLghC);
            }
            if (swtcArealghtKtchLghF.indexOf(swtcName_HandSwtc) != -1){
                 handSwtcSvrl(swtcName_HandSwtc, swtcArealghtKtchLghF);
            }
        }
    }
}
//Функция по управлению всеми SwtcSwtc в Блоке Locl
function handSwtcServ(swtcServName_HandSwtcServ, swtcArea_HandSwtcServ){
    for (i = 0; i <= swtcArea_HandSwtcServ.length - 1; i ++){ //цикл перебора элементов SwtcSwtc
        if (swtcArea_HandSwtcServ[i] == "watrHallSwtcSwtc"){
            continue;
        }
        swtcBoxx_HandSwtcServ = ($(window[swtcArea_HandSwtcServ[i]]).parent().parent());
        loclElemStrg_HandSwtcServ = swtcArea_HandSwtcServ[i].slice(0, 8);
        loclElem_HandSwtcServ = window[loclElemStrg_HandSwtcServ];
         if (swtcServ[swtcServName_HandSwtcServ] != loclElem_HandSwtcServ[swtcArea_HandSwtcServ[i]]){
             if (swtcServ[swtcServName_HandSwtcServ] == 0){ //проверяем значение  элемента в swtcServ
                loclElem_HandSwtcServ[swtcArea_HandSwtcServ[i]] = 0; //изменяем значение элемента в Json на 0
            }
            else if (swtcServ[swtcServName_HandSwtcServ] == 1) {
                loclElem_HandSwtcServ[swtcArea_HandSwtcServ[i]] = 1; //изменяем значение элемента в Json на 1
            }
            swtcBoxxActv(swtcBoxx_HandSwtcServ, loclElemStrg_HandSwtcServ); //Функция активации SwtcBoxx в зависимости от блока к которому относится Swtc
            lvl1ServActv(window[loclElemStrg_HandSwtcServ.slice(0, 4)]); ///Функция активации Блока меню "Размещения" в зависимости от значения элемента Json swtcServ
            setTimeout(sendLoclElem(loclElemStrg_HandSwtcServ, loclElem_HandSwtcServ), 4); //отправляем Json массивы на WEB сервер
        }
    }
}
//Функция по управлению Главным SWTC всех Swtc в блоке, передается Имя Главного Swtc и Массив из управляемых Swtc
function handSwtcOnOf(swtcSwtcName_HandSwtcOnOf, swtcArea_HandSwtcOnOf){
    loclElem_HandSwtcOnOf = window[swtcSwtcName_HandSwtcOnOf.slice(0, 8)]; //получаем объект соответствующего массива json
    for (i = 0; i <= swtcArea_HandSwtcOnOf.length; i ++){ //перебираем элементы в переданном массиве Swtc'ей
        loclElem_HandSwtcOnOf[swtcArea_HandSwtcOnOf[i]] = 0; //всем элементам в соответствующем массиве json назначаем 0
    }
}
//Функция по управлению несолькими Swtc`ми Swtc из массива
function handSwtcSvrl(swtcName_HandSwtcSvrl, swtcArea_HandSwtcSvrl){
    if (swtcArea_HandSwtcSvrl.indexOf(swtcName_HandSwtcSvrl) != -1){ //проверяем активный Swtc на вхождение в переданный массив
        loclElem_HandSwtcSvrl = window[swtcName_HandSwtcSvrl.slice(0, 8)]; //получаем объект соответствующего массива json
        for (i = 0; i <= swtcArea_HandSwtcSvrl.length; i ++){ //перебираем элементы в переданном массиве Swtc`ей
            if (swtcName_HandSwtcSvrl != swtcArea_HandSwtcSvrl[i]){ //проверяем активный Swtc на соответствие с перебираемыми элементами
                loclElem_HandSwtcSvrl[swtcArea_HandSwtcSvrl[i]] = 0; //всем элементам в соответствующем массиве json назначаем 0
            }
        }
    }
}
