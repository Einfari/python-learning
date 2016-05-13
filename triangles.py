#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: triangles.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 22:08:09

def triangles(n):
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
