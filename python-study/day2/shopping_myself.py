# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

list_of_product = [["IphoneX", 8999], ["Apple Air", 3088], ["MacBook Air", 5999], ["MacBookPro", 128000],
                   ["Iphone6", 4999]]
list_of_shopping = []
money_of_guest = input("请输入您的预存款：")
if money_of_guest.isdigit():
    money_of_guest = int(money_of_guest)
    while True:

        print("\n商店产品列表如下\n")

        for l in list_of_product:
            print(list_of_product.index(l), l)

        num_product = input("请输入您需要购买商品的序号：")

        if num_product.isdigit():
            num_product = int(num_product)

            if money_of_guest < list_of_product[num_product][1]:
                print("您的余额不足以购买此商品，请选择其他商品或输入q退出")
            else:
                print("已将{name_of_product}加入您的购物车".format(name_of_product=list_of_product[num_product][0]))
                money_of_guest = money_of_guest - list_of_product[num_product][1]
                print("您的余额还有{b}".format(b=money_of_guest), "元")
                list_of_shopping.append(list_of_product[num_product])
        elif num_product == "q":
            print("\n您的购物清单如下：\n")
            for i in list_of_shopping:
                print(i)
            print("您的余额还有{b}".format(b=money_of_guest), "元,欢迎下次再来！")
            exit()
else:
    print("请输入正确的金额")
