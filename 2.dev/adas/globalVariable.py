#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 16:19:26
# @Author  : li@gliang.eu
# @Link    : https://gliang.eu
# @Version : $Id$


def _init():#初始化
    global global_dict
    global_dict = {}


def set_value(key,value):
# Set
    global_dict[key] = value


def get_value(key,defValue=None):
# 　　get
    try:
        return global_dict[key]
    except KeyError:
        return defValue