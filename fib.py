#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: fib.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-11 21:58:41

#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: fib.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2020-10-02 15:38:07

def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


# f = fib(5)

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

for x in fib(10):
    print(x)