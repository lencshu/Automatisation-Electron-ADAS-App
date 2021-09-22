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

    def rename(self,Id_database,file_path):
        Id_database = str(Id_database)
        if file_path.find('_context') == -1:
            newName = Id_database+'.png'
        else:
            newName = Id_database+'_context.png'
        new_path = os.path.split(file_path)[0]+'\\'+newName
        # new_path = os.path.join(os.path.abspath(new_path))
        # file_path=os.path.join(os.path.abspath(file_path))
        if not os.path.exists(new_path) and os.path.exists(file_path):
            os.rename(file_path,new_path)
            print "Image renamed", new_path
        elif not os.path.exists(file_path):
            print "Image file not existe: ",file_path
        return new_path

    def compresser(self,file_path):
        file_path = "\""+file_path+"\""
        args = " --force --verbose --quality=45-85 --ext=.png"
        pn = subprocess.Popen("pngquant.exe " + file_path + args, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
        pn.wait()
        (error, out) = pn.communicate()
        if str(error):
            print "Error : " + error
        if str(out):
            # print "Image Quantized: ",file_path
            print "input : " + str(out)

