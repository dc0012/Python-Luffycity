# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc0012

import sys

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

name_input = input("请输入您的用户名:")
passwd_input = input("密码:")

shopping_list = []
shopping_record_list = []

# ---------------------------读取用户信息,包括用户名,密码,总金额,上次消费后余额数----------------------------
with open("account", "r", encoding="utf-8") as account_file:
    i = account_file.readline()    # 将account中一行的数据以字符串形式传给i
    name, passwd, money, balance = i.split()   # 用空格分割i,分别取到之前记录的用户名,密码,总金额,上次消费余额.
    money = int(money)
    balance = int(balance)  # 将钱数转换成整形,方便后面比较或运算.

# ---------------------------判断用户登录-------------------------------------------	
if name_input == name and passwd_input == passwd:      # 判断用户名密码是否正确
    if money == 0:      # 判断是不是第一次登陆
        print("欢迎%s来到购物中心..." % name_input)

        while True:
            money = input("请输入您的购物现金数:")
            if money.isdigit():   # 判断输入格式
                money = int(money)
                balance = money   # 初始化余额与总额相等
                break
            else:
                print("请输入正确的数字...")
                continue

    elif money == balance:  # 判断上次已经登陆,且未购买任何商品就退出的用户
        print("欢迎%s再次来到购物中心,您上次未购买任何商品,余额还剩\033[1;35m%d\033[0m元." % (name_input, balance))
    else:  # 判断为上次登陆,且有消费记录的用户
        print("欢迎%s再次来到购物中心,您的余额还剩\033[1;35m%d元\033[0m." % (name_input, balance))

# ------------------------------查询上次购买记录-----------------------------------
        while True:
            query = input("是否查询您上次的购买记录(y或者n)")
            if query == "y":
                expense = money - balance    # 计算上次消费金额

                with open("purchase_record", "r", encoding="utf-8") as f:
                    shopping_record_list = eval(f.read())    # 读取之前的消费记录,使用eval()转换字符串为代码.
                    print("\033[1;36m-----您之前所购买的商品如下-----\033[0m")

                    for i in range(len(shopping_record_list)):  # 输出之前的消费列表
                        print("序号:%d  name:%s  price:%d" %
                              (i, shopping_record_list[i]["name"], shopping_record_list[i]["price"]))
                    print("您总共购买了\033[1;35m %d \033[0m件商品,消费\033[1;35m %d元 \033[0m,"   # 输出之前的消费金额和余额
                          "余额:\033[1;35m %d元 \033[0m" % (len(shopping_record_list), expense, balance))
                    break
            elif query == "n":
                break
            else:
                print("输入错误,请输入y或者n选择")
else:
    print("\033[1;35m 用户名密码错误...程序退出\033[0m")
    sys.exit()

balance_last = balance  # 初始化上次消费后的余额,方便之后计算本次消费总金额.

# ---------------------------------购物流程---------------------------------
while True:
    print("\033[1;36m------商品列表如下:------\033[0m")

    for i in range(len(goods)):  # 打印商品列表
        print("序号:%d  name:%s  price:%d" % (i, goods[i]["name"], goods[i]["price"]))

    user_choice = input("\033[1;34m请输入要购买的商品序号\033[0m(退出请输入\033[1;32mq\033[0m):")

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 0 <= user_choice < len(goods):  # 判断用户输入商品是否存在
            if goods[user_choice]["price"] <= balance:   # 判断用户余额是否足够购买
                balance -= goods[user_choice]["price"]
                shopping_list.append(goods[user_choice])  # 将用户购买的商品添加到本次购物列表
                print("感谢您购买\033[1;35m %s \033[0m,您的余额还剩\033[1;35m %d元 \033[0m."
                      % (goods[user_choice]["name"], balance))
            else:
                print("sorry,您的余额还有\033[1;35m %d元 \033[0m,不足以以购买此商品,请重新选择" % balance)
        else:
            print("您选择的商品不存在,请重新选择")
        continue
    elif user_choice == "q":
        if not shopping_list:    # 判断用户本次是否购买了任意商品
            print("您本次未购买商品,余额还剩:\033[1;35m %d元 \033[0m" % balance)
            break
        else:
            expense = balance_last - balance   # 计算本次消费总额
            print("\033[1;36m-----您所购买的商品如下-----\033[0m")

            for i in range(len(shopping_list)):   # 打印本次消费记录
                print("序号:%d  name:%s  price:%d" % (i, shopping_list[i]["name"], shopping_list[i]["price"]))
            print("您总共购买了\033[1;35m %d \033[0m件商品,消费\033[1;35m %d元 \033[0m,"
                  "余额:\033[1;35m %d元 \033[0m" % (len(shopping_list), expense, balance))

# ------------------------------------------记录本次购买后的信息,写入文档--------------------------------				  
            with open("purchase_record", "w", encoding="utf-8") as f_purchase:
                with open("account", "w", encoding="utf-8") as f_account:
                    shopping_record_list.extend(shopping_list)    # 将本次消费记录添加到之前的消费记录
                    f_purchase.write(str(shopping_record_list))   # 将所有的(包括之前)消费记录以字符串格式写入文件
                    account = "%s %s %d %d" % (name_input, passwd_input, money, balance)
                    # 以空格分割用户名,密码,金钱总数,本次消费余额,以字符串格式赋给变量account
                    f_account.write(account)  # 将account写入文件,更新用户的余额
            break
    else:
        print("请输入正确的选项或命令....")   # 判断用户输入是否符合要求,并让用户重新输入.
        continue



