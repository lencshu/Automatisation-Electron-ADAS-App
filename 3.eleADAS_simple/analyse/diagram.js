var diaDom = document.querySelector("#diagram");
var dibDom = document.querySelector("#dibgram");
var dicDom = document.querySelector("#dicgram");
var didDom = document.querySelector('#didgram');
var dizDom = document.querySelector('#diz');
var difDom = document.querySelector('#difgram');
var proRoDom = document.querySelector('#progress_roulage');
var proSnDom = document.querySelector('#progress_sn');
var proSpDom = document.querySelector('#progress_sp');
var { ipcRenderer } = require('electron');

// 基于准备好的dom，初始化echarts实例
var dia_Roulage = echarts.init(diaDom);
var pie_Roulage = echarts.init(dibDom);
var dia_Sn = echarts.init(dicDom);
var pie_Sn = echarts.init(didDom);
console.log(dizDom);
console.log(didDom);
var dia_Sp = echarts.init(dizDom);
var pie_Sp = echarts.init(difDom);
var dataAnalyse_all=[];



var columns = ['bug0', 'bug1', 'bug2', 'bug3', 'bug4', 'bug5', 'bug6', 'bug7', 'bug8', 'bug9', 'bug10', 'bug11', 'bug12', 'bug13', 'bug14', 'bug16', 'bug17', 'bug19', 'bug20', 'bug21', 'bug22', 'bug24', 'bug25', 'bug26', 'bug27', 'bug28', 'bug29', 'bug30', 'bug31', 'bug32', 'bug35', 'bug36', 'bug37', 'bug38', 'bug39', 'bug40', 'bug41'];

var columnsDescri = ["Inappropriate Lines Number :Bug N°0", "Fluctuation of Lines :Bug N°1", "Incorrect Ego LaneAssignement:Bug N°2", "Incorrect Objet LaneAssignement:Bug N°3", "Disappearance of EgoPath:Bug N°4", "Fluctuation of EgoPath :Bug N°5", "The EgoPath does not follow the curves :Bug N°6", "Disappearance of ObjectPath:Bug N°7", "Inappropriate ObjectPath Modeling:Bug N°8", "Incorrect  Ego's speed:Bug N°9", "Incorrect Object's speed :Bug N°10", "Double detected object :Bug N°11", "Undetected object by Fusion :Bug N°12", "False AEB detection :Bug N°13", "False ACC detection :Bug N°14", "Inappropriate CIPV /TTC indicator :Bug N°16", "Incorrect ACC Number [XX]:Bug N°17", "AEB Target fluctuation :Bug N°19", "PB Statut:Bug N°20", "False positive object detection :Bug N°21", "Inappropriate Lines modeling:Bug N°22", "Undetected AEB target:Bug N°24", "Undetected ACC target:Bug N°25", "Unseen detected object :Bug N°26", "Incorrect ObjectPath for static object :Bug N°27", "Fluctuation of object path:Bug N°28", "ACC Target fluctuation :Bug N°29", "Inappropriate object position:Bug N°30", "EgoPath is a circle-like :Bug N°31", "Object Fluctuation :Bug N°32", "Undetected object by sensors:Bug N°35", "Fusion Crash:Bug N°36", "Undetected object by sensors:Bug N°37", "Incorrect EgoPath :Bug N°38", "Bad Maneuver Prediction :Bug N°39", "Incorrect anchor point :Bug N°40", "Bad bounding box modeling :Bug N°41"];
var pieDescri = ["Bug N°0: Inappropriate Lines Number", "Bug N°1: Fluctuation of Lines", "Bug N°2: Incorrect Ego LaneAssignement", "Bug N°3: Incorrect Objet LaneAssignement", "Bug N°4: Disappearance of EgoPath", "Bug N°5: Fluctuation of EgoPath", "Bug N°6: The EgoPath does not follow the curves", "Bug N°7: Disappearance of ObjectPath", "Bug N°8: Inappropriate ObjectPath Modeling", "Bug N°9: Incorrect  Ego's speed", "Bug N°10: Incorrect Object's speed", "Bug N°11: Double detected object", "Bug N°12: Undetected object by Fusion", "Bug N°13: False AEB detection", "Bug N°14: False ACC detection", "Bug N°16: Inappropriate CIPV /TTC indicator", "Bug N°17: Incorrect ACC Number [XX]", "Bug N°19: AEB Target fluctuation", "Bug N°20: PB Statut", "Bug N°21: False positive object detection", "Bug N°22: Inappropriate Lines modeling", "Bug N°24: Undetected AEB target", "Bug N°25: Undetected ACC target", "Bug N°26: Unseen detected object", "Bug N°27: Incorrect ObjectPath for static object", "Bug N°28: Fluctuation of object path", "Bug N°29: ACC Target fluctuation", "Bug N°30: Inappropriate object position", "Bug N°31: EgoPath is a circle-like", "Bug N°32: Object Fluctuation", "Bug N°35: Undetected object by sensors", "Bug N°36: Fusion Crash", "Bug N°37: Undetected object by sensors", "Bug N°38: Incorrect EgoPath", "Bug N°39: Bad Maneuver Prediction", "Bug N°40: Incorrect anchor point", "Bug N°41: Bad bounding box modeling"];

// var datas = new Array();


function creatTable(NumData, data, nameTable) {
    var dataTable = new Array();
    for (var i in columns) {
        // console.log(columns[i]);
        // console.log(data[0][columns[i]]);
        dataTable.push(data[NumData][columns[i]]);
    }
    var option = {
        title: {
            text: nameTable
        },
        tooltip: {},
        legend: {
            data: nameTable
        },
        xAxis: {
            data: columnsDescri
        },
        yAxis: {},
        series: [{
            name: nameTable,
            type: 'bar',
            data: dataTable
        }]
    };
    return option;
}

function creatThreeTable(NumData, data, nameTable) {
    var dataTable_Bugs = new Array();
    var dataTable_BugScenario = new Array();
    var dataTable_BugHeure = new Array();
    var dataTable_BugKm = new Array();
    for (var i in columns) {
        // console.log(columns[i]);
        // console.log(data[0][columns[i]]);
        dataTable_Bugs.push(data[NumData][columns[i]]);
        dataTable_BugScenario.push(data[NumData + 1][columns[i]]);
        dataTable_BugHeure.push(data[NumData + 2][columns[i]]);
        dataTable_BugKm.push(data[NumData + 3][columns[i]]);
    }
    // console.log(dataTable_Bugs);

    var option = {
        title: {
            text: nameTable,
            subtext: 'V1830'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['Bugs', 'Bug per Scenario', 'Bug per hour', 'Bug per Km']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        yAxis: {
            type: 'category',
            data: columnsDescri
        },
        series: [
            {
                name: 'Bugs',
                type: 'bar',
                data: dataTable_Bugs
            },
            {
                name: 'Bug per Scenario',
                type: 'bar',
                data: dataTable_BugScenario
            },
            {
                name: 'Bug per Heure',
                type: 'bar',
                data: dataTable_BugHeure
            },
            {
                name: 'Bug per Km',
                type: 'bar',
                data: dataTable_BugKm
            }
        ]
    };
    // console.log(dataTable_BugHeure);
    // console.log(option);
    return option;
};

function creatPieChart(NumData, data, nameTable) {
    var dataTable_BugBugs = new Array();
    var dataToUse = [];
    var jj = {};

    for (var i in columns) {
        dataTable_BugBugs.push(data[NumData][columns[i]]);
    };
    for (var i = 0; i < dataTable_BugBugs.length; i++) {
        if (dataTable_BugBugs[i] == 0) continue;
        jj.i = {};
        jj.i.value = dataTable_BugBugs[i] * 100;
        jj.i.name = pieDescri[i];
        // console.log(jj);
        dataToUse.push(jj.i);
        // let myJson = JSON.stringify(json);
        // let myJson = json
    };
    // console.log(dataToUse);
    // console.log(dataTable_BugBugs)
    // console.log(dataToUse);

    var option = {
        backgroundColor: '#2c343c',

        title: {
            text: nameTable,
            left: 'center',
            top: 20,
            textStyle: {
                color: '#ccc'
            }
        },

        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },

        visualMap: {
            show: false,
            min: 0.1,
            max: 20,
            inRange: {
                colorLightness: [0, 1]
            }
        },
        series: [
            {
                name: nameTable,
                type: 'pie',
                radius: '55%',
                center: ['50%', '50%'],
                data: dataToUse.sort(function (a, b) { return a.value - b.value; }),
                // data: dataTest.sort(function (a, b) { return a.value - b.value; }),

                roseType: 'radius',
                label: {
                    normal: {
                        textStyle: {
                            color: 'rgba(255, 255, 255, 0.3)'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        lineStyle: {
                            color: 'rgba(255, 255, 255, 0.3)'
                        },
                        smooth: 0.2,
                        length: 10,
                        length2: 20
                    }
                },
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },

                animationType: 'scale',
                animationEasing: 'elasticOut',
                animationDelay: function (idx) {
                    return Math.random() * 20;
                }
            }
        ]
    };
    console.log(option);
    return option;

}

function progressBar(NumData, data, nameTable) {
    var datasToIn = "<h1 class=\"display-4\">" + nameTable + "</h1> <p class=\"lead\">Successful Rate: " + data[NumData]["success_rate"] * 100 + "%</p> <div class=\"progress\" ><div class=\"progress-bar progress-bar-striped bg-danger progress-bar-animated\" role=\"progressbar\" aria-valuenow=\"100\" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width:" + data[NumData]["success_rate"] * 40 + "%\"></div></div>"

    // console.log(datasToIn)
    return datasToIn
}


//==>==>==>==>==>==>==>==>==>主程序开始<==<==<==<==<==<==<==<==


ipcRenderer.on('dataAnalyse_all', function (event, data) {
    dataAnalyse_all=data;
})


ipcRenderer.on('dataAnalyse_select', function (event, data) {
    // console.log(data[0]['version']);

    // diaDom.innerHTML = "";
    // dibDom.innerHTML = "";
    // dicDom.innerHTML = "";
    // didDom.innerHTML = "";
    var jsonSelected=[];
    // console.log($("#versions option:selected").text());
    for (let i = 0; i < dataAnalyse_all.length; i++) {
        if (dataAnalyse_all[i]["version"] == data) {
            // console.log(dataAnalyse_all[i]);
            jsonSelected.push(dataAnalyse_all[i]);
      }
    }
    // console.log(jsonSelected);

//Roulage
    proRoDom.innerHTML = progressBar(0, jsonSelected, 'Prototype');
    var option_Roulage = creatThreeTable(0, jsonSelected, 'Prototype');
    dia_Roulage.setOption(option_Roulage, true);

    var option_Roulage_pie = creatPieChart(4, jsonSelected, 'Prototype: the quantity of each bug out of all');
    pie_Roulage.setOption(option_Roulage_pie, true);

    //Simobj-Normal
    // if (jsonSelected[5]['version'] == '0') {

    proSnDom.innerHTML = progressBar(5, jsonSelected, 'SimObject');
    var option_Sn = creatThreeTable(5, jsonSelected, 'SimObject');
    dia_Sn.setOption(option_Sn, true);

    var option_Sn_pie = creatPieChart(9, jsonSelected, 'SimObject: the quantity of each bug out of all');
    pie_Sn.setOption(option_Sn_pie, true);

    console.log(jsonSelected.length);
    //Simobj-Parfait
    if (jsonSelected.length <= 10) {
        dieDom.innerHTML = "";
        difDom.innerHTML = "";
        proSpDom.innerHTML = "<h1 class=\"display-4\">No data of Simobj-Parfait</h1> <div class=\"progress\" ><div class=\"progress-bar progress-bar-striped bg-danger progress-bar-animated\" role=\"progressbar\" aria-valuenow=\"100\" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: 100%\"></div></div>";


    } else {
        proSpDom.innerHTML = progressBar(10, jsonSelected, 'SimObject - Perfect Sensors');
        var option_Sp = creatThreeTable(10, jsonSelected, 'SimObject - Perfect Sensors');
        dia_Sp.setOption(option_Sp, true);

        var option_Sp_pie = creatPieChart(14, jsonSelected, 'SimObject - Perfect Sensors: the quantity of each bug out of all');
        pie_Sp.setOption(option_Sp_pie, true);
    }

});