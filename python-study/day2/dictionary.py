# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author:dc

# key-value 数据类型

info = {
    'stu1101': 'aaaa',
    'stu1102': 'bbbb',
    'stu1103': 'cccc',
    'stu1104': 'dddd',

}

print(info)
print(info['stu1101'])

info['stu1101'] = '学生01'
info['stu1105'] = 'eeee'

del info['stu1103']
info.pop('stu1104')
# info.popitem()  随机删除
print(info)

print(info.get('stu1106'))   # 直接使用 info【‘stu1106’】，如果stu1106不存在，程序会直接报错

print('stu1106' in info)   # info.has_key('1103') in py2.x

b = {
    'stu1111': 'ffff',
    1: 2,
    3: 4
}
info.update(b)       # 将两个字典进行了合并
print(info)

print(info.items())  # 将字典转换成了列表，key为第一个值

c = dict.fromkeys([6, 7, 8], [1, {'name': 'dc'}, 4])  # 初始化一个字典，但是将所有的value指向了一个test，更改其中一个test，其他key的value也都会被更改
print(c)

c[7][1]['name'] = 'dong'
print(c)

for i in info:
    print(i, info[i])    # 建议使用这种

for k, v in info.items():  # 多了一个将字典转换为列表元祖的操作，数据量大的话时间会很长。
    print('>>>>', k, v)

