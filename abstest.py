#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: abstest.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 16:13:23


def my_abs(num):
    if not isinstance (num, (int, float)):
        raise TypeError('bad operation type')
    if num > 0:
        return num
    else:
        return -num
