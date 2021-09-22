var ele=require('electron');
//app 控制应用生命周期
const app=ele.app;
//窗口相关
// const bro=ele.BrowserWindow;
// let renderWindows=null;
// let dataProcessingWindows = null;

function creatWins() {
    //==>依赖
    // require('./main/menu.js');
    require("./main/ipc_main");

}

app.on('ready', creatWins);

// 当所有的窗口被关闭后退出应用
app.on('window-all-closed', function () {
    // 对于OS X系统，应用和相应的菜单栏会一直激活直到用户通过Cmd + Q显式退出
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
 






// //主进程
// var electron =require('electron');
// //electron 对象的引用
// const app=electron.app;
// //BrowserWindow 类的引用
// const BrowserWindow=electron.BrowserWindow;
// //变量 保存对应用窗口的引用
// let mainWindow=null;
// //监听应用准备完成的事件 打开html
// app.on('ready',function(){
// //创建browserwindow的实例 赋值给mainWindow打开窗口 传入窗口的宽度高度
// mainWindow=new BrowserWindow({width: 800, height: 600});
// //加载html
// mainWindow.loadFile('index.html');
// mainWindow.on('closed', function () {
// mainWindow = null;
// })
// })
