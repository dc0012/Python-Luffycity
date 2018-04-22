# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]


print(sum([x["price"] for x in goods]))

