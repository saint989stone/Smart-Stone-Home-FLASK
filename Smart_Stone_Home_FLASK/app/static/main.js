$(document).ready(function() {

    //Функция обновления данных JSON по времени и активации swtc и indc
    function strt(){
        setTimeout(function(){
            loadPerd();
            sttsActv();
            strt();
        }, 10000);
    }
    loadOnce();
    strt();

    $(".main").hover(mainActv, main);
    $(".lvl1").hover(lvl1Actv, lvl1);
    $(".swtcBoxx").click(reglActv);
});

//Функция активации Блока "Статуса"
function sttsActv(){
    sttsElem = $("#stts").children(); //Переменная хранения объектов Элементов блока "Статуса"
    sttsElemStrg = String(sttsElem.children().attr("id"));
    sttsElem.each(function () {
        if (sttsElemStrg.slice(8, 12) == "Text"){
            loclElem = window[loclElemStrg];
            indcNameType = sttsElemStrg.slice(12);
            if (indcNameType == "Temp"){
                $(this).text(loclElem[sttsElemStrg] + " °C");
            }
            else if (indcNameType == "Hmdt"){
                $(this).text(loclElem[sttsElemStrg] + " %");
            }
        }
    });
}

//Функция активации Блока "Главного" меню
function main(){
    $(this).animate({backgroundColor: "#dbdbdb"}, 500);
    $(this).children().first().animate({color: "#2b2b2b"}, 500);
    $(this).children().filter(".lvl1Serv").slideUp(500);
    $(this).children().filter(".lvl1").slideUp(500);
}

//Функция активации Блока меню "Система"
function mainActv(){
    $(this).animate({backgroundColor: "#9c9c9c"}, 500);
    $(this).children().first().animate({color: "#dbdbdb"}, 500);
    $(this).children().filter(".lvl1Serv").slideDown(500);
    lvl1ServActv(this);
}

//Функция дезактивации Блока меню "Размещения" и сворачивания Блока меню "Управления"
function lvl1(){
    //loadData(String($(this).attr("id")));
    $(this).animate({backgroundColor: "#dbdbdb"}, 500);
    $(this).children().first().animate({color: "#2b2b2b"}, 500);
    $(this).children().filter(".lvl1").slideUp(500);
    $(this).children().filter(".lvl2").slideUp(500);
}
//Функция активации Блока меню "Размещения" и разворачивания Блока меню "Управления"
function lvl1Actv(){
    loadLoclElem(String($(this).attr("id")));
    $(this).animate({backgroundColor: "#9c9c9c"}, 500);
    $(this).children().first().animate({color: "#dbdbdb"}, 500);
    $(this).children().filter(".lvl1").slideDown(500);
    $(this).children().filter(".lvl2").slideDown(500);
}
//Функция активации Блока меню "Размещения" в зависимости от значения элемента Json swtcServ
function lvl1ServActv(mainElem) {
    swtcServStrg_lvl1Serv = "swtcServ" + String($(mainElem).attr("id") + "Swtc"); //формируем имя ServSwtc
    loclElemStrg_lvl1Serv = swtcServStrg_lvl1Serv.slice(0, 8); //формируем имя соответствующего JSON массива
    loclElem = window[loclElemStrg_lvl1Serv]; //получаем JSON массив
    swtcActv(loclElemStrg_lvl1Serv);
    if (loclElem[swtcServStrg_lvl1Serv] == 0){ //дезактивируем соответствующий блок lvl1
        $(mainElem).children().filter(".lvl1").slideUp(500);
    }
    else if (loclElem[swtcServStrg_lvl1Serv] == 1) { //активируем соответствующий блок lvl1
        $(mainElem).children().filter(".lvl1").slideDown(500);
    }
}

//Функция активации Блока "Регулировок"
function reglActv(){
    swtcBlckElem = $(this).parent(); //this = swtcBoxx Получаем родительский
    elemEventClass = String($(event.target).attr("class")); //получаем класс элемента на котором сработало событие
    loclElemStrg_Regl = (String($(this).children().attr("for"))).slice(0, 8); //получаем расположение элемента в текстовом формате
    loclElem_Regl = window[loclElemStrg_Regl]; //получаем расположение элемента(lghtKtch, lghtHall) для передачи в соответствующий массив
    swtcName_Regl = String($(this).children().attr("for")); //получаем имя элемента Переключателя
    swtcVall_Regl = String($(this).children().children().filter("input").prop("checked")); //переменная для хранения значения переключателя true / false
    swtcVallBool_Regl = (swtcVall_Regl == "true") ? 1 : 0; //переменная для хранения значения переключателя 1 / 0
    loclElem_Regl[swtcName_Regl] = swtcVallBool_Regl; //изменение значения в соответствующем массиве
    // handSwtc(swtcName_Regl, loclElemStrg_Regl); //функция hand управления неактивными переключателями
    swtcBoxxActv(this, loclElemStrg_Regl);
    if (elemEventClass == "checkbox") {
        sendLoclElem(loclElemStrg_Regl, loclElem_Regl);
    }
}

//Функция активации Блока меню "Размещения" в зависимости от значения элемента Json swtcServ
function lvl1ServActv(mainElem) {
    swtcServStrg_lvl1Serv = "swtcServ" + String($(mainElem).attr("id") + "Swtc");
    loclElemStrg_lvl1Serv = swtcServStrg_lvl1Serv.slice(0, 8);
    loclElem = window[loclElemStrg_lvl1Serv];
    swtcActv(loclElemStrg_lvl1Serv);
    if (loclElem[swtcServStrg_lvl1Serv] == 0){
        $(mainElem).children().filter(".lvl1").slideUp(500);
        }
    else if (loclElem[swtcServStrg_lvl1Serv] == 1){
        $(mainElem).children().filter(".lvl1").slideDown(500);
    }
}

//Функция которая определяет к какому блоку (lght, scrt и т.д.) относится Swtc и передает SwtcBoxx соответствующего Swtc, функциям активации соотвествующих элементов
function swtcBoxxActv(swtcBoxx_SwtcBoxx, loclElemStrg_SwtcBoxx){
    if (["clmt", "scrt", "fire", "watr", "mntg"].indexOf(loclElemStrg_SwtcBoxx.slice(0, 4)) != -1){ //проверяем выключатель на соответствие к определенному блоку системы (lght, scrt, и т.д)
        indcActv(swtcBoxx_SwtcBoxx);
        }
    else if(["lght"].indexOf(loclElemStrg_SwtcBoxx.slice(0, 4)) != -1){
        sldrActv(swtcBoxx_SwtcBoxx); //Передаем функции активации блока "Ползунков" объект активного switchBoxия значения Переключателя
    }
}

//Функция активации индикаторов при активации соответствующего Swtc
function indcActv(swtcBoxx_IndcActv){
     swtcName_IndcActv = String($(swtcBoxx_IndcActv).children().attr("for")); //получаем имя Swtc
     loclElemStrg_IndcActv = swtcName_IndcActv.slice(0, 8); //получаем расположение Swtc scrtHall, scrtKtch
     loclElem_IndcActv = window[loclElemStrg_IndcActv]; //получаем соответствующий json массив
     alrmName_IndcActv = loclElemStrg_IndcActv + "AlrmBuzz"; //получаем Элемент указывающий на тревогу во всем блоке
     reglElemBlck_IndcActv = $(swtcBoxx_IndcActv).parent().parent(); //получаем элемент Regl класса lvl3
     indcElemBlck_IndcActv = $(reglElemBlck_IndcActv).children().slice(1); //получаем все indcBlck в соотвествующем блоке
     indcElemBlck_IndcActv.each(function () { //перебираем элементы indcBlck
         indcElem_IndcActv = ($(this).children().children()); //получаем элемент indc
         indcElemClss_IndcActv = indcElem_IndcActv.attr("class");
         indcName_IndcActv = (String($(indcElem_IndcActv).attr("id"))); //Строковая переменная хранения названия элем
         main_IndcActv = $(indcElem_IndcActv).parent().parent().parent().parent().parent().parent();
         lvl1_IndcActv = $(indcElem_IndcActv).parent().parent().parent().parent().parent();
         if (indcElemClss_IndcActv == "indc"){
            if (loclElem_IndcActv[swtcName_IndcActv] == 1 && loclElem_IndcActv[indcName_IndcActv] == 0){ //если Swtc системы включен и нет тревоги
                loclElem_IndcActv[alrmName_IndcActv] = 1; //Элемент указывающий на тревогу во всем блоке в выкл состояние
                loclElem_IndcActv[indcName_IndcActv] = 1; //Элемент индикатора в состояние вкл
            }
            else if (loclElem_IndcActv[swtcName_IndcActv] == 1 && loclElem_IndcActv[indcName_IndcActv] == 1){ //если Swtc системы включен и нет тревоги
                loclElem_IndcActv[alrmName_IndcActv] = 1; //Элемент указывающий на тревогу во всем блоке в выкл состояние
            }
            else if (loclElem_IndcActv[swtcName_IndcActv] == 1 && loclElem_IndcActv[indcName_IndcActv] == 2){ //если Swtc системы включен и есть тревога
                main_IndcActv.animate({backgroundColor:"#ad0000"}, 500); //в случае тревоги родительские элементы окрашены красным
                lvl1_IndcActv.animate({backgroundColor:"#ad0000"}, 500);
            }
            else if (loclElem_IndcActv[swtcName_IndcActv] == 1 && loclElem_IndcActv[indcName_IndcActv] == 3){ //если Swtc системы включен и есть неисправность
                main_IndcActv.animate({backgroundColor:"#2b2b2b"}, 500); //в случае тревоги родительские элементы окрашены красным
                lvl1_IndcActv.animate({backgroundColor:"#2b2b2b"}, 500);
            }
            else if (loclElem_IndcActv[swtcName_IndcActv] == 0){ //если Swtc системы выключен и нет тревоги
                loclElem_IndcActv[alrmName_IndcActv] = 0; //Элемент указывающий на тревогу во всем блоке в выкл состояние
                loclElem_IndcActv[indcName_IndcActv] = 0; //Элемент индикатора в состояние выкл
            }
            indcActvColr(indcElem_IndcActv, loclElemStrg_IndcActv, indcName_IndcActv); //передаем функции отвечающей за управление цветом индикаторов
         }
         else if (indcElemClss_IndcActv == "text"){
             indcNameType_IndcActv = indcName_IndcActv.slice(12); //определяем тип элемента типа Text (Temp или Hmdt)
             if (indcNameType_IndcActv == "Temp"){
                 $(indcElem_IndcActv).text(loclElem_IndcActv[indcName_IndcActv] + " °C");
             }
             else if (indcNameType_IndcActv == "Hmdt"){
                 $(indcElem_IndcActv).text(loclElem_IndcActv[indcName_IndcActv] + " %");
             }
         }
    });
}

//Функция активации индикаторов
function indcActvColr(sttsElem_Indc, loclElemStrg_Indc, sttsElemStrg_Indc){
    loclElem_Indc = window[loclElemStrg_Indc];
    if (loclElem_Indc[sttsElemStrg_Indc] == 1){ //1. "Взят" Зеленый цвет значение в соответствующем Json "1". Соответствующий swtc включен
        sttsElem_Indc.animate({backgroundColor: "#00ad00"}, 500);
    }
    else if (loclElem_Indc[sttsElemStrg_Indc] == 0){ //0. "Снят" Желтый цвет значение в соответствующем Json "0". Соответствующий swtc выключен
        sttsElem_Indc.animate({backgroundColor: "#adad00"}, 500);
    }
    else if (loclElem_Indc[sttsElemStrg_Indc] == 2){ //2. "Тревога" Красный цвет значение в соответствующем Json "2".
        sttsElem_Indc.animate({backgroundColor: "#ad0000"}, 500);
    }
    else if (loclElem_Indc[sttsElemStrg_Indc] == 3){
        sttsElem_Indc.animate({backgroundColor: "#2b2b2b"}, 500);
    }
}

//Функция активации переключателей, запускается из функции loadData
function swtcActv (loclElemStrg_Swtc){
    loclElem_Swtc = window[loclElemStrg_Swtc]; //получаем соответствущий массив по его строковому представлению
    $.each(loclElem_Swtc, function (key, value) { //перебираем элементы массива
        elem = $("#" + key); //формируем объект элемента jquery #lghtKtchBtnnSwtc
        //console.log(key, value);
        if (elem.attr("class") == "checkbox") { //проверяем принадлежность элемента к классу checkbox
            elem.prop("checked", (value == 1) ? true : false); //активируем переключатель в соответствии со значением
            swtcBoxx_Swtc = elem.parent().parent(); //получаем элемент swtcBoxx
            swtcBoxxActv(swtcBoxx_Swtc, loclElemStrg_Swtc);
        }
    });
}

//Функция активации блока "Ползунков"
function sldrActv (swtcBoxx_SldrActv){
    swtcName_SldrActv = String($(swtcBoxx_SldrActv).children().attr("for")); //получаем имя переключателя в соответствующем массиве
    loclElemStrg_SldrActv = swtcName_SldrActv.slice(0, 8); //получаем расположение элемента в текстовом формате
    loclElem_SldrActv = window[loclElemStrg_SldrActv]; //получаем расположение элемента(lghtKtch, lghtHall) для передачи в соответствующий массив
    sldrElem = $(swtcBoxx_SldrActv).parent().next().children(); //переменная хранения объекта Слайдера
    clssElemSldr = (sldrElem.attr("class")); //получаем имя класса для проверки елемента на пренадлежность к Слайдеру
    if (clssElemSldr == "sldrBoxx" || clssElemSldr == "sldrBoxx ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"){ //проверка является ли Слайдер соседним элементом относительно переключателя
        sldrName_SldrActv = String($(sldrElem[0]).attr("id")); //получаем имя слайдера
        if (sldrName_SldrActv.slice(12, 14) == "Lg") { //определяем слайдеры RGB
            sldrActvShdw(loclElem_SldrActv, swtcBoxx_SldrActv, swtcName_SldrActv, sldrName_SldrActv); //передаем функции активации тени элемента swtcBlck
        }
        sldrElem.each(function(){ //перебираем элементы sldrBoxx
            sldrName_SldrActv = String($(this).attr("id")); //получаем имя слайдера
            if (sldrName_SldrActv.slice(12, 14) == "Lg"){ ////определяем слайдеры RGB
                $(this).slider({
                    range: "min",
                    value: Number(loclElem_SldrActv[sldrName_SldrActv]), //задаем начальное значение слайдера из соответсвующего массива
                    min: 0,
                    max: 255,
                    step: 1,
                    slide: function (event, ui) {
                        sldrVall_SldrActv = ui.value; //получаем значение слайдера
                        sldrGett(this, sldrVall_SldrActv); //передаем функции "Получение значения слайдера" активный объект слайдера и его значение
                    }
                });
                if (loclElem_SldrActv[swtcName_SldrActv] == 1) {
                    $(this).slideDown(500);
                }
                else if (loclElem_SldrActv[swtcName_SldrActv] == 0) {
                    $(this).slideUp(500);
                }
            }
            else if (sldrName_SldrActv.slice(12, 14) == "Wt"){ //определяем слайдер Waterfall для определения периода смены света
                sldrName_SldrActv = String($(this).attr("id")); //получаем имя слайдера
                $(this).slider({
                    range: "min",
                    value: Number(loclElem_SldrActv[sldrName_SldrActv]),
                    min: 10,
                    max: 1000,
                    step: 10,
                    slide: function (event, ui) {
                        sldrVall_SldrActv = ui.value;
                        sldrGett(this, sldrVall_SldrActv); //передаем функции "Получение значения слайдера" активный объект слайдера и его значение
                    }
                });
                if (loclElem_SldrActv[swtcName_SldrActv] == 1){
                    $(this).slideDown(500);
                }
                else if (loclElem_SldrActv[swtcName_SldrActv] == 0){
                    $(this).slideUp(500);
                }
            }
        });
    }
}

//Функция получения значений ползунков
function sldrGett(sldrElem_SldrGett, sldrVall_SldrGett){
    sldrName_SldrGett = String($(sldrElem_SldrGett).attr("id")); //получаем id Слайдера
    loclElemStrg_SldrGett = String($(sldrElem_SldrGett).attr("id").slice(0, 8)); //получаем расположение элемента в текстовом формате
    loclElem_SldrGett = window[loclElemStrg_SldrGett]; //получаем расположение элемента(lghtKtch, lghtHall) для передачи в соответствующий массив
    loclElem_SldrGett[sldrName_SldrGett] = sldrVall_SldrGett; //изменение значения элемента в соответствущем массиве

    swtcBoxx_SldrGett = $(sldrElem_SldrGett).parent().prev().children();
    swtcName_SldrGett = String(swtcBoxx_SldrGett.children().attr("for")); //получаем имя элемента Переключателя

    if (sldrName_SldrGett.slice(12, 14) == "Lg"){
        sldrActvShdw(loclElem_SldrGett, swtcBoxx_SldrGett, swtcName_SldrGett, sldrName_SldrGett);
    }
    else if (sldrName_SldrGett.slice(12, 14) == "Wt"){
        sldrActvWtfl(loclElem_SldrGett,  swtcBoxx_SldrGett, swtcName_SldrGett, sldrElem_SldrGett, sldrName_SldrGett);//(loclElem_SldrGett, swtcBoxx_SldrGett, swtcName_SldrGett, sldrName_SldrGett);
    }
    sendLoclElem(loclElemStrg_SldrGett, loclElem_SldrGett); //передаем функции ajax имя соотвествующего массива (url), и данные массива (data)
}

//Функция активации тени блока ползунков lght RGB
function sldrActvShdw(loclElem_SldrActvShdw, swtcBoxx_SldrActvShdw, swtcName_SldrActvShdw, sldrName_SldrActvShdw){
    swtcBlckElem_SldrActvShdw = $(swtcBoxx_SldrActvShdw).parent(); //получаем объект swtcBlck соответствующего swtcBlck
    if (loclElem_SldrActvShdw[swtcName_SldrActvShdw] == 1){ //блок управления тенью Блока меню "Управление" Блока "Ползуноков" проверяем включен ли соответствующий Переключатель
        sldrName_SldrActvShdwR = sldrName_SldrActvShdw.slice(0, 15) + "R"; //формируем имя ключа массива из id слайдера например lghtKtchSldrLgW(R)
        sldrName_SldrActvShdwG = sldrName_SldrActvShdw.slice(0, 15) + "G"; //формируем имя ключа массива из id слайдера например lghtKtchSldrLgW(G)
        sldrName_SldrActvShdwB = sldrName_SldrActvShdw.slice(0, 15) + "B"; //формируем имя ключа массива из id слайдера например lghtKtchSldrLgW(B)
        sldrName_SldrActvShdwW = sldrName_SldrActvShdw.slice(0, 15) + "W"; //формируем имя ключа массива из id слайдера например lghtKtchSldrLgW(W)

        rgbaColr = "0 4em 3em -2em rgba(" + //формируем в текстовом формате параметры css
            String(loclElem_SldrActvShdw[sldrName_SldrActvShdwR]) + ", " +
            String(loclElem_SldrActvShdw[sldrName_SldrActvShdwG]) + ", " +
            String(loclElem_SldrActvShdw[sldrName_SldrActvShdwB]) + ", " + "1)";

        swtcBlckElem_SldrActvShdw.css("box-shadow", rgbaColr); //задаем параметры css тени Блока меню "Управление" Блока "Ползуноков"
    }
    else{
        swtcBlckElem_SldrActvShdw.css("box-shadow", "none"); //отключение тени Блока меню "Управление" Блока "Ползунков"
    }
}

//Функция активации анимации блока ползунка lghtHallSldrWtfl
function sldrActvWtfl(loclElem_SldrActvWtfl,  swtcBoxx_SldrActvWtfl, swtcName_SldrActvWtfl, sldrElem_SldrActvWtfl, sldrName_SldrActvWtfl) {//(loclElem_SldrActvWtfl, swtcBoxx_SldrActvWtfl, swtcName_SldrActvWtfl, sldrName_SldrActvWtfl){
    swtcBlckElem_SldrActvWtfl = $(swtcBoxx_SldrActvWtfl).parent(); //получаем объект swtcBlck соответствующего swtcBlck
    sldrActvWtflColr = ["#f50a00", "#e11e00", "#cd3300", "#aa5500",
        "#00aa55", "#009669", "#00827e", "#006996",
        "#0055aa", "#aa0055", "#be0042", "#d2002e",
        "#e6001b", "#ff0000", "#ff3232", "#ff6464", "#ff9696", "#ffc8c8", "#ffebeb", "#ffffff"]; //массив из цветов
    if (loclElem_SldrActvWtfl[swtcName_SldrActvWtfl] == 1){
        setTimeout(function () {
            for (i in sldrActvWtflColr) {
                $("#" + sldrName_SldrActvWtfl + " .ui-slider-range").animate({backgroundColor: sldrActvWtflColr[i]}, Number(loclElem_SldrActv[sldrName_SldrActv]));
                $("#" + sldrName_SldrActvWtfl + " .ui-slider-handle").animate({borderColor: sldrActvWtflColr[i]}, Number(loclElem_SldrActv[sldrName_SldrActv]));
            }
        }, Number(loclElem_SldrActv[sldrName_SldrActv]));
    }
}

