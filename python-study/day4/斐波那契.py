# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))

