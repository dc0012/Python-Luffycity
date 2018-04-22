# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

# names里有3个2，请返回第2个2的索引值。不要人肉数，要动态找(提示，找到第一个2的位置，在此基础上再找第2个)

names = [1, 9, 3, 4, 2, 1, 34, 5, 2, 6, 6, 2, 5443, 5]

new_list = names[names.index(2)+1:]

new_index = new_list.index(2)

second_index = names.index(2) + new_index + 1
print("第二个2的索引是", second_index)


