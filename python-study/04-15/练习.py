# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

a = "hello World"

print(a.capitalize())
print(a.casefold())  # 全变小写
print(a.lower())
print(a.upper())
print(a.center(20, "-"))
print(a.count("o", 0, 7))
print(a.isalnum())    # 判断是不是同时包含了字母和数字
print(a.endswith("rld"))
print(a.startswith("hel"))
print(a.find("l"))
print(a.index("lo"))
print(a.isalpha())    # 判断是不是仅仅包含了字母
print(a.isdigit())
print(a.isdecimal())  # 判断是不是小数
print(a.isprintable())  # 判断是不是可打印输出的
print(a.isspace())  # 判断是不是空格
print("-".join(a))
print(a.replace("hello", "dark", 1))
print(a.title())
print(a.swapcase())
