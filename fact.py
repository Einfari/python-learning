#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: fact.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 17:27:38

# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

num = int(input('input a number plz:'))
print(fact(num));
