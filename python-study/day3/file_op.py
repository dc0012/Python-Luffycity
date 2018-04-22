# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

# data = open('yesterday', encoding='utf-8').read()

"""
f = open('yesterday', 'a', encoding='utf-8')  # 文件句柄  w模式会直接创建yesterday文件，覆盖原文件。

data = f.read()
data2 = f.read()

print(data)
print('-----------------data2----------------', data2)  # data2 并没有输出内容,由于指针移到了文件末尾。

f.write('\n我爱北京天安门')
f.write('\n天安门上太阳升')

f.close()

f = open('yesterday2', 'r', encoding='utf-8')

# for i in range(5):
#   print(f.readline())

# for line in f.readlines():
#     print(line.strip())

for index, line in enumerate(f.readlines()):
    if index == 9:
        print('--------------------------')
        continue
    print(line.strip())

f = open('yesterday2', 'r', encoding='utf-8')
count = 0
for line in f:     # 这种方法比readline（）的方法占用内存少，读一行，释放前一行的内存。
    if count == 9:
        print("-----------分割线-----------")
        count += 1
        continue
    print(line)
    count += 1
"""

f = open('yesterday2', 'r+', encoding='utf-8')   # r+以读和追加的模式打开file。
#  w+写读不常用，a+追加读写。rb以二进制格式读文件，网络传输使用二进制。wb二进制写模式

print(f.tell())  # .tell返回当前指针位置
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(10)
print(f.tell())

print(f.encoding)
print(f.flush())  #

# f.truncate(20)  从0开始截断20个字节

