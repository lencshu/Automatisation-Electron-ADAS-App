var { ipcRenderer } = require('electron');
var {remote}=require('electron');
// const BrowserWindow = require('electron').remote.BrowserWindow
// const path = require('path')


var effaceDom=document.querySelector('#dialog');

var dataTableDom = document.querySelector("#dataTable");
// var imgeID;
// imgePath = './Database/imgs_log/' + imgeID+'*'
var btnAnalyse = document.querySelector('#btnAnalyse');


//==>图片点击操作
$("#dataTable").bind('DOMNodeInserted', function (e) {
    // alert('element now contains: ' + $(e.target).html()); 
    $("#dataTable tr").click(function () {
        // $(this).addClass('selected').siblings().removeClass('selected');
        // $(this).addClass('table-info').siblings().removeClass('table-info');
        var value = $(this).find('td:first').html();
        // alert(value);
        console.log(value);
        // alert(path.resolve('./'));
        // imageID=value;     
        // console.log($("#dataTable tr"));
        // const modalPath = path.resolve('C:/Users/gli/Documents/Dropbox/Altran/3.eleADAS_simple/modal.html');
        // win.on('blur', function () { win = null; win.close()})
        if (value !=null) {
            ipcRenderer.send('imagesWindow', value);
            ipcRenderer.send('imagesWindow', 'show');
        }
        // win.loadURL(modalPath)

    });
});


//==>Analyse窗口交互

btnAnalyse.onclick = function () {
    // console.log('analyseWindows')
    ipcRenderer.send("analyseWindows", $("#versions option:selected").text());

    // ipcRenderer.send('versionSelect', $("#versions option:selected").text());
}

//重置表格
effaceDom.onclick=function () {
    remote.dialog.showMessageBox({
        type:'info',
        title:'bug',
        message:'Effacer tous ?',
        buttons:['ok','no']
    },function (index) {
        if (index==0) {
            dataTableDom.innerHTML = '';            
        }
        console.log(index);
    });
}


