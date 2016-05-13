#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: is_even.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 10:45:18

def is_even(s):
    return s % 2 == 0

print(list(filter(is_even,[1,2,3,4,5,6,7,8])))
