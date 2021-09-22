var btn=document.querySelector('#btn');

var BrowserWindow=require('electron').remote.BrowserWindow;
var win =null;
btn.onclick=function () { 
    // alert('点击');
    //调用browserwindow
    newWin=new BrowserWindow({
        width:800,
        height:600,
        // frame:false
    })
    win.loadFile('new.html');
    win.on('closed',()=>{
        win=null;
    })
}