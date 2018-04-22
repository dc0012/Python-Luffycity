# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

print('''
# 1. 列表['alex','egon','yuan','wusir','666']（编程）
# - 1.把666替换成999
# - 2.获取"yuan"索引
# - 3.假设不知道前面有几个元素，分片得到最后的三个元素
''')

a = ['alex', 'egon', 'yuan', 'wusir', '666']
print("a=", a)

a[-1] = "999"
print(a)


print("yuan的索引:", a.index("yuan"))

print(a[-3:])

print(" 将字符串“www.luffycity.com”给拆分成列表：li=['www','luffycity','com']")
b = "www.luffycity.com"
print("b=", b)
c = b.split(".")
print("c=", c)

print("计算1+2+3...+98+99+100")
a = 0
for i in range(1, 101):
    a += i
print(a)


