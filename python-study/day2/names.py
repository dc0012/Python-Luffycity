# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

names = ["ZhangYang", "Guyun", "XiangPeng", "XuLiangchen"]

print(names)

print(names[0], names[2])

print(names[1:3])  # 顾头不顾尾，包含1，不包含3，切片

print(names[-1])   # 从末尾往前数第一个，-2表示末尾往前数第二个

print(names[-3:])

print(names[:3])

names.append("LeiHaidong")  # 插到最后

names.insert(1, "ChenRonghua")  # 插到指定位置

print(names)

names[2] = "XieDi"  #更改

print(names[2])

# 删除
# names.remove("ChenRonghua")

# del names[1]

names.pop()  # 不输入角标的话，默认删除最后一个

print(names)

print(names.index("XieDi"))  # 查找、索引
print(names[names.index("XieDi")])

print(names.count("ChenRonghua"))  #

# names.clear()  # 清空列表
names.reverse()  # 反转列表
names.sort()  # 排序
names2 = [1, 2, 3, 4]
names.extend(names2)  # 将names2扩展到names中，names2还存在。
del names2
print(names)



names[2] = "向鹏"

print(names)

names = ['ChenRonghua', 'XiangPeng', '向鹏', ["Dong", "Chao"], 'XuLiangchen', 'ZhangYang', 1, 2, 3, 4]

names2 = names.copy()

print(names)
print(names2)

names[3][0] = "DONG"
names[0] = "陈荣华"

print(names)
print(names2)

import copy

# names2 = copy.copy(names)  # 依然是浅copy
names2 = copy.deepcopy(names)  # 深copy,一般不大量使用,开辟独立内存来存储。

# range(1,10,2)
print(">>>>>>>>>", names[0:-1:2])

print(">>>>>>>>>", names[::2])

for i in names:
    print("--------------", i)




