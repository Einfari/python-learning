#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: func.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 17:03:21


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#默认参数
def power_1(x , n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#伪可变参数
def calc(numbers):
    sum  = 0
    for num in numbers:
        sum = sum + num
    return sum

calc([1,2,3,4])
calc((1,2,3,4))

#可变参数
def calc_1(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

calc_1(1,2,3)

#如果已经有一个list或者tuple
nums = [1,2,3]
calc_1(*nums)

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict。
#关键字参数
def person(name, age, **kw):
    print(name, age, kw)

person('Lipsum', 24, gender='M', city='SH')

extra = {'city': 'SH', 'job': 'CS'}
person('Lipsum', 24, **extra)


#命名关键字参数，如果要限制关键字参数的名字，就可以用命名关键字参数
def person_1(name, age, *, city, job):
    print(name, age, city, job)

