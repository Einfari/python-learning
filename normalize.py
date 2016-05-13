#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: normalize.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 10:03:52


def normalize(name):
    return str(name[0].upper()) + str(name[1:].lower())

print(normalize('aBcdeF'))
