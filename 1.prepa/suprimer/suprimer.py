#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$

import os
import shutil

def sup(path):
    global fileremoved
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            nomDir=file_path.split('\\')[-1]
            if nomDir.find('log_')==0:
                shutil.rmtree(file_path)
                fileremoved+=1
                print fileremoved, " log files removed"
            else:
                sup(file_path)

fileremoved=0
sup(os.getcwd())
