var { ipcMain } = require('electron');
var { BrowserWindow } = require('electron');
var fs = require('fs');
var sqlite3 = require('sqlite3').verbose();
const path = require('path');
// const jquery=require('jquery') 
const dialog = require('electron').dialog

var ele = require('electron');
//app 控制应用生命周期
const app = ele.app;


//==>==>==>==>==>==>==>==>==>窗口相关<==<==<==<==<==<==<==<==
let renderWindows = null;
let imagesWindows = null;
let analyseWindows = null;
let dataPrintWindows = null;
let evolutionWindows = null;
// let analysePrintWindows = null;

//==>renderWindows    ID=
renderWindows = new BrowserWindow({ width: 1600, height: 900 });
renderWindows.loadFile('index.html');

//==>imagesWindows ID=
// imagesWindows = new BrowserWindow({ show: false, alwaysOnTop: true, frame: false, width: 700, height: 500 })
imagesWindows = new BrowserWindow({ show: false, alwaysOnTop: true , frame:false, width: 1370, height: 900})
imagesWindows.loadFile('images.html');  
imagesWindows.on('blur', function () { imagesWindows.hide(); })
// imagesWindows.on('close', function () { imagesWindows = null });
// imagesWindows.on('blur', function () { imagesWindows = null; imagesWindows.hide(); })
//==>analyseWindows  ID=
analyseWindows = new BrowserWindow({ show: false, frame: false, width: 1200, height: 900 });
// analyseWindows = new BrowserWindow({ show: false, alwaysOnTop: true, frame: false, width: 1200, height: 900 });
analyseWindows.loadFile('analyse.html');
// analyseWindows.on('blur', function () { analyseWindows.hide(); })

//==>evolutionWindows  ID=
// evolutionWindows = new BrowserWindow({ show: false, alwaysOnTop: true, frame: false, width: 1500, height: 900 });
evolutionWindows = new BrowserWindow({frame: false, width: 1500, height: 900 });
// evolutionWindows = new BrowserWindow({ alwaysOnTop: true, frame: false, width: 1500, height: 900 });
evolutionWindows.loadFile('evolution.html');
// evolutionWindows.on('blur', function () { evolutionWindows.hide(); })


//==>dataPrintWindows   ID=
dataPrintWindows = new BrowserWindow({ title: 'dataPrintWindows', show: false, width: 1600, height: 900 });
dataPrintWindows.loadFile('printData.html');

// //==>analysePrintWindows   ID=
// analysePrintWindows = new BrowserWindow({ title: 'analysePrintWindows', width: 1200, height: 900 });
// // analysePrintWindows = new BrowserWindow({ title: 'analysePrintWindows', show: false, width: 1200, height: 900 });
// analysePrintWindows.loadFile('analysePrint.html');

//==>退出程序
renderWindows.on('close', function () {
renderWindows = null;
dataPrintWindows = null;
analyseWindows = null;
imagesWindows = null;
evolutionWindows = null;
// analysePrintWindows = null;
  app.quit() //重要!    
})



//==>==>==>==>==>==>==>==>==>开发者模式<==<==<==<==<==<==<==<==
imagesWindows.webContents.openDevTools();
analyseWindows.webContents.openDevTools();
renderWindows.webContents.openDevTools();
dataPrintWindows.webContents.openDevTools();
evolutionWindows.webContents.openDevTools();




//==>==>==>==>==>==>==>==>==>数据库操作<==<==<==<==<==<==<==<==
//=>connect database

// const path_rootdir = "./resources/app";
const path_rootdir = ".";

const path_database = path_rootdir + "/Database/DataAdas.db";
const dbPath = path.resolve(path_database);
var db = new sqlite3.Database(dbPath, "OPEN_READONLY");
var dataReturn = [];
var dataAllReturn = [];
var dataAnalyse = [];
var versionAll = [];

//==>SQL命令
var sqlCommand_getAll = "select ID,type,scenario_type,id_senario,duration,author,date,version,n_iteration,time,bug_number,description,path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time from DataAdas";

var sqlCommand_getAnalyse = "select version,indice,type,scenario_type,number_bugs,success_rate,number_scenerios_bugs,number_scenerios_all,total_duration_scenarios,total_distances,bug0,bug1,bug2,bug3,bug4,bug5,bug6,bug7,bug8,bug9,bug10,bug11,bug12,bug13,bug14,bug15,bug16,bug17,bug18,bug19,bug20,bug21,bug22,bug23,bug24,bug25,bug26,bug27,bug28,bug29,bug30,bug31,bug32,bug33,bug34,bug35,bug36,bug37,bug38,bug39,bug40,bug41,bug42 from Analyse";

function sqlAll_selectVersion(v) {
  var commande = "select ID,type,scenario_type,id_senario,duration,author,date,version,n_iteration,time,bug_number,description,path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time from DataAdas where version = \'" + v + "\'";
  return commande;
}

//path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,

function sqlAll_selectVersionModule(v,m) {
  var commande = "select ID,type,scenario_type,id_senario,duration,author,date,version,n_iteration,time,bug_number,description,"+m+",global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time from DataAdas where version = \'" + v + "\'";
  return commande;
}

function sqlAnalyse_selectVersion(v) {
  var commande = "select version,indice,type,scenario_type,number_bugs,success_rate,number_scenerios_bugs,number_scenerios_all,total_duration_scenarios,total_distances,bug0,bug1,bug2,bug3,bug4,bug5,bug6,bug7,bug8,bug9,bug10,bug11,bug12,bug13,bug14,bug15,bug16,bug17,bug18,bug19,bug20,bug21,bug22,bug23,bug24,bug25,bug26,bug27,bug28,bug29,bug30,bug31,bug32,bug33,bug34,bug35,bug36,bug37,bug38,bug39,bug40,bug41,bug42 from Analyse where version = \'"+ v+"\'";
  return commande;
}

// var sqlCommand_getAnalyse = "select ID,version,indice,type,scenario_type,number_bugs,success_rate,number_scenerios_bugs,number_scenerios_all,total_duration_scenarios,total_distances,bug0,bug1,bug2,bug3,bug4,bug5,bug6,bug7,bug8,bug9,bug10,bug11,bug12,bug13,bug14,bug15,bug16,bug17,bug18,bug19,bug20,bug21,bug22,bug23,bug24,bug25,bug26,bug27,bug28,bug29,bug30,bug31,bug32,bug33,bug34,bug35,bug36,bug37,bug38,bug39,bug40,bug41,bug42 from Analyse";

// var sqlCommand_getSimobj = "select ID,scenario_type,id_senario,duration,author,date,version,n_iteration ,time,bug_number,description,path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time from DataAdas where type='Simobj'";


//===>函数定义

function getLength(json) {
  var jsonLength = 0;
  for (var i in json) {
    jsonLength++;
  }
  return jsonLength;
}


function deleteEmptyProperty(object) {
  for (var i in object) {
    var value = object[i];
    if (typeof value === 'object') {
      if (Array.isArray(value)) {
        if (value.length == 0) {
          delete object[i];
          continue;
        }
      }
      deleteEmptyProperty(value);
      if (isEmpty(value)) {
        delete object[i];
      }
    } else {
      if (value === '' || value === null || value === undefined) {
        delete object[i];
      } else {
      }
    }
  }
}


function isEmpty(object) {
  for (var name in object) {
    return false;
  }
  return true;
}

function delRep_back(obj) {
  var newJson = {};
  for (var key in obj) {
    if (newJson[obj[key]]) {
      delete obj[key];
    } else {
      newJson[obj[key]] = true;
    }
  }
  // console.log(obj)
  return obj
}

function delRep(obj) {
  var newJson = [];
  newJson.push(obj[0]);
  versionPush = obj[0]['version'];
  for (let i = 0; i < obj.length; i++) {
    if (obj[i]['version'] != versionPush) {
      newJson.push(obj[i]);
      versionPush = obj[i]['version'];
    }
  }
  return newJson
}

function databaseAll(db, sqlCo) {
  db.serialize(function () {
    db.all(sqlCo, function (err, row) {
      if (err) {
        console.log(err);
        return "error";
      }
      else {
          // console.log(row);
        dataReturn = row;
        return row;
      }
    });
  })

}


function databaseAnalyse(db, sqlCo) {
  db.serialize(function () {
    db.all(sqlCo, function (err, row) {
      if (err) {
        console.log(err);
        return "error";
      }
      else {
        // console.log(row);
        dataAnalyse = row;
        return row;
      }
    });
  })
}


function getAllVersion() {
  var versions = [];
  versionJson = {};
  // var commande = 'select version from Analyse';
  var commande = 'select version from DataAdas';
  db.serialize(function () {
    db.all(commande, function (err, row) {
      if (err) {
        console.log(err);
        return "error";
      }
      else {
        // console.log(row);
        var newRow = delRep(row)
        // deleteEmptyProperty(newRow)
        // console.log(row);
        // console.log(getLength(newRow));
        for (let index = 0; index < getLength(newRow); index++) {
          versionJson.index = {};
          versionJson.index.id = index + 1;
          versionJson.index.title = newRow[index].version;
          versions.push(versionJson.index);
          // console.log(versions)
        }
        // console.log(versions)

        // dataReturn = row;
        versionAll = versions;
        // console.log(versionAll);
        // return versionAll;
      }
    });
  })
}

function getAllVersionParVersion() {
  var versions = [];
  versionJson = {};
  var commande = 'select version from Analyse';
  db.serialize(function () {
    db.all(commande, function (err, row) {
      if (err) {
        console.log(err);
        return "error";
      }
      else {
        var newRow = delRep(row)
        // deleteEmptyProperty(newRow)
        // console.log(newRow);
        // console.log(getLength(newRow));
        for (let index = 0; index < getLength(newRow); index++) {
          commande = sqlAll_selectVersion(newRow[index].version);
          // console.log(commande);
          databaseAll(db, commande);
          dataAllReturn.push(dataReturn);
        }
        // console.log(dataAllReturn)
        
      }
    });
  })
}



function copyDir(src, dist, callback) {
  fs.access(dist, function (err) {
    if (err) {
      // 目录不存在时创建目录
      fs.mkdirSync(dist);
    }
    _copy(null, src, dist);
  });

  function _copy(err, src, dist) {
    if (err) {
      callback(err);
    } else {
      fs.readdir(src, function (err, paths) {
        if (err) {
          callback(err)
        } else {
          paths.forEach(function (path) {
            var _src = src + '/' + path;
            var _dist = dist + '/' + path;
            fs.stat(_src, function (err, stat) {
              if (err) {
                callback(err);
              } else {
                // 判断是文件还是目录
                if (stat.isFile()) {
                  fs.writeFileSync(_dist, fs.readFileSync(_src));
                } else if (stat.isDirectory()) {
                  // 当是目录是，递归复制
                  copyDir(_src, _dist, callback)
                }
              }
            })
          })
        }
      })
    }
  }
}



//==>==>==>==>==>==>==>==>==>主程序初始化<==<==<==<==<==<==<==<==

//==>数据库执行
// getAllVersionParVersion();
getAllVersion();
databaseAnalyse(db, sqlCommand_getAnalyse);
databaseAll(db, sqlCommand_getAll);

//==>Wins加载完成后发送全部数据
renderWindows.webContents.on('did-finish-load', (event) => {
  renderWindows.webContents.send('render_receiver_all', dataReturn);
  // console.log(dataReturn);
})

analyseWindows.webContents.on('did-finish-load', (event) => {
  analyseWindows.webContents.send('dataAnalyse_all', dataAnalyse);
  // console.log(dataAnalyse);
})

evolutionWindows.webContents.on('did-finish-load', (event) => {
  evolutionWindows.webContents.send('dataEvolution', dataAnalyse);
  evolutionWindows.webContents.send("versionAll", versionAll);
})

// analysePrintWindows.webContents.on('did-finish-load', (event) => {
//   analysePrintWindows.webContents.send('dataAnalyse_all', dataAnalyse);
// })

// renderWindows.webContents.send("render_receiver_all", dataReturn);

//==>Communication-IPC-version 有延迟的问题 等待解决！

// ipcMain.on('versionSelect', function (event, data) {
//   com_VS=sqlAnalyse_selectVersion(data);
//   // console.log(com_VS);
//   databaseAnalyse(db, com_VS);
//   // console.log(data);
//   analyseWindows.webContents.send('dataAnalyse_all', dataAnalyse);

// })



//==>==>==>==>==>==>==>==>==>选择init-Version版本<==<==<==<==<==<==<==<==

ipcMain.on('versionGet', function (event, data) {
    // console.log(data);
    renderWindows.webContents.send('getVersion', versionAll);
})

//==>==>==>==>==>==>==>==>==>Bug图像详情窗口交互<==<==<==<==<==<==<==<==
//===>Communication-IPC-image
ipcMain.on('imagesWindow', function (event, data) {
    imagesWindows.show();

    if (data!='show') {
      // imagesWindows.webContents.send("imageID", data);
      imagesWindows.webContents.send("imageDetails", dataReturn[data - 1], data);
    }
  })

//==>==>==>==>==>==>==>==>==>analyse窗口显示交互<==<==<==<==<==<==<==<==
//===>Communication-IPC-analyse
ipcMain.on('analyseWindows', function (event, data) {
  //==>analyseWindows
  // event.sender.send("dataAnalyse_all", dataAnalyse);
  analyseWindows.webContents.send("dataAnalyse_select", data); 
  // analysePrintWindows.webContents.send("dataAnalyse_select", data); 
  // console.log(data);
  analyseWindows.show();
  analyseWindows.focus();
  // console.log(dataAnalyse);
  // console.log(data);

})


//==>==>==>==>==>==>==>==>==>evolution窗口显示交互<==<==<==<==<==<==<==<==
//===>Communication-IPC-analyse
ipcMain.on('evolutionWindows', function (event, data) {
  //==>evolutionWindows
  // evolutionWindows.webContents.send("versionAll", versionAll);
  // console.log(data);
  evolutionWindows.show();
  evolutionWindows.focus();
  // console.log(dataAnalyse);
  // console.log(data);

})




//==>==>==>==>==>==>==>==>==>HTML保存生成<==<==<==<==<==<==<==<==


function getSave(pathO,pathD,dataToAdd) {
  fs.readFile(pathO, { flag: 'r+', encoding: 'utf8' }, function (err, data) {
    if (err) {
      console.error(err);
      return;
    }
    data = data + dataToAdd;

    // console.log(dataReturn.toString('utf-8'));
    // console.log(dataReturn);

    // fs.writeFile(pathD, data, { flag: 'a' }, function (err) {
    fs.writeFile(pathD, data, 'utf-8', function (err) {
      if (err) {
        console.error(err);
      } else {
        renderWindows.webContents.send('sucReceive', 'HTMLs successfully saved to: \n' + pathD);
      }
    });

  });
}



//==>==>==>==>==>==>==>==>==>Save all as HTMLs<==<==<==<==<==<==<==<==
ipcMain.on('saveHtml', function (event, data) {
  //==>save
  // console.log(data[0]);
  dialog.showOpenDialog({
    properties: ['openFile', 'openDirectory']
  }, function (files) {
    if (files){

//==>Detail Page 生成<==
      var pathO_Detail = path_rootdir + '/templates/printData.html';
      var pathD_Detail = files + "\\details.html";
      var dataToAdd_Detail = "<script> \n dataAll =" + JSON.stringify(dataReturn) + "; \n versionData =" + JSON.stringify(versionAll) + ";\n </script>";
      // filesAnalyse = files + "\\analyseH.html";
      getSave(pathO_Detail, pathD_Detail,dataToAdd_Detail);

//==>Analyse Page 生成<==
      var pathO_Analyse = path_rootdir + '/templates/printAnalyse.html';
      var pathD_Analyse = files + "\\analyses.html";
      var dataToAdd_Analyse = "<script> \n dataAnalyse_all =" + JSON.stringify(dataAnalyse) + "; \n versionData =" + JSON.stringify(versionAll) + ";\n </script>";
      // filesAnalyse = files + "\\analyseH.html";
      getSave(pathO_Analyse, pathD_Analyse, dataToAdd_Analyse);


//==>Evolution Page 生成<==
      var pathO_Evolution = path_rootdir + '/templates/printEvolution.html';
      var pathD_Evolution = files + "\\index.html";
      var dataToAdd_Evolution = "<script> \n dataAnalyse_all =" + JSON.stringify(dataAnalyse) + "; \n version_all =" + JSON.stringify(versionAll) + ";\n </script>";
      getSave(pathO_Evolution, pathD_Evolution, dataToAdd_Evolution);

//==>imagesWindows Page 生成<==
      var pathO_Image = path_rootdir + '/templates/images.html';
      var pathD_Image = files + "\\images.html";
      var dataToAdd_Image = "<script> \n </script>";
      getSave(pathO_Image, pathD_Image, dataToAdd_Image); 
//         imagesWindows.webContents.savePage(files+"\\images.html", 'HTMLComplete', function (error) {
//         if (!error)
//           renderWindows.webContents.send('sucReceive', 'HTMLs successfully saved to: \n' + files + "\\images.html");
//         });

//==>libHtmls 复制<==

      copyDir(path_rootdir + '/templates/libHtmls', files +"\\libHtmls\\", function (err) {
        if (err) {
          // console.log(err);
          renderWindows.webContents.send('errorsReceive', err);
        }
      })

      }})

      // analysePrintWindows.webContents.send("dataAnalyse_select", data[0]);
      // // analysePrintWindows.webContents.on('did-finish-load', (event) => {
      //   analysePrintWindows.webContents.savePage(filesAnalyse, 'HTMLComplete', function (error) {
      //     if (!error)
      //       console.log(filesAnalyse);
      //   });
      // });
      
    })


//==>==>==>==>==>==>==>==>==>Save evolution as HTMLs<==<==<==<==<==<==<==<==
ipcMain.on('saveEvolution', function (event, data) {
  //==>save
  // console.log(data[0]);
  dialog.showOpenDialog({
    properties: ['openFile', 'openDirectory']
  }, function (files) {
    if (files) {

      //==>Analyse Page 生成<==
      var pathO_Analyse = path_rootdir + '/templates/printAnalyseSingle.html';
      var pathD_Analyse = files + "\\analyses.html";
      var dataToAdd_Analyse = "<script> \n dataAnalyse_all =" + JSON.stringify(dataAnalyse) + "; \n versionData =" + JSON.stringify(versionAll) + ";\n </script>";
      // filesAnalyse = files + "\\analyseH.html";
      getSave(pathO_Analyse, pathD_Analyse, dataToAdd_Analyse);


      //==>Evolution Page 生成<==
      var pathO_Evolution = path_rootdir + '/templates/printEvolutionSingle.html';
      var pathD_Evolution = files + "\\index.html";
      var dataToAdd_Evolution = "<script> \n dataAnalyse_all =" + JSON.stringify(dataAnalyse) + "; \n version_all =" + JSON.stringify(versionAll) + ";\n </script>";
      getSave(pathO_Evolution, pathD_Evolution, dataToAdd_Evolution);


      //==>libHtmls 复制<==

      copyDir(path_rootdir + '/templates/libHtmls', files + "\\libHtmls\\", function (err) {
        if (err) {
          // console.log(err);
          renderWindows.webContents.send('errorsReceive', err);
        }
      })

    }
  })

})


//==>==>==>==>==>==>==>==>==>Save Weekly as HTMLs<==<==<==<==<==<==<==<==
ipcMain.on('saveWeekly', function (event, data) {
  //==>save
  // console.log(data[0]);
  dialog.showOpenDialog({
    properties: ['openFile', 'openDirectory']
  }, function (files) {
    if (files) {

      //==>Detail Page 生成<==
      var pathO_Detail = path_rootdir + '/templates/printDataWeekly.html';
      var pathD_Detail = files + "\\index_Weekly.html";
      var dataToAdd_Detail = "<script> \n dataAll =" + JSON.stringify(dataReturn) + "; \n versionData =" + JSON.stringify(versionAll) + ";\n </script>";
      // filesAnalyse = files + "\\analyseH.html";
      getSave(pathO_Detail, pathD_Detail, dataToAdd_Detail);

      //==>imagesWindows Page 生成<==
      var pathO_Image = path_rootdir + '/templates/images.html';
      var pathD_Image = files + "\\images.html";
      var dataToAdd_Image = "<script> \n </script>";
      getSave(pathO_Image, pathD_Image, dataToAdd_Image);
      //         imagesWindows.webContents.savePage(files+"\\images.html", 'HTMLComplete', function (error) {
      //         if (!error)
      //           renderWindows.webContents.send('sucReceive', 'HTMLs successfully saved to: \n' + files + "\\images.html");
      //         });

      //==>libHtmls 复制<==

      copyDir(path_rootdir + '/templates/libHtmls', files + "\\libHtmls\\", function (err) {
        if (err) {
          // console.log(err);
          renderWindows.webContents.send('errorsReceive', err);
        }
      })

    }
  })

})












//==>备份
    // event.sender.send("render_receiver_all", dataReturn);
    // var dataReturn=[]; 
    // var selector = data.split(",")
    // var dataReturn = databaseAll(db, sqlCommand_getAll);
    // databaseAll(db, sqlCommand_getAll);
    //===延迟加载
    // setTimeout(function () {
    //   // console.log('datareturn:',dataReturn);
    //   event.sender.send("render_receiver", dataReturn);
    // }, 500);
    // console.log(dataReturn);


    // wins=BrowserWindow.getAllWindows();
    // console.log(wins);

  // bugInfos = dataReturn['ID: 31'];
    // console.log(bugInfos);
    // console.log(dataReturn[data-1]);
    // console.log(data);
    // event.sender.send("imageID", data);











// ipcMain.on("sendsync", function(event, data) {
//   console.log(data);
//   // console.log(event);
//   //给客户端返回数据
//   databaseAll(db, sqlCommand_getAll);
//     // event.returnValue = databaseAll(db, sqlCommand_getAll);
//   event.returnValue = dataReturn;
// });



// //接受
// ipcMain.on('sendM',function (event,data) {
//     console.log(data);
//     console.log(event);
// })

// //接收同步广播


//==>同步等待



// function getInfos(sqlCo) {
//   return new Promise((resolve, reject) => {
//     databaseAll(db, sqlCo);
//   });
// }

// function sendInfos(event) {
//   return new Promise((event, reject) => {
//     console.log(dataReturn);
//     event.sender.send("render_receiver", dataReturn);
//   });
// }


// async function databaseDone(event) {
//   await getInfos(db, sqlCommand_getAll);
//   await sendInfos(event, dataReturn);
// }
// ipcMain.on("main_receiver", function(event, data) {
//   databaseDone(event);
// });