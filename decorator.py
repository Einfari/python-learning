#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: decorator.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 11:44:56

def log(exectue = 'call'):
    def decorator(func):
        def wrapper(*args, **kv):
            print('begin %s' %exectue)
            return func(*args, **kv)
        print('end %s' %exectue)
        return wrapper
    return decorator

@log

def f():
    pass

f()
