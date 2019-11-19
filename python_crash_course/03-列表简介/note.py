# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:28:55 2019

@author: p_bhcui
"""

def fs():
	print("*" * 40)

# 3.1 列表是什么
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-1].title())

fs()
message = "My first bicycles was a " + bicycles[0].title() + "."
print(message)

# 动手试一试
fs()
names = ['cuibinghua', 'dongfeng', 'huazi', 'shujuhui']
print(names[0])
print(names[1])
print(names[2])
print(names[3])


# 3.2 修改、添加和删除元素
fs()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

fs()
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

fs()
motorcycles.insert(0, 'ducati')
print(motorcycles)

fs()
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

fs()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

fs()
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + '.')

fs()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

fs()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

fs()

# 3.3 组织列表



# 3.4 使用列表时避免索引错误

"""
1、列表是什么以及如何使用其中元素
2、如何定义列表以及如何增删元素
3、如何对列表进行永久性排序，以及如何为展示列表而进行临时排序
4、如何确定列表的长度，以及在使用列表时如何避免索引错误

"""