#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: str2float.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 10:26:43


def str2num(x):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, '.':'.'}[x]

print(list(map(str2num, '123.456')))
