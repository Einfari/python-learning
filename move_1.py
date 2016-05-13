#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: move_1.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 18:25:12

def move(n, source, bridge, destination):
    if n == 1:
        print(source, '-->', destination)
    else:
        move(n-1, source, destination, bridge)
        move(1, source, bridge, destination)
        move(n-1, bridge, source, destination)

num = ('A','B','C')
move(3,*num)
