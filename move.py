#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: move.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 18:01:51


def move(num, a, b, c):
    if num == 1:
        print(a, '-->', c)
        return

    move(num-1, a, c, b)
    print(a, '-->', c)
    move(num-1, b, a, c)

move(3, 'A', 'B', 'C')
