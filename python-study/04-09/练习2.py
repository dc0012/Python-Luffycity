# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

names = ['-1', 'rain', ['oldboy', 'oldgirl'], 'jack', '珊珊', 'peiqi', 'Alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]

print(names)

count = 0
for i in names:
    if names.index(i) % 2 == 0:
        names[count] = "-1"
    print(count, names[count])
    count += 1
print(names)

