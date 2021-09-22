var electron = require('electron').remote;
var menu = electron.Menu;
var { ipcRenderer } = require('electron');




var template = [
    // {
    //     label: "trier par module",
    //     // accelerator: 'e',
    //     submenu: [{ label: 'Tous' },
    //     { label: 'ACC' },
    //     { label: 'AEB18' },
    //     { label: 'AEB20' },
    //     { label: 'AD1' },
    //     { label: 'AD1evo' },
    //     { label: 'ENVIRONMENT' },
    //     { label: 'ENVIRONMENT AEB' },
    //     { label: 'TRAJAM' },
    //     { label: 'LSS' },
    //     { label: 'FusionAssessment' },
    //     { label: 'TSAssessment' },
    //     { label: 'VariousDriving' },
    //     ]
    // },
    // {
    //     label: "trier par scenerio",
    //     // accelerator: 'o',
    //     submenu: [{ label: 'Tous' },
    //     { label: 'Pathprediction Ego' },
    //     { label: 'EgoTracking' },
    //     { label: 'Lane Assignement' },
    //     { label: 'Lane Fusion' },
    //     { label: 'PathPrediction Object' },
    //     { label: 'Object Tracking' },
    //     { label: 'TSAD' },
    //     { label: 'TSLSS' },
    //     { label: 'TSAEB' },
    //     ]
    // },
    {
        label: 'Save as HTML',
        click: function () {
            // console.log('Save');
            ipcRenderer.send("saveHtml", 'save');
        },
        accelerator: 's',
    },


//===>demo
    // {
    //     label: "trier par module",
    //     submenu: [
    //         {
    //             label: '新建文件',
    //             click: function () {
    //                 console.log('新建');
    //             }
    //         },

    //         {
    //             label: '新建窗口',
    //             accelerator: 'ctrl+n',
    //         },
    //     ]
    // },
    // {
    //     label: "trier par senario",
    // },
]

var m = menu.buildFromTemplate(template);

// menu.setApplicationMenu(m);

//右键

window.addEventListener('contextmenu', function (e) {
    // alert('1212')
    //阻止默认事件
    e.preventDefault();
    //当前窗口弹出模板
    m.popup({ window: electron.getCurrentWindow() });

}, false)