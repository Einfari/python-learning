#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: fib.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 21:58:41


def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        yield b
        b, a = a + b, b
        n = n + 1

    return 'done'

fib(4)
