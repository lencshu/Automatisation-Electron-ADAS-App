var { ipcRenderer } = require('electron');

var trierIndice = document.querySelector('#indice')

json_versions=[]


$('#btnAllVersions').click(function () {
    ipcRenderer.send("versionGet", 'get');
});

setTimeout(function () {
    ipcRenderer.send("versionGet", 'get');
}, 2000);

ipcRenderer.on('getVersion',function (event,data) {
    json_versions=data;
    // console.log(json_versions);
    var versions = $("#versions");
    $("option", versions).remove();
    $.each(json_versions, function (index, array) {
        var option = "<option value='" + array['id'] + "'>" + array['title'] + "</option>";
        versions.append(option);
    });

    var bugs = $("#bugs");
    $("option", bugs).remove();
    $.each(json_bugs, function (index, array) {
        var option = "<option value='" + array['id'] + "'>" + array['title'] + "</option>";
        bugs.append(option);
    });
})

json_tous = [{ "id": 1, "title": "Tous" }, { "id": 2, "title": "AEB18" }, { "id": 3, "title": "AEB20" }, { "id": 4, "title": "AD1" }, { "id": 5, "title": "AD1evo" }, { "id": 6, "title": "ENVIRONMENT" }, { "id": 7, "title": "ENVIRONMENT AEB" }, { "id": 8, "title": "TRAJAM" }, { "id": 9, "title": "LSS" }, { "id": 10, "title": "ACC" }, { "id": 11, "title": "FusionAssessment" }, { "id": 12, "title": "TSAssessment" }, { "id": 13, "title": "VariousDriving" }];

json_simobj = [{ "id": 1, "title": "Tous" }, { "id": 2, "title": "AEB18" }, { "id": 3, "title": "AEB20" }, { "id": 4, "title": "AD1" }, { "id": 5, "title": "AD1evo" }, { "id": 6, "title": "ENVIRONMENT" }, { "id": 7, "title": "ENVIRONMENT AEB" }, { "id": 8, "title": "TRAJAM" }, { "id": 9, "title": "LSS" }, { "id": 10, "title": "ACC" }];

json_module = [{ "id": 0, "title": "Tous" }, { "id": 1, "title": "Path Prediction Ego" }, { "id": 2, "title": "Ego Tracking" }, { "id": 3, "title": "Lane Assignement" }, { "id": 4, "title": "Lane Fusion" }, { "id": 5, "title": "Path Prediction Object" }, { "id": 6, "title": "Object Tracking" }, { "id": 7, "title": "TSAD" }, { "id": 8, "title": "TSLSS" }, { "id": 9, "title": "TSAEB" }];


json_roulage = [{ "id": 0, "title": "Tous" }, { "id": 1, "title": "FusionAssessment" },
{ "id": 2, "title": "TSAssessment" },
{ "id": 3, "title": "VariousDriving" }];

json_bugs = [{ "id": 0, "title": "Tous" }, { "id": 1, "title": "bug0" }, { "id": 2, "title": "bug1" }, { "id": 3, "title": "bug2" }, { "id": 4, "title": "bug3" }, { "id": 5, "title": "bug4" }, { "id": 6, "title": "bug5" }, { "id": 7, "title": "bug6" }, { "id": 8, "title": "bug7" }, { "id": 9, "title": "bug8" }, { "id": 10, "title": "bug9" }, { "id": 11, "title": "bug10" }, { "id": 12, "title": "bug11" }, { "id": 13, "title": "bug12" }, { "id": 14, "title": "bug13" }, { "id": 15, "title": "bug14" }, { "id": 16, "title": "bug15" }, { "id": 17, "title": "bug16" }, { "id": 18, "title": "bug17" }, { "id": 19, "title": "bug18" }, { "id": 20, "title": "bug19" }, { "id": 21, "title": "bug20" }, { "id": 22, "title": "bug21" }, { "id": 23, "title": "bug22" }, { "id": 24, "title": "bug23" }, { "id": 25, "title": "bug24" }, { "id": 26, "title": "bug25" }, { "id": 27, "title": "bug26" }, { "id": 28, "title": "bug27" }, { "id": 29, "title": "bug28" }, { "id": 30, "title": "bug29" }, { "id": 31, "title": "bug30" }, { "id": 32, "title": "bug31" }, { "id": 33, "title": "bug32" }, { "id": 34, "title": "bug33" }, { "id": 35, "title": "bug34" }, { "id": 36, "title": "bug35" }, { "id": 37, "title": "bug36" }, { "id": 38, "title": "bug37" }, { "id": 39, "title": "bug38" }, { "id": 40, "title": "bug39" }, { "id": 41, "title": "bug40" }, { "id": 42, "title": "bug41" }, { "id": 43, "title": "bug42" }];

json_roulage_module = [];


function getSelectScenerio() {
    //获取后台json数据
    // console.log($("#type").val())
    var Fname = $("#type").val()
    var scenerio = $("#scenerio");
    var module = $("#module");
    
    $("option", scenerio).remove(); //清空原有的选项
    $("option", module).remove(); //清空原有的选项 
    if (Fname == 1) {
        $.each(json_tous, function (index, array) {
            var option = "<option value='" + array['id'] + "'>" + array['title'] + "</option>";
            scenerio.append(option);
        });
    }

    if (Fname == 2) {
        $.each(json_simobj, function (index, array) {
            var option = "<option value='" + array['id'] + "'>" + array['title'] + "</option>";
            scenerio.append(option);
        });
    }

    if (Fname == 3) {
        $.each(json_roulage, function (index, array) {
            var option = "<option value='" + array['id'] + "'>" + array['title'] + "</option>";
            scenerio.append(option);
        });
    }

    $.each(json_module, function (index, array) {
        var option = "<option value='" + array['id'] + "'>" + array['title'] + "</option>";
        module.append(option);
    });


};




// 选择1级菜单选项触发事件
$(function () {
    getSelectScenerio();
    $("#type").change(function () {
        getSelectScenerio();
    });
});

// 选择2级菜单选项触发事件
// $(function () {
//     // getSelectScenerio();
//     $("#scenerio").change(function () {
//         // getSelectScenerio();
//         console.log($("#scenerio").val()[0]);
//     });
// }); 

// 点击添加，获取选中选项的value和text
$(document).ready(function () {
    $("#add").click(function () {
        var result = $("#result");
        $("#scenerio option:selected").each(function () {
            // console.log($("#type option:selected").text() + ',' + $("#scenerio option:selected").text() + ',' + $("#module option:selected").text());
            // var option = "<option value='" + $(this).val() + "' selected=\"selected\">" + $(this).text() + "</option>";
            // $("option", result).remove();
            var option = "<option value='" + $("#type option:selected").text() + ',' + $("#scenerio option:selected").text() + ',' + $("#module option:selected").text() + ',' + $("#bugs option:selected").text() + "' >" + $("#type option:selected").text() + '-->' + $("#scenerio option:selected").text() + '-->' + $("#module option:selected").text() + '-->' +$("#bugs option:selected").text() + "</option>";
            result.append(option);
            trierIndice.innerHTML = '<div class="alert alert-primary alert-dismissible fade show" role="alert" style="text-align: center;">La condition de tri: <strong>' + $("#type option:selected").text() + "->" + $("#scenerio option:selected").text() + "->" + $("#module option:selected").text() + "->"  + $("#bugs option:selected").text() + '</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
            //==========Go 之后直接显示结果
            // ipcRenderer.send("main_receiver", $("#type option:selected").text() + "," + $("#scenerio option:selected").text() + "," + $("#module option:selected").text());
        });
    });
});