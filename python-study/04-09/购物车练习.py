# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

# 写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里， 最终用户输入q退出时，打印购物车里的商品列表

products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['Nike Shoes', 799]]

shopping_cart = []

count_shopping = 1

run_flag = True

while run_flag:
    print("---------商品列表---------")

    for i in products:
        # print(products.index(i), ".", i[0], "    ", i[1])  还是用下面的表示方法更好
        print("%d.%s    %d" % (products.index(i), i[0], i[1]))

    user_input = input("\n选择想要购买商品的序号,加入你的购物车,退出请直接输入'q':")

    if user_input == "q":  # 判断用户是否选择退出
        if not shopping_cart:  # 判断用户是否未购买任何商品
            print("\n未购买任何商品,购物结束.")
        else:
            print("\n您购物车里的商品如下:\n")
            for i in shopping_cart:      # 循环输出用户已购买的商品
                print("%d.%s   %d" % (count_shopping, i[0], i[1]))
                # 使用count_shopping计数用户购买的商品,从1开始计数更符合用户习惯.
                # 如果使用shopping_cart.index(i),会出现多次购买同一商品造成序号相同的bug
                count_shopping += 1
            print("\n------购物结束------")
        run_flag = False
    # else:
    #     num = int(user_input)
    #     shopping_cart.append(products[num])
    #     print("\n已将%s加入您的购物车\n" % products[num][0])
    elif user_input.isdigit():  # 判断输入的是不是数字
        user_input = int(user_input)
        if 0 <= user_input < len(products)-1:  # 判断选择的商品是否存在
            shopping_cart.append(products[user_input])
            print("\n已将%s加入您的购物车\n" % products[user_input][0])
        else:
            print("\n抱歉,您输入的商品序号不存在,请重新输入.")
    else:
        print("\n请输入正确的商品序号(数字)或使用命令'q'退出.\n")



