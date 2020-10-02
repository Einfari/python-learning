#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: is_palindrome.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 11:11:42


def is_palindrome(n):
    str_n = str(n)
    return [str_n for i in range(len(str_n)) if str_n[i] == str_n[-i - 1]]

print(is_palindrome(12345))
