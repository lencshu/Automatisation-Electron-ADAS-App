var content=document.querySelector('#content')

var fs=require('fs');

content.ondragenter=content.ondragover=content.ondragleave=function(){
    return false;
    //组织默认行为
}

content.ondrop=function(e){
    e.preventDefault();
    console.log(e.dataTransfer.files[0]);
    var path=e.dataTransfer.files[0].path;
    fs.readFile(path,'utf-8',(err,data)=> {
        if(err){
            console.log(err)
            return false;
        }
    content.innerHTML=data;
    })
}
