var electron=require('electron').remote;
var menu=electron.Menu;



var template=[
    {
        label:"trier par module",
        submenu:[
            {
                label:'新建文件',
                click:function(){
                    console.log('新建');
                },
                accelerator: 'ctrl+n',
            },

            {
                label:'新建窗口',
                accelerator:'ctrl+n',
            },
        ]
    },
    {
        label:"trier par senario",
    },
]

var m=menu.buildFromTemplate(template);

// menu.setApplicationMenu(m);

//右键

window.addEventListener('contextmenu',function(e){
    // alert('1212')
    //阻止默认事件
    e.preventDefault();
    //当前窗口弹出模板
    m.popup({window:electron.getCurrentWindow()});

},false)