#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$


import ConfigParser
import os

currentDir = os.getcwd()
parentDir = os.path.abspath(os.path.join(currentDir, os.pardir))  # 父路径
logDir = parentDir+"/3.Htmls/resources/app/Database/"
conObj = ConfigParser.ConfigParser()
iniPath = currentDir+"\\ADASet.ini"
iniExiste = os.path.exists(iniPath)
conObj.read(iniPath)

class iniConfig(object):
    def __init__(self):
        super(iniConfig, self).__init__()

    def confReadOrAdd(self,userName, option):
        conObj.read(iniPath)
        try:
            value = conObj.get(userName, option)
        except :
            value = self.userExiste(userName, option)
        return value
    
    def creatConfig(self, userName):
        conObj.read(iniPath)
        conObj.add_section(userName)
        print "Enter the Path of Emballer_logs(example: C:\Users\gli\Desktop\_Travail\Emballer_logs): "
        value_Emballer_logs = raw_input() or 'C:\Users\gli\Desktop\_Travail\Emballer_logs'
        conObj.set(userName, 'Emballer_logs', value_Emballer_logs)
        print "Enter the Path of Database(Default: ../3.Htmls/resources/app/Database): "
        value_datapath = raw_input() or logDir
        try:
            if not os.path.exists(value_datapath):
                os.mkdir(value_datapath)
        except :
            print "Error: Path HTML not Found ! \n"
            value_datapath = './Database/'
        else:
            pass
        value_datapath = os.path.abspath(value_datapath)
        conObj.set(userName, 'datapath', value_datapath)
        value_logs_backup = os.path.abspath(os.path.join(value_Emballer_logs, os.pardir)) +'\\logs_backup'
        conObj.set(userName, 'logs_backup', value_logs_backup)
        value_imgs_log = os.path.abspath(os.path.join(value_datapath, './imgs_log'))
        conObj.set(userName, 'imgs_log', value_imgs_log)
        conObj.write(open('ADASet.ini', 'w'))

    def userExiste(self, userName, option):
        conObj.read(iniPath)
        try:
            value = conObj.get(userName, option)
        except ConfigParser.NoSectionError:
            self.creatConfig(userName)
        except ConfigParser.NoOptionError:
            self.creatConfig(userName)
        # print value_Emballer_logs
        value = conObj.get(userName, option)
        return value

    def getAll(self,userName):
        conObj.read(iniPath)
        path_log_emballer = self.confReadOrAdd(userName, 'Emballer_logs')
        imgs_log=self.confReadOrAdd(userName, 'imgs_log')
        datapath = self.confReadOrAdd(userName, 'datapath')
        logs_backup=self.confReadOrAdd(userName, 'logs_backup')
        return path_log_emballer, logs_backup, imgs_log, datapath
        
        


