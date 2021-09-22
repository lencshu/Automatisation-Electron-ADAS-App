#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$


import database
# from database import database



da = database.dataAdas()

dictoPush = {}.fromkeys(['version','indice','type','scenario_type','number_bugs','success_rate','number_scenerios_bugs','number_scenerios_all','total_duration_scenarios','total_distances','bug0','bug1','bug2','bug3','bug4','bug5','bug6','bug7','bug8','bug9','bug10','bug11','bug12','bug13','bug14','bug15','bug16','bug17','bug18','bug19','bug20','bug21','bug22','bug23','bug24','bug25','bug26','bug27','bug28','bug29','bug30','bug31','bug32','bug33','bug34','bug35','bug36','bug37','bug38','bug39','bug40','bug41','bug42'], 0)

itemsBug=['bug0','bug1','bug2','bug3','bug4','bug5','bug6','bug7','bug8','bug9','bug10','bug11','bug12','bug13','bug14','bug15','bug16','bug17','bug18','bug19','bug20','bug21','bug22','bug23','bug24','bug25','bug26','bug27','bug28','bug29','bug30','bug31','bug32','bug33','bug34','bug35','bug36','bug37','bug38','bug39','bug40','bug41','bug42']

class analyse(object):
    """docstring for analyse"""

    def __init__(self):
        super(analyse, self).__init__()

    def bugCount(self,index,datas):
        BugN='bug'+str(datas[index][11])
        try:
            dictoPush[BugN]=dictoPush[BugN]+1
        except :
            print 'No such bug:', BugN

    def initAll(self):
        allItems=['version','indice','type','scenario_type','number_bugs','success_rate','number_scenerios_bugs','number_scenerios_all','total_duration_scenarios','total_distances','bug0','bug1','bug2','bug3','bug4','bug5','bug6','bug7','bug8','bug9','bug10','bug11','bug12','bug13','bug14','bug15','bug16','bug17','bug18','bug19','bug20','bug21','bug22','bug23','bug24','bug25','bug26','bug27','bug28','bug29','bug30','bug31','bug32','bug33','bug34','bug35','bug36','bug37','bug38','bug39','bug40','bug41','bug42']
        for i in allItems:
            dictoPush[i]=0

    def infoToPush(self):
        da.addAnalyse(dictoPush['version'],dictoPush['indice'],dictoPush['type'],dictoPush['scenario_type'],dictoPush['number_bugs'],dictoPush['success_rate'],dictoPush['number_scenerios_bugs'],dictoPush['number_scenerios_all'],dictoPush['total_duration_scenarios'],dictoPush['total_distances'],dictoPush['bug0'],dictoPush['bug1'],dictoPush['bug2'],dictoPush['bug3'],dictoPush['bug4'],dictoPush['bug5'],dictoPush['bug6'],dictoPush['bug7'],dictoPush['bug8'],dictoPush['bug9'],dictoPush['bug10'],dictoPush['bug11'],dictoPush['bug12'],dictoPush['bug13'],dictoPush['bug14'],dictoPush['bug15'],dictoPush['bug16'],dictoPush['bug17'],dictoPush['bug18'],dictoPush['bug19'],dictoPush['bug20'],dictoPush['bug21'],dictoPush['bug22'],dictoPush['bug23'],dictoPush['bug24'],dictoPush['bug25'],dictoPush['bug26'],dictoPush['bug27'],dictoPush['bug28'],dictoPush['bug29'],dictoPush['bug30'],dictoPush['bug31'],dictoPush['bug32'],dictoPush['bug33'],dictoPush['bug34'],dictoPush['bug35'],dictoPush['bug36'],dictoPush['bug37'],dictoPush['bug38'],dictoPush['bug39'],dictoPush['bug40'],dictoPush['bug41'],dictoPush['bug42'])

    # def datasToPush(self,dict):
    #     for i in dict:
    #         data_cmd=
    #     da.addAnalyse()
    
    def init(self):
        # for i in range(1,len(dictoPush)):
        for i in dictoPush:
            if i!='version':
                dictoPush[i]=0
                # print i,dictoPush[i]
            
 

    def sToMiS(self,t):
        t=t.replace('s','').replace('m','').split(':')
        toT=0
        for i in range(0,len(t)-1):
            toT=1000*int(t[i])+toT
        toT=toT+int(t[-1])
        return toT

    def analyseParType_back(self, type):
        datas = da.getdatas('DataAdas')
        numB = 0
        numSce = 0
        dictoPush['version'] = datas[0][8]
        for i in range(0, len(datas)):
            numB = numB+1
            self.bugCount(i, datas)
            # print datas[i]
            # print datas[i][5],datas[i][23],datas[i][8]
            if dictoPush['version'] == datas[i][8]:
                if int(datas[i][27]) == 1:  # count_in
                    numSce = numSce+1
                    # print datas[i]
                    dictoPush['total_duration_scenarios'] = self.sToMiS(
                        datas[i][5])+dictoPush['total_duration_scenarios']
                    dictoPush['total_distances'] = float(
                        datas[i][23].replace(',', '.'))+dictoPush['total_distances']
            else:
                dictoPush['number_scenerios'] = numSce
                dictoPush['number_bugs'] = numB
                # print dictoPush
                print dictoPush['version']
                self.infoToPush()
                self.init()
                dictoPush['version'] = datas[i][8]

            # self.bugCount(i,datas)
            # print datas[i]
        dictoPush['number_scenerios'] = numSce
        dictoPush['number_bugs'] = numB
        self.infoToPush()
        # print dictoPush
        #

    def getVersion(self):
        allVersion=[]
        version=''
        datas = da.getdatas('DataAdas')
        
        for i in range(0, len(datas)):
            if version != str(datas[i][8]):
                version = str(datas[i][8])
                allVersion.append(version)
        allVersion = sorted(set(allVersion))
        return allVersion

    def analyseParType(self, type,version):
        datas = da.getdatas('DataAdas')
        dictoPush['type'] = type
        numB = 0
        numSce = 0
        numSce_bug = 0
        for i in range(0, len(datas)):
            if (datas[i][1]==type) and (datas[i][8]==version):
                numB = numB+1
                self.bugCount(i, datas)
                dictoPush['version'] = version
                if int(datas[i][27]) == 1:  # count_in
                        numSce = numSce+1
                        if datas[i][22]=='r_ouge':
                            numSce_bug = numSce_bug+1
                        dictoPush['total_duration_scenarios']=self.sToMiS(datas[i][5])+dictoPush['total_duration_scenarios']
                        dictoPush['total_distances'] = float(datas[i][23].replace(',', '.'))+dictoPush['total_distances']

        dictoPush['number_scenerios_all'] = numSce
        dictoPush['total_duration_scenarios']=float(dictoPush['total_duration_scenarios'])/3600000
        dictoPush['total_distances']=float(dictoPush['total_distances'])/1000
        dictoPush['number_scenerios_bugs'] = numSce_bug
        dictoPush['number_bugs'] = numB
        if dictoPush['number_scenerios_all']!=0:
            dictoPush['success_rate']=float(dictoPush['number_scenerios_all']-dictoPush['number_scenerios_bugs'])/dictoPush['number_scenerios_all']
        dictoPush['indice']=type
        print dictoPush
        self.infoToPush()
        dictoPush['indice']=type + '_BugScenario'
        for i in itemsBug:
            if dictoPush['number_scenerios_all']!=0:
                dictoPush[i] = float(dictoPush[i])/dictoPush['number_scenerios_all']
        self.infoToPush()
        dictoPush['indice'] = type + '_BugHeure'
        for i in itemsBug:
            if dictoPush['total_duration_scenarios']!=0:
                dictoPush[i] = float(dictoPush[i])*dictoPush['number_scenerios_all']/dictoPush['total_duration_scenarios']
        self.infoToPush()
        dictoPush['indice'] = type + '_BugKm'
        for i in itemsBug:
            if dictoPush['total_distances']!=0:
                dictoPush[i] = float(dictoPush[i])*dictoPush['total_duration_scenarios']/dictoPush['total_distances']
        self.infoToPush()
        dictoPush['indice'] = type + '_BugBugs'
        for i in itemsBug:
            if dictoPush['number_bugs']!=0:
                dictoPush[i] = float(dictoPush[i])*dictoPush['total_distances']/dictoPush['number_bugs']
        self.infoToPush()
        # dictoPush['indice'] = '0'
        self.initAll()

    def analyse(self):
        allV=self.getVersion()
        allExisteV = da.getAllExisteVersion()
        # print allExisteV
        # print allV
        for v in allV:
            if not v in allExisteV:
                self.analyseParType('Roulage', v)
                self.analyseParType('Simobj_Normal', v)
                self.analyseParType('Simobj_Parfait', v)



                        


    





