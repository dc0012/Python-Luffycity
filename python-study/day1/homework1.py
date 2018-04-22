# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

username_of_login = input("Username:")
password_of_login = input("Password:")
count = 0

for lockuser in open("/home/dc/lock_account.txt"):
    if username_of_login == lockuser:
        print("Sorry,This accountment was locked,Please try later.")
        break

for account in open("/home/dc/account.txt"):
    if username_of_login



"""  
for username in open("/home/dc/username.txt"):
    if username_of_login == username:
        for password in open("/homne/dc/password.txt"):
            if password_of_login == password:
                print("Welcome user ", username_of_login,"login.")
            else:
                print("Invid username or password,Please try again.")
                count +=1
存在bug，有可能第二个用户名与第一个密码对应上了，就判断登录了
"""

