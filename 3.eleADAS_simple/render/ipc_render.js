//渲染进程给主进程发消息
var {ipcRenderer}=require('electron');
var electron = require('electron').remote;
var { remote } = require('electron');

var menu = electron.Menu;
var dataTable = document.querySelector('#dataTable')
var trierIndice = document.querySelector('#indice')
var allDom = document.querySelector('#getAll');
var selectDom=document.querySelector('#add');
var effaceDom = document.querySelector('#dialog');
var btnAnalyse = document.querySelector('#btnAnalyse');
var btnEvolution = document.querySelector('#btnEvolution');

//==>==>==>==>==>==>==>==>==>定义全局变量<==<==<==<==<==<==<==<==
var dataAll=null;
var column=[];

//显示全部数据
// var column = ["ID", "type", "scenario_type", "sub_scenario_type", "id_senario", "duration", "author", "date", "version", "n_iteration", "time", "bug_number", "description", "ego_distance", "img_path", "img_context_path", "creat_time", "count_in", "modifier_time", "path_prediction_ego", "ego_tracking", "lane_assignement", "lane_fusion", "path_prediction_object", "object_tracking", "tsad", "tslss", "tsaeb", "global_statuts"];

var column_all = ["ID", "type", "scenario_type", "id_senario", "duration", "author", "date", "version", "n_iteration", "time", "bug_number", "ego_distance","path_prediction_ego", "ego_tracking", "lane_assignement", "lane_fusion", "path_prediction_object", "object_tracking", "tsad", "tslss", "tsaeb", "global_statuts"];

var rotateColumn = ['path_prediction_ego', 'ego_tracking', 'lane_assignement', 'lane_fusion', 'path_prediction_object', 'object_tracking', 'tsad', 'tslss', 'tsaeb', 'global_statuts'];






//==>==>==>==>==>==>==>==>==>定义函数<==<==<==<==<==<==<==<==

function findArray(Array,toFind) {
    for(var i in Array){
        if (Array[i] == toFind) return true;
    }
    return false; 
}


function creatTable(data,column) {
    // console.log(data.length);
    if (data.length==0) {
        dataTable.innerHTML = '<div class="container"><div class="alert alert-warning alert-dismissible fade show" role="alert" style="text-align: center;"><strong>Il n\'y pas de cas pour cette condition de tri</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div></div>';
    } else{
        var datas = [];//new Array()
        var datasHead = [];//new Array()
        var datasBody = [];//new Array()
        //自动生成表头
        // datasHead.push("<table id=\"mytable\"><thead><tr>");    
        datasHead.push("<table id=\"my_table\" class=\"table table-bordered table-striped  table-sm thead-light  table-hover\"><thead class=\"fixedThead\"><tr>");
        for (var i in column)
        // for (var i = 0; i < column.length ; i++)
        {
            // datasHead.push('<th style=\"transform: rotate(310deg)\">');
            if (findArray(rotateColumn, column[i])) {
                // console.log("find")
                datasHead.push('<th class=\"rotate\"><div><span>');
                // data.push(',');
                datasHead.push(column[i]);
                // console.log(column[i]);
                datasHead.push('</span></div></th>');
            }
            else {
                // console.log("find noting")
                datasHead.push('<th>');
                // datasHead.push('<th class=\"normal\">');
                // data.push(',');
                datasHead.push(column[i]);
                // console.log(column[i]);
                datasHead.push('</th>');
            }

            // data.push(',');
        }
        datasHead.push("</tr></thead><tbody>");
        // console.log(datasHead);
        //组装表身
        for (var i = data.length - 1; i >= 0; i--) {
            datasBody.push("<tr>");
            var num = new Number(parseFloat(data[i]["ego_distance"].replace(",", ".")));
            data[i]["ego_distance"] = num.toFixed(2);
            for (var k in column) {
                // console.log(data[i][k])
                if (data[i][column[k]] == 'r_ouge') {
                    datasBody.push("<td class=\"bg-danger\">");
                    // console.log("danger");
                    datasBody.push('');

                } else if ((data[i][column[k]] == 'v_ert')) {
                    datasBody.push("<td class=\"bg-success\">");
                    // console.log("danger");
                    datasBody.push('');
                }
                else {
                    datasBody.push("<td>");
                    datasBody.push(data[i][column[k]]);
                }
                datasBody.push("</td>");
                // dataTable.innerHTML = data[i].id_senario;
                // console.log(data[i].id_senario);
            }
            datasBody.push("</tr>");
        }
        datasBody.push("</tbody></table>");
        // console.log(datas.join(''));
        datas = datasHead.concat(datasBody);
        // console.log(datas);
        datasHead = null;
        datasBody = null;
        dataTable.innerHTML = datas.join("");
    // $("#dataTable").remove();
    // $('#dataTable').append(datas.join(""));
    }
    
}

function dataAll_Version() {
var jsonSelected=[];
    // console.log($("#versions option:selected").text());
    var versionSelect = $("#versions option:selected").text();
    for (let i = 0; i < dataAll.length; i++) {
        if (dataAll[i]["version"] == versionSelect) {
          // console.log(dataAnalyse_all[i]);
            jsonSelected.push(dataAll[i]);
        }
    }
    // console.log(jsonSelected);
    // console.log(versionSelect);
    return jsonSelected;
}

function nomPageToDatabaseChange(name) {
    var newName;
    switch (name) {
        case 'SimObject':
            newName ='Simobj_Normal';
            break;
        case 'SimObj Perfect Sensor':
            newName = 'Simobj_Parfait';
            break;
        case 'Path Prediction Ego':
            newName = 'path_prediction_ego';
            break;
        case 'Ego Tracking':
            newName = 'ego_tracking';
            break;
        case 'Lane Assignement':
            newName = 'lane_assignement';
            break;
        case 'Lane Fusion':
            newName = 'lane_fusion';
            break;
        case 'Path Prediction Object':
            newName = 'path_prediction_object';
            break;
        case 'Object Tracking':
            newName = 'object_tracking';
            break;
        case 'TSAD':
            newName = 'tsad';
            break;
        case 'TSLSS':
            newName = 'tslss';
            break;
        case 'TSAEB':
            newName = 'tsaeb';
            break;
        case 'ENVIRONMENT AEB':
            newName = 'ENVIRONMENT_AEB';
            break;
        case 'AD1evo':
            newName = 'AD1_EVO';
            break;

        default:
            newName = name;
    }
    return newName;
}


function dataAll_Select(v,t,s,m,b) {
    var column_Module = ["ID", "type", "scenario_type", "id_senario", "duration", "author", "date", "version", "n_iteration", "time", "bug_number", "ego_distance"];
    var jsonSelected=[];
    // var versionSelect = $("#versions option:selected").text();
    // var typeSelect = $("#type option:selected").text();
    // var scenarioSelect = $("#scenerio option:selected").text();
    // var moduleSelect = $("#module option:selected").text();

    var versionSelect = v;
    var typeSelect = t;
    var scenarioSelect = s;
    var moduleSelect = m;
    var bugSelect = b;

    versionSelect = nomPageToDatabaseChange(versionSelect);
    typeSelect = nomPageToDatabaseChange(typeSelect);
    scenarioSelect = nomPageToDatabaseChange(scenarioSelect);
    moduleSelect = nomPageToDatabaseChange(moduleSelect);
    bugSelect = bugSelect.replace(/bug/, "")
    // console.log(bugSelect)
    // console.log($("#versions option:selected").text());

    // console.log(scenarioSelect);
    // console.log(versionSelect);
    // console.log(typeSelect);
    // console.log(moduleSelect);
    var co = 0;
    for (let i = 0; i < dataAll.length; i++) {
        if (dataAll[i]["version"] == versionSelect) {
            // console.log(dataAll[i]);
            if ((dataAll[i]["type"] == typeSelect) || (typeSelect=='Tous')) {
            // console.log(dataAll[i]);
                if ((dataAll[i]["scenario_type"] == scenarioSelect) || (scenarioSelect == 'Tous')) {
                // console.log(moduleSelect);
                // console.log(dataAll[i][moduleSelect]);
                // console.log(dataAll[i]);
                    // console.log(dataAll[i][moduleSelect]);
                    if ((dataAll[i]["bug_number"] == bugSelect) || (bugSelect == 'Tous')) {
                            if ((dataAll[i][moduleSelect] == 'r_ouge') && (!(moduleSelect == 'Tous'))) {
                            // console.log(dataAll[i]);
                                jsonSelected.push(dataAll[i]);
                                co=1;
                            } else if ( moduleSelect == 'Tous') {
                            // console.log(dataAll[i]);
                                jsonSelected.push(dataAll[i]);
                                column = column_all;
                            }
                        }
                }
            }
        }
    // console.log(jsonSelected);
    // console.log(versionSelect);
    }
            if (co==1) {
                column_Module.push(moduleSelect);
                column_Module.push("global_statuts");
                column = column_Module;
            }

            return jsonSelected;

}




//==>==>==>==>==>==>==>==>==>主程序初始化<==<==<==<==<==<==<==<==
ipcRenderer.on('render_receiver_all', function (event, data) {
    dataAll = data;
    // console.log(dataAll);
    // creatTable(data, column_all);
    // console.log(data);
    // setTimeout(creatTable(data, column), 1000);
})

// bodyDom.onload=function () {
//     ipcRenderer.send('main_receiver', 'this is baodyDom');
// }


//==>==>==>==>==>==>==>==>==>结果选中历史记录重现<==<==<==<==<==<==<==<==

$("#result").change(function () {
    // console.log($(this).val()[0].split(","));
    trierIndice.innerHTML = '<div class="alert alert-primary alert-dismissible fade show" role="alert" style="text-align: center;">La condition de tri: <strong>' + $(this).val()[0].split(",").join("-->") + '</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
    console.log($(this).val()[0]);
    var dataSelected = dataAll_Select($("#versions option:selected").text(), $(this).val()[0].split(",")[0], $(this).val()[0].split(",")[1], $(this).val()[0].split(",")[2], $(this).val()[0].split(",")[3]);
    creatTable(dataSelected, column);
    // ipcRenderer.send("main_receiver", $(this).val()[0]);
});
// console.log($("#type option:selected").text() + "," + $("#scenerio option:selected").text() + "," + $("#module option:selected").text());


//==>==>==>==>==>==>==>==>==>Go按钮按下<==<==<==<==<==<==<==<==
selectDom.onclick = function () {
    var dataSelected = dataAll_Select($("#versions option:selected").text(), $("#type option:selected").text(), $("#scenerio option:selected").text(), $("#module option:selected").text(), $("#bugs option:selected").text());
    // console.log(dataSelected);
    creatTable(dataSelected, column);
}

//==>==>==>==>==>==>==>==>==>All按钮按下<==<==<==<==<==<==<==<==
allDom.onclick = function () {
    //触发广播
    // dataTable.innerHTML ='';
    // ipcRenderer.send('main_receiver', 'this is rendereraaa');
    // console.log(dataAll[0]['version']);
    creatTable(dataAll_Version(), column_all);
    trierIndice.innerHTML = '<div class="alert alert-primary alert-dismissible fade show" role="alert" style="text-align: center;">La condition de tri: <strong> TOUS ! </strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
}

//==>==>==>==>==>==>==>==>==>Analyse窗口交互<==<==<==<==<==<==<==<==

btnAnalyse.onclick = function () {
    // console.log('analyseWindows')
    ipcRenderer.send("analyseWindows", $("#versions option:selected").text());

    // ipcRenderer.send('versionSelect', $("#versions option:selected").text());
}

//==>==>==>==>==>==>==>==>==>Evolution窗口交互<==<==<==<==<==<==<==<==

btnEvolution.onclick = function () {
    // console.log('analyseWindows')
    ipcRenderer.send("evolutionWindows", $("#versions option:selected").text());

    // ipcRenderer.send('versionSelect', $("#versions option:selected").text());
}

//==>==>==>==>==>==>==>==>==>图片点击操作<==<==<==<==<==<==<==<==
// var { ipcRenderer } = require('electron');
var dataTableDom = document.querySelector("#dataTable");
$("#dataTable").bind('DOMNodeInserted', function (e) {
    // alert('element now contains: ' + $(e.target).html()); 
    $("#dataTable tr").click(function () {
        // $(this).addClass('selected').siblings().removeClass('selected');
        // $(this).addClass('table-info').siblings().removeClass('table-info');
        var value = $(this).find('td:first').html();
        // alert(value);
        // console.log(value);
        // alert(path.resolve('./'));
        // imageID=value;     
        // console.log($("#dataTable tr"));
        // const modalPath = path.resolve('C:/Users/gli/Documents/Dropbox/Altran/3.eleADAS_simple/modal.html');
        // win.on('blur', function () { win = null; win.close()})
        if (value != null) {
            ipcRenderer.send('imagesWindow', value);
            ipcRenderer.send('imagesWindow', 'show');
        }
        // win.loadURL(modalPath)

    });
});


//==>==>==>==>==>==>==>==>==>重置表格<==<==<==<==<==<==<==<==
effaceDom.onclick = function () {
    remote.dialog.showMessageBox({
        type: 'info',
        title: 'bug',
        message: 'Effacer tous ?', 
        buttons: ['ok', 'no']
    }, function (index) {
        if (index == 0) {
            dataTableDom.innerHTML = '';
        }
        console.log(index);
    });
}

//==>==>==>==>==>==>==>==>==>错误信息<==<==<==<==<==<==<==<==
ipcRenderer.on('errorsReceive', function (event, data) {
    console.log(data);
    remote.dialog.showMessageBox({
        type: 'info',
        title: 'Error!',
        message: data["code"] + data["errno"] + "\n" + data["path"],
        buttons: ['ok', 'no']
    }, function (index) {
        console.log(index);
    });
})

//==>==>==>==>==>==>==>==>==>成功信息<==<==<==<==<==<==<==<==
ipcRenderer.on('sucReceive', function (event, data) {
    console.log(data);
    remote.dialog.showMessageBox({
        type: 'info',
        title: 'success!',
        message: data,
        buttons: ['ok']
    }, function (index) {
        console.log(index);
    });
})

//==>==>==>==>==>==>==>==>==>右键菜单<==<==<==<==<==<==<==<==

var template = [
    {
        label: 'Save all as HTML',
        click: function () {
            // console.log('Save');
            ipcRenderer.send("saveHtml", [$("#versions option:selected").text(), $("#type option:selected").text(), $("#scenerio option:selected").text(), $("#module option:selected").text()]);
        },
        accelerator: 's',
    },
    {
        label: 'Save weekly report as HTML',
        click: function () {
            // console.log('Save');
            ipcRenderer.send("saveWeekly", [$("#versions option:selected").text(), $("#type option:selected").text(), $("#scenerio option:selected").text(), $("#module option:selected").text()]);
        },
        accelerator: 'w',
    },
    {
        label: 'Save evolution report as HTML',
        click: function () {
            // console.log('Save');
            ipcRenderer.send("saveEvolution", [$("#versions option:selected").text(), $("#type option:selected").text(), $("#scenerio option:selected").text(), $("#module option:selected").text()]);
        },
        accelerator: 'e',
    }]
var m = menu.buildFromTemplate(template);

window.addEventListener('contextmenu', function (e) {
    // alert('1212')
    //阻止默认事件
    e.preventDefault();
    //当前窗口弹出模板
    m.popup({ window: electron.getCurrentWindow() });

}, false)























// sendreplyDom.onclick = function () {
//     var msg = ipcRenderer.sendSync("sendsync", $("#type option:selected").text());
//     creatTable(msg, column);
// // console.log(msg)
// }

/* 备份

ipcRenderer.on('reply',function (event,data) {
    var datas = [];//new Array()
    var datasHead = [];//new Array()
    var datasBody = [];//new Array()
    var column = ['ID', 'scenario_type', 'id_senario', 'duration', 'author', 'date', 'version', 'n_iteration', 'time', 'bug_number', 'path_prediction_ego', 'ego_tracking', 'lane_assignement', 'lane_fusion', 'path_prediction_object', 'object_tracking', 'tsad', 'tslss', 'tsaeb', 'global_statuts', 'ego_distance', 'creat_time'];//'img_path', 'img_context_path',

    //自动生成表头
    datasHead.push("<table id=\"my_table\" class=\"table table-striped table-bordered table-sm table-dark table-hover\"><thead><tr class=\"bg-success\">")
    for (var i in column)
    // for (var i = 0; i < column.length ; i++)
        {
        datasHead.push('<th>');
            // data.push(',');
        datasHead.push(column[i]);
            console.log(column[i]);
        datasHead.push('</th>');
            // data.push(',');
        }
    datasHead.push("</tr></thead><tbody>");
    // console.log(datasHead);
        //组装表身
    for (var i in data)
    {
        datasBody.push("<tr>");
        for (var k in column)
        {
            // console.log(data[i][k])
            datasBody.push("<td>");
            datasBody.push(data[i][column[k]]);
            datasBody.push("</td>");
        // dataTable.innerHTML = data[i].id_senario;
        // console.log(data[i].id_senario);
        }
        datasBody.push("</tr>");
    }
    datasBody.push("</tbody></table>");
    // console.log(datas.join(''));
    datas=datasHead.concat(datasBody);
    console.log(datas);
    datasHead = null;
    datasBody = null;
    dataTable.innerHTML = datas.join("");
})

*/






//发送消息
// var sendDom = document.querySelector('#send');
// sendDom.onclick=function () {
//     // alert('1212')

//     //触发广播
// ipcRenderer.send('sendM','this is renderer');

// }




// //同步通信
// var sendsyncDom=document.querySelector('#sendsync');
// sendsyncDom.onclick=function () {
//     // alert('1212')

//     //触发广播
//     var msg=ipcRenderer.sendSync('sendsync','this is renderer   ccc sync');
// console.log(msg)
// }



    // console.log(data);
    // console.log(data.length); //22
    // for(var a in column)
    // {
    //     co =String(column[a])
    //     console.log(co);
    //     console.log(data[1][column[a]]);
    // } //22
    //直接生成表头
    // datas.push('<table id="my_table" class="table table-striped table-bordered table-sm table-dark table-hover"><thead><tr class="bg-success"><th> No.</th ><th> scenario type</th ><th>Id Senario</th><th>Duration</th><th>Author</th><th>Date</th><th>Version </th><th>N° Iteration </th><th>Time</th><th>Description</th><th>Pathprediction Ego</th><th>EgoTracking</th><th>Lane Assignement</th><th>Lane Fusion</th><th>PathPrediction Object</th><th>Object Tracking</th><th>TSAD</th><th>TSLSS</th><th>TSAEB</th><th>Global Statuts </th><th>ego_distance</th><th>img_path</th><th>img_context_path</th><th>creat_time</th></tr></tr></thead >');