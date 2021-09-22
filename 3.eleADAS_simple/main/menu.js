var electron=require('electron');
var menu=electron.Menu;

// var {Menu}=require('electron')

var {shell}=require('electron');

function openweb(url){
    shell.openExternal(url);
}

var template=[
    {
        label:"文件",
        submenu:[
            {
                label:'新建文件',
                click:function(){
                    console.log('新建');
                }
            },
            {
                type:'separator'
            },

            {
                label:'新建窗口',
                accelerator:'ctrl+n',
            },
        ]
    },
    {
        label:"关于我",
        click:function () {
            openweb('https://gliang.eu');
        }
    },
]

var m=menu.buildFromTemplate(template);

menu.setApplicationMenu(m);

