#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$
# 

"""
methodes:
readLog.pushtoData(path_log,desti_img_path)
""" 

# from database import database
import database
import re
import os
import image
import time



dictoPush = {}.fromkeys(['type', 'scenario_type', 'sub_scenario_type', 'id_senario', 'duration', 'author', 'date', 'version', 'n_iteration', 'time', 'bug_number', 'description', 'path_prediction_ego', 'ego_tracking', 'lane_assignement', 'lane_fusion', 'path_prediction_object', 'object_tracking', 'tsad', 'tslss', 'tsaeb', 'global_statuts', 'ego_distance', 'img_path', 'img_context_path', 'creat_time', 'count_in','modifier_time'], 0)
img=image.image()

# da = database.dataAdas(path_database)

da=database.dataAdas()



class readLog(object):
    """docstring for log"""
    def __init__(self):
        pass
        # super(log, self).__init__()

    def dir_rename(self,a):
        b=os.path.dirname(a)
        b=a.replace(b,'')
        b='.\\Database\\imgs_log'+b
        b=b.replace('\\',"/")
        return b

    def time_dir(self,path_log):
        ct=path_log.split('\\')[-2].split('_')
        creat_time=ct[-1]+','+ct[-2]+','+ct[-3]
        creat_data=ct[-2]+'/'+ct[-3]+'/2018'
        # print creat_time
        dictoPush['date']=creat_data
        dictoPush['creat_time']=creat_time

    def get_ego_distance(self,path_log):
        file_object = open(path_log,'r')
        try: 
            for line in file_object:
                 if 'Ego distance' in line:
                    line=line.split()
                    dictoPush['ego_distance']=line[2]
                    # print dictoPush['ego_distance']
        finally:
             file_object.close()

    def addValidationBug(self):
        try:
            da.addValidation(dictoPush['type'],dictoPush['scenario_type'], dictoPush['id_senario'], dictoPush['duration'], dictoPush['author'], dictoPush['date'], dictoPush['version'], dictoPush['n_iteration'], dictoPush['time'], dictoPush['bug_number'], dictoPush['description'], dictoPush['path_prediction_ego'], dictoPush['ego_tracking'], dictoPush['lane_assignement'], dictoPush['lane_fusion'], dictoPush['path_prediction_object'], dictoPush['object_tracking'], dictoPush['tsad'], dictoPush['tslss'], dictoPush['tsaeb'], dictoPush['global_statuts'], dictoPush['ego_distance'], dictoPush['img_path'], dictoPush['img_context_path'], dictoPush['creat_time'], dictoPush['sub_scenario_type'],dictoPush['count_in'])
        except:
            time.sleep(5)
            try:
                da.addValidation(dictoPush['type'],dictoPush['scenario_type'], dictoPush['id_senario'], dictoPush['duration'], dictoPush['author'], dictoPush['date'], dictoPush['version'], dictoPush['n_iteration'], dictoPush['time'], dictoPush['bug_number'], dictoPush['description'], dictoPush['path_prediction_ego'], dictoPush['ego_tracking'], dictoPush['lane_assignement'], dictoPush['lane_fusion'], dictoPush['path_prediction_object'], dictoPush['object_tracking'], dictoPush['tsad'], dictoPush['tslss'], dictoPush['tsaeb'], dictoPush['global_statuts'], dictoPush['ego_distance'], dictoPush['img_path'], dictoPush['img_context_path'], dictoPush['creat_time'], dictoPush['sub_scenario_type'],dictoPush['count_in'])
            except:
                print "Data save failed"


    def img_rename(self,path_log,desti_img_path,thisValidationNumber,line,indiceType,path_errorFile):
        path_root=os.path.dirname(path_log)
        path_img=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+".png"
        #SimObj
        if indiceType==1:
            path_img_context_1=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+"_context_1.png"
            path_img_context_0=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+"_context_0.png"
            path_img_context = path_img_context_0
            try:
                path_img_context = img.rename(thisValidationNumber, path_img_context_1, path_errorFile)
                print "Image renamed", path_img_context
                path_img_context = img.rename(thisValidationNumber, path_img_context_0, path_errorFile)
                print "Image renamed", path_img_context
            except :
                path_img_context=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+"_context.png"
                try:
                    path_img_context = img.rename(thisValidationNumber, path_img_context, path_errorFile)
                    print "Image renamed", path_img_context
                except:
                    print "Image file not exist: ", path_img_context
                    errorsData = "\nImage file not exist: "+ path_img_context
                    self.errorWrite(path_errorFile, errorsData)
        else:
            path_img_context=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+"_context_0.png"
            try:
                path_img_context = img.rename(thisValidationNumber, path_img_context, path_errorFile)
                print "Image renamed", path_img_context
            except:
                path_img_context=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+"_context.png"
                try:
                    path_img_context = img.rename(thisValidationNumber, path_img_context, path_errorFile)
                    print "Image renamed", path_img_context
                except:
                    print "Image file not exist: ", path_img_context
                    errorsData = "\nImage file not exist: " + path_img_context
                    self.errorWrite(path_errorFile, errorsData)
        # print path_img
        # print line,line[3]
        # print r'C:\Users\lencs\Desktop\Altran\_dev\2.dev\adas\log_7_16_13h54min22sec\ID_1_Step_0.png')
        try:
            path_img=img.rename(thisValidationNumber,path_img, path_errorFile) 
            print "Image renamed", path_img
        except:
            print "Image file not exist: ", path_img
            errorsData = "\nImage file not exist: " + path_img
            self.errorWrite(path_errorFile, errorsData)
        # thisValidationNumber += 1
        # thisValidationNumber += 1
        # print path_img,path_img_context
        dictoPush['img_path']=self.dir_rename(path_img)
        dictoPush['img_context_path']=self.dir_rename(path_img_context)
        # print dictoPush['img_path']

    def img_rename_old(self,path_log,desti_img_path,thisValidationNumber,line):
        path_root=os.path.dirname(path_log)
        path_img=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+".png"
        path_img_context=path_root+"\\ID_"+line[1].strip()+"_Step_"+line[3].strip()+"_context.png"
        # print path_img
        # print line,line[3]
        # print r'C:\Users\lencs\Desktop\Altran\_dev\2.dev\adas\log_7_16_13h54min22sec\ID_1_Step_0.png')
        path_img=img.rename(thisValidationNumber,path_img)
        # thisValidationNumber += 1
        path_img_context=img.rename(thisValidationNumber,path_img_context)
        # thisValidationNumber += 1
        # print path_img,path_img_context
        dictoPush['img_path']=self.dir_rename(path_img)
        dictoPush['img_context_path']=self.dir_rename(path_img_context)
        # print dictoPush['img_path']


    def moduleInit(self):
        dictoPush['path_prediction_ego'] = 'v_ert'
        dictoPush['ego_tracking'] = 'v_ert'
        dictoPush['lane_assignement'] = 'v_ert'
        dictoPush['lane_fusion'] = 'v_ert'
        dictoPush['path_prediction_object'] = 'v_ert'
        dictoPush['object_tracking'] = 'v_ert'
        dictoPush['tsad'] = 'v_ert'
        dictoPush['tslss'] = 'v_ert'
        dictoPush['tsaeb'] = 'v_ert'
        dictoPush['global_statuts'] = 'v_ert'

    def ifNoBugs(self):
        if dictoPush['description']==0:
            return True
        return False

    def findIfNoBugs(self, path_log):
        file_object = open(path_log,'r')
        num_bugs=0
        try: 
            for line in file_object:
                 if 'IssueID' in line:
                     num_bugs = num_bugs+1
                    # print dictoPush['ego_distance']
        finally:
            file_object.close()
            if num_bugs==0:
                return True
            else:
                return False
             

    def colorFul_back(self):
        toColor = ['path_prediction_ego',"ego_tracking","lane_assignement","lane_fusion","path_prediction_object","object_tracking","tsad","tslss","tsaeb"]
        for i in toColor:
            # print i
            if dictoPush[i]== 'r_ouge':
                return True
        return False

    def colorBlanc(self):
        toColor = ['path_prediction_ego',"ego_tracking","lane_assignement","lane_fusion","path_prediction_object","object_tracking","tsad","tslss","tsaeb"]
        for i in toColor:
            dictoPush[i]== 'b_lanc'

    def initAll(self):
        items = ['type', 'scenario_type', 'sub_scenario_type', 'id_senario', 'duration', 'author', 'date', 'version', 'n_iteration', 'time', 'bug_number', 'description', 'path_prediction_ego', 'ego_tracking', 'lane_assignement', 'lane_fusion', 'path_prediction_object', 'object_tracking', 'tsad', 'tslss', 'tsaeb', 'global_statuts', 'ego_distance', 'img_path', 'img_context_path', 'creat_time', 'count_in','modifier_time']
        for i in items:
            dictoPush[i] == 0
            # print i,dictoPush[i]

    def initAllOthers(self):
        dictoPush['description'] = 0
        dictoPush['bug_number'] = -1
        dictoPush['author'] = 0
        dictoPush['n_iteration'] = 0
        dictoPush['time'] = 0
        dictoPush['img_path'] = 0
        dictoPush['img_context_path'] = 0
        # items = ['author', 'n_iteration', 'time', 'bug_number', 'description', 'img_path', 'img_context_path']
        # for i in items:
        #     dictoPush[i] == 0
            # print i,dictoPush[i]


    def colorFulFinal(self):
        toColor = ['path_prediction_ego',"ego_tracking","lane_assignement","lane_fusion","path_prediction_object","object_tracking","tsad","tslss","tsaeb","global_statuts"]
        for i in toColor:
            # print i
            if dictoPush[i] == '0':
                dictoPush[i] == 'v_ert'

    def infostoPush(self,thisValidationNumber,line,positionLine,path_errorFile):
        print line #[issueID...]
        # print len(line)
        if ('Generic bug' in line) and not ("Issue" in line[3]):
# ['IssueID', ' 4', 'Generic bug', 'Bug  5', ' Fluctuation of EgoPath']
#['IssueID', ' 1', 'Generic bug', '  No Issues Found']
            dictoPush['time'] = '0'
            dictoPush['n_iteration'] = '0'
            dictoPush['bug_number'] = line[3].replace('Bug ', '').strip()
            dictoPush['description'] = line[3]+':'+line[4]
        elif (' Generic bug' in line) and not ("Issue" in line[3]):
# ['IssueID', ' 31', ' Generic bug', 'Bug  8', ' Inappropriate ObjectPath Modeling']
            dictoPush['time'] = '0'
            dictoPush['n_iteration'] = '0'
            dictoPush['bug_number'] = line[3].replace('Bug ', '').strip()
            dictoPush['description'] = line[3]+':'+line[4]
        elif ('Generic bug' in line) and ("Issue" in line[3]):
#['IssueID', ' 1', 'Generic bug', 'New Issue - No Issues Found']
# ['IssueID', ' 1', 'Generic bug', '  No Issues Found']
            dictoPush['time'] = '0'
            dictoPush['n_iteration'] = '0'
            dictoPush['bug_number'] = "-2"
            dictoPush['description'] = line[3]
        elif len(line)>6:
            if "New" in line[7]:
#['IssueID', ' 9', ' Step', ' 1695', 'Time', ' 34', '070', 'New Issue - Ego Coridor represented Wrongly']
#['IssueID', ' 8', ' Step', '  815', 'Time', ' 1350515', '662', 'New - Ego corridor represented wrongly']

                dictoPush['n_iteration'] = line[3].strip()
                dictoPush['time'] = str(line[5]+":"+line[6]).strip()
                dictoPush['bug_number'] = "-2"
                dictoPush['description'] = line[7]
            else:
#['IssueID', ' 1', ' Step', '  294', 'Time', ' 6', '043', 'Bug 29', ' ACC Target fluctuation']
#['IssueID', ' 1', ' Step', '  465', 'Time', ' 9', '460', 'Bug  0', ' Inappropriate Lines Number']
                try:
                    dictoPush['n_iteration']=line[3].strip()
                    errorsData="n_iteration not found: "+ line +"\nLog File:"+positionLine
                    self.errorWrite(path_errorFile,errorsData)
                except:
                    dictoPush['n_iteration']=''
                try:
                    dictoPush['time'] = str(line[5]+":"+line[6]).strip()
                except:
                    dictoPush['time'] ='' 
                    errorsData="time not found: "+ line +"\nLog File:"+positionLine
                    self.errorWrite(path_errorFile,errorsData)
                try:
                    dictoPush['bug_number']=line[7].replace('Bug ','').strip()
                except:
                    dictoPush['bug_number']=''
                    errorsData="bug_number not found: "+ line +"\nLog File:"+positionLine
                    self.errorWrite(path_errorFile,errorsData)
                try:
                    dictoPush['description']=line[7]+':'+line[8]
                except:
                    dictoPush['description']=''
                    errorsData="description not found: "+ line +"\nLog File:"+positionLine
                    self.errorWrite(path_errorFile,errorsData)
                
        else:
#['IssueID', ' 1', ' Step', '  294', 'Time', ' 6', '043', 'Bug 29', ' ACC Target fluctuation']
#['IssueID', ' 1', ' Step', '  465', 'Time', ' 9', '460', 'Bug  0', ' Inappropriate Lines Number']
            try:
                dictoPush['n_iteration']=line[3].strip()
            except:
                dictoPush['n_iteration']=''
                errorsData = "n_iteration not found: " + line + "\nLog File:"+positionLine
                self.errorWrite(path_errorFile, errorsData)
            try:
                dictoPush['time'] = str(line[5]+":"+line[6]).strip()
            except:
                dictoPush['time'] ='' 
                errorsData = "time not found: " + line + "\nLog File:"+positionLine
                self.errorWrite(path_errorFile, errorsData)
            try:
                dictoPush['bug_number']=line[7].replace('Bug ','').strip()
            except:
                dictoPush['bug_number']='-1'
                errorsData = "bug_number not found: " + line + "\nLog File:"+positionLine
                self.errorWrite(path_errorFile, errorsData)
            try:
                dictoPush['description']=line[7]+':'+line[8]
            except:
                dictoPush['description']=''
                errorsData = "description not found: " + line + "\nLog File:"+positionLine
                self.errorWrite(path_errorFile, errorsData)

        self.moduleInit()
        try :
            bugMo = da.bugtoModule(int(dictoPush['bug_number']))
        except:
            dictoPush['bug_number'] = '-1'
            bugMo = da.bugtoModule(int(dictoPush['bug_number']))
        if not bugMo=="nothing":
            dictoPush[bugMo] = 'r_ouge'
        else :
            self.colorBlanc()
            print 'blanc'
        dictoPush['modifier_time']=time.time()
        # if dictoPush['path_prediction_ego']+dictoPush['ego_tracking']+dictoPush['lane_assignement']+dictoPush['lane_fusion']+       dictoPush['path_prediction_object']+dictoPush['object_tracking']+dictoPush['tsad']+dictoPush['tslss']+dictoPush['tsaeb']>=100:
        if not self.ifNoBugs():
            dictoPush['global_statuts']="r_ouge"
        # print dictoPush
        # self.colorFulFinal()
        self.addValidationBug()

    def errorWrite(self,path_errorFile,errorData):
        with open(path_errorFile, 'a') as errorFile:
            errorFile.writelines(errorData)




    def pushtoData(self,path_errorFile,path_log,desti_img_path,V_ersion):
        print "===Reading log files and saving into the database==="
        try:
            lastValidationNumber = da.getNumberValidation('ID', 1)
        except IndexError:
            lastValidationNumber = 0
        dictoPush['count_in']=1
        thisValidationNumber=lastValidationNumber+1
        typeIndice=0
        self.time_dir(path_log)
        self.get_ego_distance(path_log)
        ifnoBugs = self.findIfNoBugs(path_log)
        # print ifnoBugs
        file = open(path_log,'r')
        # issueFull=False
        while True:
            line = file.readline()
            line=line.replace('\"','')
            if not line:
                break
            line = re.split(r'[:\t\n\r\f\v]',line)
            # 去除空数据
            line = [item for item in filter(lambda x:x != '', line)]
            # print line
            if 'Scenario' in line:
                positionLine=line
                lesinfos = line[2].split('\\')
                # print line[2]
                if 'ProtoAEB' in line[2]:
                    typeIndice=0
                    dictoPush['type'] = "Roulage"
                    try:
#C:\Altran\IS_ADAS_RENAULT\V1830\SUV_ADAS_V2.0_1830\SUV_ADAS_V2.0_1830\ProtoAEB\FusionAssessment\Deliveries\AdditionalTests\AdditionalTests_Day5\DoubleTargets_Cars_Oncoming\20171020_114637_RecFile_2
                        startEle = lesinfos.index('Deliveries')+1
                        endEle = len(lesinfos)-1
                        sub_scenario_type='->'.join(lesinfos[startEle:endEle])
                        # print sub_scenario_type
                        dictoPush['sub_scenario_type'] = sub_scenario_type.strip()
                        dictoPush['scenario_type'] = lesinfos[startEle-2].strip()
                        # dictoPush['version'] = lesinfos[startEle-4].strip()
                    except:
#Scenario: D:\LocalData\z023479\Desktop\EgoCaracterization\Constant_SWA\20171106_101707_RecFile_2
                        dictoPush['sub_scenario_type'] =''

                        try:
                            startEle = lesinfos.index('Constant_SWA')+1
                            dictoPush['scenario_type'] = lesinfos[startEle-2].strip()
                        except:
                            dictoPush['scenario_type'] = ''
                            errorsData="Scenario_type not found: "+ line
                            self.errorWrite(path_errorFile,errorsData)
                elif ('SimObject' in line[2]) or ('Scenarii_Data_v5.4' in line[2]):
                    typeIndice = 1
                    dictoPush['type'] = "Simobj_Normal"
                    dictoPush['scenario_type']=lesinfos[-2].strip()
                    # dictoPush['version'] = lesinfos[-5].strip() #其他版本
                    # dictoPush['version'] = lesinfos[-6].strip()   #perfect sensor
                elif ('SimObj Perfect Sensors' in line[2]) or ('Scenarii_Data_v5.7' in line[2]):
                    typeIndice = 1
                    dictoPush['type'] = "Simobj_Parfait"
                    dictoPush['scenario_type'] = lesinfos[-2].strip()
                else:
                    print "Type not found!",path_log
                    errorsData = "Type not found: " + line
                    self.errorWrite(path_errorFile, errorsData)
                    break
                # ===>===>===>===>===>===> 修改版本
                dictoPush['version'] = V_ersion
                dictoPush['id_senario'] = lesinfos[-1].strip()
            elif 'duration' in line:
                # '920ms, Num steps'
                tempSteps=line[2].split(',')
                dictoPush['duration']=str(line[1]+":"+tempSteps[0]).strip()
                # print line[3]
                # print 'duration=',dictoPush['duration']
                # print line,tempSteps
            elif not ifnoBugs:
                if 'user name' in line:
                    dictoPush['author']=line[1]
                elif 'IssueID' in line:
                    self.img_rename(path_log,desti_img_path,thisValidationNumber,line,typeIndice,path_errorFile)
                    self.infostoPush(thisValidationNumber,line,positionLine,path_errorFile)
                    # self.initAllOthers()
                    dictoPush['count_in'] = 0
                    #是否只存储一次ego distance
                    # dictoPush['ego_distance'] = 0
                    thisValidationNumber += 1
            elif ifnoBugs:
                self.moduleInit()
                self.initAllOthers()
                self.addValidationBug()
            # elif ('Ego distance:' in line) and (self.ifNoBugs()):
            #     # self.initAllOthers()
            #     self.moduleInit()
            #     self.addValidationBug()
        # if self.ifNoBugs():
        #     # self.infostoPush(thisValidationNumber, line)
        #     self.moduleInit()
        #     self.addValidationBug()
        dictoPush['count_in'] = 0
        # dictoPush['description'] = 0
        file.close()







'''

            elif 'IssueID' in line:
                if not issueFull:
                    self.img_rename(path_log,desti_img_path,thisValidationNumber,line)
                    self.infostoPush(thisValidationNumber,line)
                    issueFull=True
                else :
                    issueFull=False
                    self.img_rename(path_log,desti_img_path,thisValidationNumber,line)
                    self.infostoPush(thisValidationNumber,line)

# print ','.join(lesinfos)
# print da.bugtoModule(int(dictoPush['bug_number']))
# print "dictoPush[%s]="%(da.bugtoModule(int(dictoPush['bug_number']))),dictoPush[da.bugtoModule(int(dictoPush['bug_number']))]

# print lastValidationNumber
# print os.path.dirname(path)
# print 'lastValidationNumber=',lastValidationNumber
# print dictoPush
# for key, value in dictoPush.items():
#     print key, ':',  value



dictoPush['path_prediction_ego']=
dictoPush['ego_tracking']=
dictoPush['lane_assignement']=
dictoPush['lane_fusion']=
dictoPush['path_prediction_object']=
dictoPush['object_tracking']=
dictoPush['tsad']=
dictoPush['tslss']=
dictoPush['tsaeb']=

da.updateValidation('img_path','c:/','1')

'''
        
