#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$

"""
methode:

image.compresser(self,file_path)
image.rename(self,Id_database,file_path)
"""


import os
import subprocess

class image(object):
    """docstring for image"""
    def __init__(self):
        super(image, self).__init__()

    def rename_old(self,Id_database,file_path):
        nomDir=file_path.split('\\')[-1]
        new_nomDir=str(Id_database)+'_'+nomDir
        new_path=os.path.split(file_path)[0]+'\\'+new_nomDir
        # new_path = os.path.join(os.path.abspath(new_path))
        # file_path=os.path.join(os.path.abspath(file_path))
        if not os.path.exists(new_path) and os.path.exists(file_path):
            os.rename(file_path,new_path)
            print "Image renamed", new_path
        elif not os.path.exists(file_path):
            print "Image file not existe: ",file_path
        return new_path

    def rename_backup(self, Id_database, file_path):
        Id_database = str(Id_database)
        if file_path.find('_context') == -1:
            newName = Id_database+'.png'
        else:
            newName = Id_database+'_context.png'
        new_path = os.path.split(file_path)[0]+'\\'+newName
        # new_path = os.path.join(os.path.abspath(new_path))
        # file_path=os.path.join(os.path.abspath(file_path))
        if not os.path.exists(new_path) and os.path.exists(file_path):
            os.rename(file_path, new_path)
            print "Image renamed", new_path
        elif not os.path.exists(file_path):
            print "Image file not existe: ", file_path
        return new_path


    def errorWrite(self, path_errorFile, errorData):
        with open(path_errorFile, 'a') as errorFile:
            errorFile.writelines(errorData)

    def rename(self, Id_database, file_path, path_errorFile):
        Id_database = str(Id_database)
        if file_path.find('_context') == -1:
            newName = Id_database+'.png'
        else:
            if file_path.find('_context_0') != -1:
                newName = Id_database+'_context_0.png'
            elif file_path.find('_context_1') != -1:
                newName = Id_database+'_context_1.png'
            else:
                newName = Id_database+'_context.png'
            # newName = Id_database+'_context.png'
        new_path = os.path.split(file_path)[0]+'\\'+newName

        os.rename(file_path, new_path)
        # new_path = os.path.join(os.path.abspath(new_path))
        # file_path=os.path.join(os.path.abspath(file_path))


        # if not os.path.exists(file_path):
        #     print "Not exist image file: ", file_path
            # raw_input()
            # errorData = "Not exist image file: "+ file_path
            # self.errorWrite(path_errorFile,errorData)
            
        # os.rename(file_path,new_path)
        # if not os.path.exists(new_path) and os.path.exists(file_path):
        #     os.rename(file_path,new_path)
        #     print "Image renamed", new_path
        # elif not os.path.exists(file_path):
        #     print "Image file not existe: ",file_path
        return new_path

    def compresser(self,file_path):
        file_path = "\""+file_path+"\""
        args = " --force --verbose --quality=45-85 --ext=.png"
        try:
            pn = subprocess.Popen("pngquant.exe " + file_path + args, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
            pn.wait()
            (error, out) = pn.communicate()
            if str(error):
                print "Error : " + error
            if str(out):
                print "Image compressed: ", file_path
                # print "Image compressed"
                # print "input : " + str(out)
            # print "compression ignored"
            
        except :
            print '==> Image compressing failed, skip to the next step <=='
        


