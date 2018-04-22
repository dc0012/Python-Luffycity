# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

# 递归练习题
menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': []},
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
        ]
    }
]
# 深度查询
# 1. 打印所有的节点
# 2. 输入一个节点名字，沙河， 你要遍历找，找到了，就打印它，并返回true,


def func1(x):
    for i in x:
        print()
        if i:
            func1(i)
        else:
            break


func1(menus)


