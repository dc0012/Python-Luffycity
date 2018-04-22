# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

import sys

print(sys.path) #打印环境变量

#print(sys.argv)
#print(sys.argv[2])

import os

cmd_res = os.system("df -h")  #仅执行命令，不保存结果
cmd_res = os.popen("df -h").read()  #必须用.read（）读取
print("------>",cmd_res)

os.mkdir("1111111")
os.rmdir("1111111")




