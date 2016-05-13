#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: hello.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 14:32:31

__author__ = 'Saturn'

import sys

def test():
    args = sys.argv
    if(len(args) == 1):
        print('Hello World')
    elif(len(args) == 2):
        print('Hello %s' %args[1])
    else:
        print('参数太多了')


if __name__ == '__main__':
    test()
