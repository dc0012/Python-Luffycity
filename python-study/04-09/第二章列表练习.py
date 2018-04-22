# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

# 现有商品列表如下:
#     products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]
#     需打印出这样的格式：
#
#     ---------商品列表----------
#     0. Iphone8    6888
#     1. MacPro    14800
#     2. 小米6    2499
#     3. Coffee    31
#     4. Book    80
#     5. Nike Shoes    799

products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

print("---------商品列表---------")
for i in products:
    # print(products.index(i), ".", i[0], "    ", i[1])  还是用下面的表示方法更好
    print("%d.%s    %d" % (products.index(i), i[0], i[1]))

print("\n---------商品列表---------")
for i, p in enumerate(products):
    print(i, p[0], p[1])






