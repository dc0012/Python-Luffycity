# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

product_list = [
    ("Iphone", 5800),
    ("Mac Pro", 9800),
    ("Bike", 800),
    ("Watch", 10600),
    ("Coffee", 31),
    ("Alex Python", 120),
]
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salayr = int(salary)
    while True:
        for index, item in enumerate(product_list):
            # print(product_list.index(item), item)
            print(index, item)
        user_chioce = input("选择要买什么？>>>")
        if user_chioce.isdigit():
            user_chioce = int(user_chioce)
            if user_chioce < len(product_list) and user_chioce >=0:
                p_item = product_list[user_chioce]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]

                    print("Added %s into shopping cart,your current account is %s"%())

        elif user_chioce == "q":
            print("exit.....")
        else:
            print("")


