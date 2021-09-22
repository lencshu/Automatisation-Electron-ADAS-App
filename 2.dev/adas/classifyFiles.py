#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$

"""
methode:

files.classify(self,path_log_emballer,path_logs,path_images)
files.osWalk(self,dirname)
"""
import image
import os
import shutil
import time


im=image.image()

class files(object):
    """docstring for files"""
    def __init__(self):
        super(files, self).__init__()

    def dir_exist(self,dirname):
        if not os.path.exists(dirname):
             os.mkdir(dirname)
    def osWalk(self,dirname):
        for root, dirs, files in os.walk(dirname):
            for file in files:
                index = []
                filetype = os.path.splitext(file)[1].strip('.')
                index.append(filetype)
                index.append(root)
                index.append(file)
                index.append(root+'\\'+file)
                return index

    def classify(self,path_log_emballer,path_logs,path_images,indiceCompress):
        if os.path.exists(path_log_emballer):
           print "===Classifying and compressing all the log and image files==="
           self.dir_exist(path_logs)
           self.dir_exist(path_images)
           path_logs=path_logs+'\\' 
           path_images=path_images+'\\'
           path_logs_in_one=path_logs+'All_logs_in_one_'+str(time.time())+'.txt'
           file_logs_in_one=open(path_logs_in_one,'a')
           for root, dirs, files in os.walk(path_log_emballer):
               for file in files:
                   filetype=os.path.splitext(file)[1] 
                   if filetype == '.png':
                       image_path_abs=root+'\\'+file
                       if indiceCompress:
                           im.compresser(image_path_abs)
                       else:
                           print "compression ignored: ",image_path_abs
                       shutil.copy(image_path_abs,path_images)
                       os.remove(image_path_abs)
                       print file,' moved'
                   elif filetype == '.txt':
                       file_path_abs=root+'\\'+file
                       # print file_path_abs
                       for line in open(file_path_abs):
                           file_logs_in_one.writelines(line)
                       file_logs_in_one.write('\n')
                       if os.path.exists(file_path_abs):
                           os.remove(file_path_abs)
                           print file_path_abs,' removed'
           file_logs_in_one.close()
           print path_logs_in_one
           shutil.rmtree(path_log_emballer)
        else:
            print "Error: No directory named \"Emballer_logs\""








