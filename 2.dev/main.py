#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$


# from adas.database import database
from adas import database
from adas import image
from adas import globalVariable as go
from adas import classifyFiles
from adas import readLog
from adas import analyse
from adas import iniSet
import os 
import re

go._init()  # 先必须在主模块初始化（只在Main模块需要一次即可）
co = iniSet.iniConfig()
da = database.dataAdas()
cl=classifyFiles.files()
re=readLog.readLog()
an=analyse.analyse()

 
#==>==>==>==>==>Version

print '==>==>==> Manipulation de la base de donee V3.0 <==<==<=='

#==>==>==>==>==>les initiations du config de chaque User

indiceCompress = raw_input("Want to compress the image?(Yes:1,[No]:0): ") or 0

userName = raw_input("Enter your Name: ") or 'GL'
conf=co.getAll(userName)

version = raw_input("Enter The Version of Validation : ")


path_log_emballer = conf[0]
path_logs = conf[1]
path_errorFile = conf[3]+'\\errorFile.txt'
path_images = conf[2]
datapath=conf[3]
go.set_value('USERNAME', userName)
go.set_value('datapath', datapath)

# print conf


#==>==>==>==>==>les initiations des tables du database

try:
    da.addTable_validation()
except:
    print 'Attention(Normal):Validation Table already exist'
else:
    pass

try:
    da.addTable_analyse()
except:
    print 'Attention(Normal): Analyse Table already exist'
else:
    pass

try:
    da.addTable_Bug()
    da.addBugAll()
    print "Bugs created successfully"
except:
    print 'Attention(Normal): Bugs Table already exist'
else:
    pass

 

#==>==>==>==>==>readLog


for root, dirs, files in os.walk(path_log_emballer):
    for file in files:
        filetype=os.path.splitext(file)[1] 
        if filetype == '.txt':
            path_log = root+'\\'+file
            re.pushtoData(path_errorFile,path_log, path_images, version)

#==>==>==>==>==>Bug 0 update

da.ignoreNullBug() 

#==>==>==>==>==>timeShift

# da.timeShift()

#==>==>==>==>==>Analyse

an.analyse()




#==>==>==>==>==>classify

cl.classify(path_log_emballer,path_logs,path_images,indiceCompress)


#==>==>==>==>==>versionChange
# da.versionChange(version)




























#==>大数据库测试

# da.addAnalyse('version','indice','type','scenario_type','number_bugs','number_scenerios_bugs','number_scenerios_all','total_duration_scenarios','total_distances','bug0','bug1','bug2','bug3','bug4','bug5','bug6','bug7','bug8','bug9','bug10','bug11','bug12','bug13','bug14','bug15','bug16','bug17','bug18','bug19','bug20','bug21','bug22','bug23','bug24','bug25','bug26','bug27','bug28','bug29','bug30','bug31','bug32','bug33','bug34','bug35','bug36','bug37','bug38','bug39','bug40','bug41','bug42')



# for i in range(1,10000):
#     print i
#     da.addValidation('Roulage', 'FusionAssessment', 'S1', '15s: 780ms', 'GL', '25/7/2018', 'SUV_ADAS_V2.0_1829', '51', '1519280:578', '22', 'Bug 22: Inappropriate Lines modeling - Other issue', 'v_ert', 'v_ert', 'v_ert','v_ert', 'v_ert', 'v_ert', 'v_ert', 'v_ert', 'r_ouge', 'v_ert', '134,468765','./Database/imgs_log/1_ID_1_Step_51.png', './Database/imgs_log/1_ID_1_Step_51_context.png', '13h17min50sec,25,7', 'AdditionalTests->AdditionalTests_Day3->DoubleTargets_Cars_Oncoming', '0')

#     da.addValidation('Simobj', 'ACC', 'S1', '15s: 780ms', 'GL', '25/7/2018', 'SUV_ADAS_V2.0_1829', '51', '1519280:578', '22', 'Bug 22: Inappropriate Lines modeling - Other issue', 'v_ert', 'v_ert', 'v_ert','v_ert', 'v_ert', 'r_ouge', 'v_ert', 'v_ert', 'r_ouge', 'r_ouge', '134,468765','./Database/imgs_log/1_ID_1_Step_51.png', './Database/imgs_log/1_ID_1_Step_51_context.png', '13h17min50sec,25,7', '0', '0')

    # da.addValidation(type,scenario_type,id_senario,duration,author,date,version,n_iteration ,time,bug_number,description,path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time)







# path = r'Scenario: C:\Users\gli\Desktop\Validation\SUV_ADAS_V2.0_1829\ProtoAEB\FusionAssessment\Deliveries\AdditionalTests\AdditionalTests_Day3\DoubleTargets_Cars_Oncoming\20171018_160052_RecFile_2'
# path = r'Scenario: C:\Users\gli\Desktop\Validation\SUV_ADAS_V2.0_1829\ProtoAEB\FusionAssessment\Deliveries\AdditionalTests\AdditionalTests_Day3\DoubleTargets_Cars_Oncoming\20171018_160052_RecFile_2'

# line = re.split(r'[:\t\n\r\f\v]', path)
# line = [item for item in filter(lambda x:x != '', line)]
# lesinfos = line[2].split('\\')
# if 'ProtoAEB' in line[2]:
#     print 'OK'
# startEle=lesinfos.index('Deliveries')+1
# endEle=len(lesinfos)-1
# sub_scenario_type = '->'.join(lesinfos[startEle:endEle])
# st = lesinfos[startEle-4].strip()
# print st













