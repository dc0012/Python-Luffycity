# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

list_1 = [1, 4, 5, 7, 3, 6, 7, 9]
list_1 = set(list_1)
print(list_1, type(list_1))

list_2 = set([2, 6, 0, 66, 22, 8, 4])
print(list_1, list_2)

print(list_1.intersection(list_2))  # 交集

print(list_1.union(list_2))  # 并集，去重

print(list_1.difference(list_2))  # 差集，in list_1 but not in list_2
print(list_2.difference(list_1))  # 差集，in list_2 but not in list_1

list_3 = set([1, 3, 7])
print(list_3.issubset(list_1))  # 子集
print(list_1.issuperset(list_3))  # 父集

print(list_1.symmetric_difference(list_2))  # 对称差集，将两个里面互相都没有的作为一个集合

print('--------------------')


list_4 = set([5, 6, 8])
print(list_3.isdisjoint(list_4))  # Return True if two sets have a null intersection.

print(list_1 & list_2)  # 交集
print(list_2 | list_1)  # 并集
print(list_1 - list_2)  # in list_1 but not in list_2
print(list_1 ^ list_2)  # 对称差集，

list_1.add(999)
list_1.update([888, 777, 555])
print(list_1)

