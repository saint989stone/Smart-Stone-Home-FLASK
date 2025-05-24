//Функция отправки данных и получение ответа от сервера
function sendLoclElem(loclElemStrg_Send, loclElem_Send) {
    $.ajax({
        url: loclElemStrg_Send, //адрес запроса
        type: "post", //тип запроса
        cache: false, //В случае значения false браузер не будет кешировать производимый запрос. Кроме этого, это приведет к добавлению строки
        dataType: "json",
        contentType: 'application/json',
        data: JSON.stringify(loclElem_Send),
        success: function (jsonRsps_Send) {
            $.each(jsonRsps_Send, function (key, value) {
                window[key.slice(0, 8)][key] = value; //вносим полученные значения в json объект
            });
        }
    });
    console.log(loclElemStrg_Send.slice(0, 8));
    if (loclElemStrg_Send.slice(0, 8) == "swtcServ"){
        console.log("Yes");
        loadPerd();
    }
    else{
        swtcActv(loclElemStrg_Send);
    }
}

//Функция отправки запроса на получения значений элементов
function loadLoclElem(loclElemStrg_Load) {
    urll = "load/" + loclElemStrg_Load; //формируем url вида "/load_lghtKtch"
    $.ajax({
        url: urll,
        type: "post",
        cache: false,
        dataType: "json",
        success: function (jsonRsps_Load) {
            $.each(jsonRsps_Load, function (key, value) { //перебираем значения объекта
                window[key.slice(0, 8)][key] = value; //вносим полученные значения в json объект
            });
        }
    });
    swtcActv(loclElemStrg_Load);
}
function loadPerd(){
    urll = "loadPerd";
    $.ajax({
        url: urll,
        type: "post",
        cache: false,
        dataType: "json",
        success: function (jsonRsps_Load) {
            $.each(jsonRsps_Load, function (key, value) { //перебираем значения объекта
                window[key.slice(0, 8)][key] = value; //вносим полученные значения в json объект
            });
        }
    });
    loclElemStrgArea = ["swtcServ", "scrtKtch", "scrtHall", "fireKtch", "fireHall", "watrKtch", "mntgKtch", "mntgHall"];
    for (i = 0; i <= loclElemStrgArea.length - 1; i++){
        swtcActv(loclElemStrgArea[i]);
    }
}
function loadOnce(){
    urll = "loadOnce";
    $.ajax({
        url: urll,
        type: "post",
        cache: false,
        dataType: "json",
        success: function (jsonRsps_Load) {
            $.each(jsonRsps_Load, function (key, value) { //перебираем значения объекта
                window[key.slice(0, 8)][key] = value; //вносим полученные значения в json объект
            });
        }
    });
    loclElemStrgArea = ["lghtHall", "lghtKtch"];
    for (i = 0; i <= loclElemStrgArea.length - 1; i++){
        swtcActv(loclElemStrgArea[i]);
    }
}

