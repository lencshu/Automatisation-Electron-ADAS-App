

var fs=require('fs');
window.onload=function(){
    var btn=this.document.querySelector('#btn');
    var textarea=this.document.querySelector('#textarea');
    btn.onclick=function(){
        // 获取本地文件
        fs.readFile('package.json',(err,data)=>{
            // console.log(data)
            textarea.innerHTML=data;
        })

    }
}