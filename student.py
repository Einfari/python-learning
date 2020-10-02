#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: student.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 14:51:48

class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def print_s(self):
        print(self.__name,self.__age)

if __name__ == '__main__':
    Lipsum = Student('Lipsum',24)
    Lipsum.print_s()
