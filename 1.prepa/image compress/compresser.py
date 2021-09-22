#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$


import image
import os

img=image.image()

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filetype = os.path.splitext(file)[1]
        if filetype == '.png':
            path_img = root+'\\'+file
            print path_img
            img.compresser(path_img)

