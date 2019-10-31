# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 3.2-修改-添加和删除元素.py
@time: 2019/10/30 10:57
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 3.2.1 修改元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 添加元素
# 1 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 2 在列表中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.2.3 从列表中删除元素
# 1 使用del删除元素
del motorcycles[0]
print(motorcycles)

# 2 使用pop删除元素
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 3 弹出列表中任何位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(first_owned)
print(motorcycles)

# 4 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


"""
列表的操作方法
motorcycles.append()
motorcycles.count()
motorcycles.copy()
motorcycles.clear()
motorcycles.extend()
motorcycles.index()
motorcycles.insert()
motorcycles.pop()
motorcycles.remove()
motorcycles.reverse()
motorcycles.sort()
"""
