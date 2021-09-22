#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$

import os
import shutil

def emballer(path,destipath):
    global filecopied
    global errorfile
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            nomDir=file_path.split('\\')[-1]
            if nomDir.find('log_')==0:
                cpfile_path=destipath+nomDir
                if not os.path.exists(cpfile_path):
                    shutil.copytree(file_path,cpfile_path)
                    filecopied+=1
                    print filecopied," files copied"
                else :
                    print "Error, direcoiry already existe:", file_path,", renamed"
                    # raw_input("Rename?")
                    cpfile_path = cpfile_path+str(errorfile)+'ms'
                    shutil.copytree(file_path, cpfile_path)
                    filecopied += 1
                    errorfile+=1
                    
            else:
                emballer(file_path,destipath)

filecopied=0
errorfile=1
destipath=os.getcwd()+"\\Emballer_logs\\"
emballer(os.getcwd(),destipath)
