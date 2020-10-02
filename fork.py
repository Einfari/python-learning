#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: fork.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-16 11:01:29

import os

print('Process %s start...' %(os.getpid()))

pid = os.fork()

if pid == 0:
    print('I am child process %s and my parent process is %s' %(os.getpid(), os.getppid()))
else:
    print('I am father process %s and i create a child process %s' %(os.getppid(),pid))
