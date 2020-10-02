#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: expection.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 16:52:40


import logging

def foo(n):
    return 10 / int(n)

def main():
    n= input('input a num plz:')
    try:
        print(foo(n))
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()

