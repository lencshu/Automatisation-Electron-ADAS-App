#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$


import sqlite3
import time
import os
import globalVariable as go

"""
methode:

dataAdas.addTable_validation()
dataAdas.addTable_Bug()
dataAdas.addValidation(type,scenario_type,id_senario,duration,author,date,version,n_iteration ,time,bug_number,description,path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time)
dataAdas.getValidation(self,column)
dataAdas.getLastValidation(self,column,N)
dataAdas.getNumberValidation(self,column,N)
dataAdas.addBug(self,r1,r2='',r3='',r4='',r5='',r6='')
dataAdas.getBug(self,n)
dataAdas.bugtoModule(self,n)
"""



class dataAdas(object):
    """docstring for dataAdas"""
    def __init__(self):
    # def __init__(self,datapath):
        super(dataAdas, self).__init__()
        # self.datapath = datapath

    def dir_exist(self, dirname):
        if not os.path.exists(dirname):
             os.mkdir(dirname)

    def connect(self):
        datapath = go.get_value('datapath')
        self.dir_exist(datapath)
        dataFile = datapath+"/DataAdas.db"
    #   con=sqlite3.connect('./Database/DataAdas.db')
        con = sqlite3.connect(dataFile)
        # con=sqlite3.connect(self.datapath)
    #   print "Connect database successfully"
        return con

    def addTable_validation(self):
        conn = self.connect()
        # print "Opened database successfully";
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE DataAdas
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       type           TEXT,
       scenario_type           TEXT,
       sub_scenario_type    TEXT,
       id_senario            TEXT,
       duration        TEXT,
       author         TEXT,
       date    TEXT,
       version TEXT,
       n_iteration  TEXT,
       time     TEXT,
       bug_number      TEXT,
       description      TEXT,
       path_prediction_ego   TEXT,
       ego_tracking     TEXT,
       lane_assignement     TEXT,
       lane_fusion      TEXT,
       path_prediction_object   TEXT,
       object_tracking  TEXT,
       tsad TEXT,
       tslss TEXT,
       tsaeb    TEXT,
       global_statuts   TEXT,
       ego_distance   TEXT,
       img_path   TEXT,
       img_context_path   TEXT,
       creat_time   TEXT,
       count_in     TEXT,
       modifier_time   TEXT);''')
        conn.commit()
        print "Validation Table created successfully";


    def addValidation(self,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26='',r27=''):
        t=str(time.time())
        exCommand = 'INSERT INTO DataAdas (type,scenario_type,id_senario,duration,author,date,version,n_iteration ,time,bug_number,description,path_prediction_ego,ego_tracking,lane_assignement,lane_fusion,path_prediction_object,object_tracking,tsad,tslss,tsaeb,global_statuts,ego_distance,img_path,img_context_path,creat_time,sub_scenario_type,count_in,modifier_time) values (\"'+str(r1)+'\",\"'+str(
            r2)+'\",\"'+str(r3)+'\",\"'+str(r4)+'\",\"'+str(r5)+'\",\"'+str(r6)+'\",\"'+str(r7)+'\",\"'+str(r8)+'\",\"'+str(r9)+'\",\"'+str(r10)+'\",\"'+str(r11)+'\",\"'+str(r12)+'\",\"'+str(r13)+'\",\"'+str(r14)+'\",\"'+str(r15)+'\",\"'+str(r16)+'\",\"'+str(r17)+'\",\"'+str(r18)+'\",\"'+str(r19)+'\",\"'+str(r20)+'\",\"'+str(r21)+'\",\"'+str(r22)+'\",\"'+str(r23)+'\",\"'+str(r24)+'\",\"'+str(r25)+'\",\"'+str(r26)+'\",\"'+str(r27)+'\",\"'+t+'\")'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        conn.commit()
        print "Validations created successfully"#,exCommand

    def addMultiValidation(self,r1,r2=''):
        exCommand='INSERT INTO DataAdas ('+str(r1)+') values (\"'+str(r2)+'\")'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        conn.commit()
        print "Multi-validations created successfully"#,exCommand

        # UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
    def updateValidationTime(self,r1,r2,r3):
        t=str(time.time())
        exCommand='UPDATE DataAdas SET '+str(r1)+'=\"'+str(r2)+'\",modifier_time='+t+' WHERE ID='+str(r3)+';'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        # cursor.execute('''UPDATE DataAdas SET ?=?,modifier_time=? WHERE ID=?;'''%(r1,r2,t,r3))
        conn.commit()
        print "Validations updated successfully"#,exCommand

    def updateValidation(self,r1,r2,r3):
        exCommand='UPDATE DataAdas SET '+str(r1)+'=\"'+str(r2)+'\" WHERE ID='+str(r3)+';'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        # cursor.execute('''UPDATE DataAdas SET ?=?,modifier_time=? WHERE ID=?;'''%(r1,r2,t,r3))
        conn.commit()
        print "Validations updated successfully"#,exCommand

    def getValidation(self,column):
        exCommand='SELECT '+str(column)+' FROM DataAdas;'
        print exCommand
        conn = self.connect()
        c = conn.cursor()
        cursor = c.execute(exCommand)
        print 'Get Validation successfully'
        return cursor.fetchall()

    def getNumberValidation(self,column,N):
        exCommand='SELECT '+str(column)+' FROM DataAdas;'
        # print exCommand
        # conn = self.connect()
        # conn = sqlite3.connect('./Database/DataAdas.db')
        conn = self.connect()
        c = conn.cursor()
        cursor = c.execute(exCommand)
        print 'Get the last ',N,'th Validation successfully'
        return cursor.fetchall()[-N][-1]

    def getLastValidation(self,column,N):
        exCommand='SELECT '+str(column)+' FROM DataAdas;'
        # print exCommand
        conn = self.connect()
        c = conn.cursor()
        cursor = c.execute(exCommand)
        print 'Get the last ',N,'th line of Validation successfully'
        return cursor.fetchall()[-N]

    def addTable_Bug(self):
        conn = self.connect()
        # print "Opened database successfully";
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE Bugs
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       bug_number           TEXT,
       issue            TEXT,
       description     TEXT,
       issues_dependency        TEXT,
       module_related_n   TEXT,
       module_related   TEXT);''')
        conn.commit()
        print "Bugs Table created successfully";

    def addTable_Bug_fusion(self):
        conn = self.connect()
        # print "Opened database successfully";
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE Bugs_fusion
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       bug_number           TEXT,
       issue            TEXT,
       description     TEXT,
       issues_dependency        TEXT,
       module_related_n   TEXT,
       module_related   TEXT);''')
        conn.commit()
        print "Bugs_fusion Table created successfully"


    def addBug(self,r1,r2='',r3='',r4='',r5='',r6=''):
        exCommand='INSERT INTO Bugs (bug_number,issue,description,issues_dependency,module_related_n,module_related) values (\"'+str(r1)+'\",\"'+str(r2)+'\",\"'+str(r3)+'\",\"'+str(r4)+'\",\"'+str(r5)+'\",\"'+str(r6)+'\")'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        conn.commit()
        # print "Bugs created successfully"#,exCommand

    def addBugAll(self):
        self.addBug(0,"Bug NaN: No fbi file", "The fbi file doesn't exist ")
        self.addBug(1,"Bug N°1: Inappropriate Lines Number", " The number of Lines is not correct")
        self.addBug(2,"Bug N°2: Fluctuation of Lines", "The Lines disappear and reappear ")
        self.addBug(3,"Bug N° 3:Incorrect Ego LaneAssignement", "Inappropriate LaneAssignement for Ego vehicle ")
        self.addBug(4,"Bug N°4 : Incorrect Objet LaneAssignement", "Inappropriate LaneAssignement for objects ")
        self.addBug(5,"Bug N°5 : Disappearance of EgoPath", "Disappearance of EgoPath")
        self.addBug(6,"Bug N°6: Fluctuation of EgoPath", " The Path of the ego goes in all directions and does not respect the normal trajectory")
        self.addBug(7,"Bug N°7: The EgoPath does not follow the curves", " the EgoPath does not follow curves , it does not respect the lane modeling")
        self.addBug(8,"Bug N°8: Disappearance of ObjectPath", "Disappearance of ObjectPath")
        self.addBug(9,"Bug N°9: Inappropriate ObjectPath Modeling", "The modeling of ObjectPath is Inappropriate (after cut in, curves...) ,does not respect the lane modeling or  ObjectPath does not follow curves , it does not respect the lane modeling ")
        self.addBug(10,"Bug N°10: Incorrect  Ego's speed", "The ego does not have the right described speed , or its speed exceeds the threshold")
        self.addBug(11,"Bug N°11: Incorrect Object's speed", "The object does not have the right described speed , or its speed exceeds the threshold")
        self.addBug(12,"Bug N°12: Double detected object", "Detection of more than one object when there is only one")
        self.addBug(13,"Bug N°13: Undetected object by Fusion", "Undetected object , we  don't have the fused object , but we have the tracked objet , the measured object  and  the context view object ")
        self.addBug(14,"Bug N°14 : False AEB detection", "A false detection of the AEB target : on a double object, on a  unseen detected object , on a static lateral targets or dynamic lateral targets due to the Inappropriate modeling of their trajectory")
        self.addBug(15,"Bug N°15: False ACC detection", "A false detection of the ACC target : on a double object, on a  unseen detected object ,static lateral targets ")
        self.addBug(16,"Bug N°16: False  LSS detection", "False detection of the LSS target")
        self.addBug(17,"Bug N°17:Inappropriate CIPV /TTC indicator", " problem of TSAEB with CIPV/TTC Label even when approaching the collision")
        self.addBug(18,"Bug N°18: Incorrect ACC Number [XX]", "The ACC target changes number [XX] even if it keeps the same position")
        self.addBug(19,"Bug N°19:Undetected LSS Target", "Undetected LSS Target")
        self.addBug(20,"Bug N°20: AEB Target  fluctuation", "The AEB target is not stable")
        self.addBug(21,"Bug N°21: PB Statut Or Fusion Crash ")
        self.addBug(22,"Bug N°22:  False positive object detection", "Object false detection  ")
        self.addBug(24,"Bug N°24: Inappropriate Lines modeling", "Inappropriate Lines modeling ,the lines are not complete ,chaotic lines modeling ")
        self.addBug(25,"Bug N°25: Undetected AEB target", "Object not detected as AEB target")
        self.addBug(26,"Bug N°26: Undetected ACC target", "Object not detected as ACC target")
        self.addBug(27,"Bug N°27: Unseen detected object", "An unseen detected object  appears in the fusion display but it is not represented in the context view ,we have the fused object , the tracked objet and the measured object , but it's a ghost object that does not exit in the context view")
        self.addBug(28,"Bug N°28: Incorrect ObjectPath for static object", "Static Object with Path ")
        self.addBug(29,"BugN°29 : Fluctuation of object path", " object path is fluctuating to the left and right ,or disappears ")
        self.addBug(30,"Bug N°30: ACC Target  fluctuation", "The ACC target is not stable")
        self.addBug(31,"Bug N°31:Inappropriate object position", "Inappropriate representation of object position")
        self.addBug(32,"Bug N°32: EgoPath is a circle-like", "The Path of the ego  is a circle-like  and does not respect the normal trajectory")
        self.addBug(34,"Bug N°34:  Object Fluctuation", "The Object is not stable , it disappear and reappear")
        self.addBug(35,"Bug N°35: LSS  Target  fluctuation", "The LSS target is not stable")
        self.addBug(37,"Bug N°37: Undetected object by sensors", "Undetected object , we  don't have the measured object and the fused object , but we have the context view object , it might be sensors problems ")
        self.addBug(38,"Bug N°38: Incorrect EgoPath", " the EgoPath does not follow the normal trajectory of the ego   ")
        self.addBug(39,"Bug N°39: Bad Maneuver Prediction", "Bad Maneuver Prediction  ")
        self.addBug(40,"BugN°40: Incorrect anchor point", " The anchor point is not correctly located on the object. For example it is located on the lateral side of object instead of its behind")
        self.addBug(41,"BugN°41: Bad bounding box modeling", "The size or the direction of bounding box  is not correct ")


    def addBug_fusion(self,r1,r2='',r3='',r4='',r5='',r6=''):
        exCommand='INSERT INTO Bugs_fusion (bug_number,issue,description,issues_dependency,module_related_n,module_related) values (\"'+str(r1)+'\",\"'+str(r2)+'\",\"'+str(r3)+'\",\"'+str(r4)+'\",\"'+str(r5)+'\",\"'+str(r6)+'\")'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        conn.commit()
        print "Bugs_fusion created successfully",#,exCommand

    def getBug(self,n):
        exCommand='SELECT bug_number,issue,description,issues_dependency,module_related_n,module_related FROM Bugs WHERE bug_number='+str(n)+';'
        # print exCommand
        conn = self.connect()
        c = conn.cursor()
        cursor = c.execute(exCommand)
        print 'Get infos of Bug successfully'
        return cursor.fetchall()

    def bugtoModule(self,n):
        return { 
        0:'lane_fusion',
        1:'lane_fusion',
        2:'lane_assignement',
        3:'lane_assignement',
        4:'path_prediction_ego',
        5:'path_prediction_ego',
        6:'path_prediction_ego',
        7:'path_prediction_object',
        8:'path_prediction_object',
        9:'ego_tracking',
        10:'object_tracking',
        11:'object_tracking',
        12:'object_tracking',
        13:'tsaeb',
        14:'tsad',
        15:'tslss', #16 deleted
        16:'tsaeb',
        17:'tsad',
        18:'tslss', #19 deleted
        19:'tsaeb',
        20:'nothing',
        21:'object_tracking',
        22:'Lane Fusion',
        24:'tsaeb',
        25:'tslss',
        26:'object_tracking',
        27:'path_prediction_object',
        28:'path_prediction_object',
        29:'tslss',
        30:'object_tracking',
        31:'path_prediction_ego',
        32:'nothing',
        34:'nothing', #35 deleted
        37:'object_tracking',
        38:'path_prediction_ego',
        39:'path_prediction_ego',
        40:'object_tracking',
        41:'object_tracking',
        45:'Bug NaN: No fbi file'
        }.get(n, 'Not defined')

    def bugtoModuleExcel(self,n):
        return { 
        1:'lane_fusion',
        2:'lane_fusion',
        3:'lane_assignement',
        4:'lane_assignement',
        5:'path_prediction_ego',
        6:'path_prediction_ego',
        7:'path_prediction_ego',
        8:'path_prediction_object',
        9:'path_prediction_object',
        10:'ego_tracking',
        11:'object_tracking',
        12:'object_tracking',
        13:'object_tracking',
        14:'tsaeb',
        15:'tsad',
        16:'tslss',
        17:'tsaeb',
        18:'tsad',
        19:'tslss',
        20:'tsaeb',
        21:'nothing',
        22:'object_tracking',
        24:'Lane Fusion',
        25:'tsaeb',
        26:'tslss',
        27:'object_tracking',
        28:'path_prediction_object',
        29:'path_prediction_object',
        30:'tslss',
        31:'object_tracking',
        32:'path_prediction_ego',
        34:'nothing',
        35:'nothing',
        37:'object_tracking',
        38:'path_prediction_ego',
        39:'path_prediction_ego',
        40:'object_tracking',
        41:'object_tracking',
        0:'Bug NaN: No fbi file'
        }.get(n, 'Not defined')

    def bugNumberToName(self,n):
        return {
        1:'dsafdsaflane_fusion',
        2:'lane_fusion',
        3:'lane_assignement',
        4:'lane_assignement',
        5:'path_prediction_ego',
        6:'path_prediction_ego',
        7:'path_prediction_ego',
        8:'path_prediction_object',
        9:'path_prediction_object',
        10:'ego_tracking',
        11:'object_tracking',
        12:'object_tracking',
        13:'object_tracking',
        14:'tsaeb',
        15:'tsad',
        16:'tslss',
        17:'tsaeb',
        18:'tsad',
        19:'tslss',
        20:'tsaeb',
        21:'nothing',
        22:'object_tracking',
        24:'Lane Fusion',
        25:'tsaeb',
        26:'tslss',
        27:'object_tracking',
        28:'path_prediction_object',
        29:'path_prediction_object',
        30:'tslss',
        31:'object_tracking',
        32:'path_prediction_ego',
        34:'nothing',
        35:'nothing',
        37:'object_tracking',
        38:'path_prediction_ego',
        39:'path_prediction_ego',
        40:'object_tracking',
        41:'object_tracking',
        0:'Bug NaN: No fbi file'
        }.get(n, 'Not defined')

    def bugListToBugFusionRunner(self,n):
        return {
        1:'sdfsadfsadlane_fusion',
        2:'lane_fusion',
        3:'lane_assignement',
        4:'lane_assignement',
        5:'path_prediction_ego',
        6:'path_prediction_ego',
        7:'path_prediction_ego',
        8:'path_prediction_object',
        9:'path_prediction_object',
        10:'ego_tracking',
        11:'object_tracking',
        12:'object_tracking',
        13:'object_tracking',
        14:'tsaeb',
        15:'tsad',
        16:'tslss',
        17:'tsaeb',
        18:'tsad',
        19:'tslss',
        20:'tsaeb',
        21:'nothing',
        22:'object_tracking',
        24:'Lane Fusion',
        25:'tsaeb',
        26:'tslss',
        27:'object_tracking',
        28:'path_prediction_object',
        29:'path_prediction_object',
        30:'tslss',
        31:'object_tracking',
        32:'path_prediction_ego',
        34:'nothing',
        35:'nothing',
        37:'object_tracking',
        38:'path_prediction_ego',
        39:'path_prediction_ego',
        40:'object_tracking',
        41:'object_tracking',
        0:'Bug NaN: No fbi file'
        }.get(n, 'Not defined')


    def BugFusionRunnerToBugList(self,n):
        return {
        1:'1',
        2:'3',
        3:'4',
        4:'5',
        5:'6',
        6:'7',
        7:'8',
        8:'9',
        9:'10',
        10:'ego_tracking',
        11:'object_tracking',
        12:'object_tracking',
        13:'object_tracking',
        14:'tsaeb',
        15:'tsad',
        16:'tslss',
        17:'tsaeb',
        18:'tsad',
        19:'tslss',
        20:'tsaeb',
        21:'nothing',
        22:'object_tracking',
        24:'Lane Fusion',
        25:'tsaeb',
        26:'tslss',
        27:'object_tracking',
        28:'path_prediction_object',
        29:'path_prediction_object',
        30:'tslss',
        31:'object_tracking',
        32:'path_prediction_ego',
        34:'nothing',
        35:'nothing',
        37:'object_tracking',
        38:'path_prediction_ego',
        39:'path_prediction_ego',
        40:'object_tracking',
        41:'object_tracking',
        0:'1'
        }.get(n, 'Not defined')

    def addTable_analyse(self):
        conn = self.connect()
        # print "Opened database successfully";
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE Analyse
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        version           TEXT,
        indice          TEXT,
        type           TEXT,
        scenario_type           TEXT,
        number_bugs           TEXT,
        success_rate           TEXT,
        number_scenerios_bugs    TEXT,
        number_scenerios_all    TEXT,
        total_duration_scenarios           TEXT,
        total_distances         TEXT,
        bug0        TEXT,
        bug1        TEXT,
        bug2        TEXT,
        bug3        TEXT,
        bug4        TEXT,
        bug5        TEXT,
        bug6        TEXT,
        bug7        TEXT,
        bug8        TEXT,
        bug9        TEXT,
        bug10       TEXT,
        bug11       TEXT,
        bug12       TEXT,
        bug13       TEXT,
        bug14       TEXT,
        bug15       TEXT,
        bug16       TEXT,
        bug17       TEXT,
        bug18       TEXT,
        bug19       TEXT,
        bug20       TEXT,
        bug21       TEXT,
        bug22       TEXT,
        bug23       TEXT,
        bug24       TEXT,
        bug25       TEXT,
        bug26       TEXT,
        bug27       TEXT,
        bug28       TEXT,
        bug29       TEXT,
        bug30       TEXT,
        bug31       TEXT,
        bug32       TEXT,
        bug33       TEXT,
        bug34       TEXT,
        bug35       TEXT,
        bug36       TEXT,
        bug37       TEXT,
        bug38       TEXT,
        bug39       TEXT,
        bug40       TEXT,
        bug41       TEXT,
        bug42       TEXT,
        modifier_time   TEXT);''')
        conn.commit()
        print "Analyse Table created successfully";

    def addAnalyse(self,r1,r2='',r3='',r4='',r5='',r6='',r7='',r8='',r9='',r10='',r11='',r12='',r13='',r14='',r15='',r16='',r17='',r18='',r19='',r20='',r21='',r22='',r23='',r24='',r25='',r26='',r27='',r28='',r29='',r30='',r31='',r32='',r33='',r34='',r35='',r36='',r37='',r38='',r39='',r40='',r41='',r42='',r43='',r44='',r45='',r46='',r47='',r48='',r49='',r50='',r51='',r52='',r53=''):
        t=str(time.time())
        exCommand = 'INSERT INTO Analyse (version,indice,type,scenario_type,number_bugs,success_rate,number_scenerios_bugs,number_scenerios_all,total_duration_scenarios,total_distances,bug0,bug1,bug2,bug3,bug4,bug5,bug6,bug7,bug8,bug9,bug10,bug11,bug12,bug13,bug14,bug15,bug16,bug17,bug18,bug19,bug20,bug21,bug22,bug23,bug24,bug25,bug26,bug27,bug28,bug29,bug30,bug31,bug32,bug33,bug34,bug35,bug36,bug37,bug38,bug39,bug40,bug41,bug42,modifier_time) values (\"'+str(r1)+'\",\"'+str(
            r2)+'\",\"'+str(r3)+'\",\"'+str(r4)+'\",\"'+str(r5)+'\",\"'+str(r6)+'\",\"'+str(r7)+'\",\"'+str(r8)+'\",\"'+str(r9)+'\",\"'+str(r10)+'\",\"'+str(r11)+'\",\"'+str(r12)+'\",\"'+str(r13)+'\",\"'+str(r14)+'\",\"'+str(r15)+'\",\"'+str(r16)+'\",\"'+str(r17)+'\",\"'+str(r18)+'\",\"'+str(r19)+'\",\"'+str(r20)+'\",\"'+str(r21)+'\",\"'+str(r22)+'\",\"'+str(r23)+'\",\"'+str(r24)+'\",\"'+str(r25)+'\",\"'+str(r26)+'\",\"'+str(r27)+'\",\"'+str(r28)+'\",\"'+str(r29)+'\",\"'+str(r30)+'\",\"'+str(r31)+'\",\"'+str(r32)+'\",\"'+str(r33)+'\",\"'+str(r34)+'\",\"'+str(r35)+'\",\"'+str(r36)+'\",\"'+str(r37)+'\",\"'+str(r38)+'\",\"'+str(r39)+'\",\"'+str(r40)+'\",\"'+str(r41)+'\",\"'+str(r42)+'\",\"'+str(r43)+'\",\"'+str(r44)+'\",\"'+str(r45)+'\",\"'+str(r46)+'\",\"'+str(r47)+'\",\"'+str(r48)+'\",\"'+str(r49)+'\",\"'+str(r50)+'\",\"'+str(r51)+'\",\"'+str(r52)+'\",\"'+str(r53)+'\",\"'+t+'\")'
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(exCommand)
        conn.commit()
        print "Analyses created successfully"#,exCommand

    def GetTables(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("select name from sqlite_master where type='table' order by name")
            # print cursor.fetchall()
            return cursor.fetchall()
        except sqlite3.Error, e:
            print e

    def getdatas(self,tablename):
        try:
            cmd="select * from "+tablename+" order by ID"
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(cmd)
            # print cursor.fetchall()
            print 'get all infos from:',tablename
            return cursor.fetchall()
        except sqlite3.Error, e:
            print e


    def getAllExisteVersion(self):
        allist=[]
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("select version from Analyse")
            # print cursor.fetchall()
            liste = sorted(set(cursor.fetchall()))
            for i in range(0,len(liste)):
                # print liste[i][-1]
                allist.append(liste[i][-1])
            return allist
        except sqlite3.Error, e:
            print e

    def ignoreNullBug(self):
        cmd="select * from DataAdas order by ID"
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(cmd)
        liste = cursor.fetchall()
        N=0
        # print liste
#(16, u'Simobj_Normal', u'AEB20', u'0', u'S11_6', u'9s:920ms', u' AR', u'22/8/2018', u'f', u'450', u'9:168', u'12', u'Bug 12: Undetected object by Fusion', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'r_ouge', u'v_ert', u'v_ert', u'v_ert', u'r_ouge', u'164,544540', u'./Database/imgs_log/ID_3_Step_450.png', u'./Database/imgs_log/ID_3_Step_450_context.png', u'11h9min44sec,22,8', u'0', u'1537173603.05')
        for i in range(0, len(liste)):
            if liste[i][6] == '0' and liste[i][12] == '0' and liste[i][11] != '-1':
                N=N+1
                exCommand = 'UPDATE DataAdas SET bug_number="-1" WHERE ID='+str(i+1)+';'
                print N,exCommand, liste[i][6], liste[i][11]
                cursor.execute(exCommand)
                conn.commit()
        print N


    def get_number(self,x):
        return float(filter(str.isdigit, str(x)))

    def timeShift(self):
        cmd="select * from DataAdas order by ID"
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(cmd)
        liste = cursor.fetchall()
        N=0
        #(1, u'Simobj_Parfait', u'AEB20', u'0', u'S1', u'4s:320ms', u'0', u'1/8/2018', u'V1830', u'0', u'0', u'-1', u'0', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'51,476219', u'0', u'0', u'10h13min48sec,1,8', u'1', u'1533899903.49')
        print liste
        for i in range(0, len(liste)):
            if liste[i][5] != '0':
                timeChange = liste[i][5].replace('s', '').replace('m', '').split(':')
                # for ii in timeChange:
                N=N+1
                exCommand = 'UPDATE DataAdas SET bug_number="-1" WHERE ID='+str(i+1)+';'
                print N,exCommand, liste[i][12], liste[i][11]
                cursor.execute(exCommand)
                conn.commit()
        # print N


    def versionChange(self,versionSelect):
        cmd="select * from DataAdas order by ID"
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(cmd)
        liste = cursor.fetchall()
        N=0
        # print liste
#(16, u'Simobj_Normal', u'AEB20', u'0', u'S11_6', u'9s:920ms', u' AR', u'22/8/2018', u'f', u'450', u'9:168', u'12', u'Bug 12: Undetected object by Fusion', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'v_ert', u'r_ouge', u'v_ert', u'v_ert', u'v_ert', u'r_ouge', u'164,544540', u'./Database/imgs_log/ID_3_Step_450.png', u'./Database/imgs_log/ID_3_Step_450_context.png', u'11h9min44sec,22,8', u'0', u'1537173603.05')
        for i in range(0, len(liste)):
            N=N+1
            print N,liste[i][8]
            exCommand = 'UPDATE DataAdas SET version="'+ versionSelect +'" WHERE ID='+str(i+1)+';'
            cursor.execute(exCommand)
            conn.commit()
        print N
