# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc


age_of_gril = 28
count = 0
while True:
    if count == 3:
        break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_gril:
        print()
