# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 2.3-字符串.py
@time: 2019/10/30 10:55
"""

# 字符串方法
name = "love the Python"
# print(help(name.rsplit))

print("*" * 40)
# 返回 str在name里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数
# count(sub[, start[, end]])
print(name.count('o', 0, 14))

# 返回一个长度和宽度居中的字符串，使用指定的填充字符填充(默认为空格)
# center(width, fillchar=' ', /)
print(name.center(20, '*'))

# 返回适合无大小写比较的字符串版本
print(name.casefold())

# 将字符串的第一个字符转换为大写
print(name.capitalize())

# 返回使用空格展开所有制表符的副本，默认的空格是8个字符
print("I\tlove\tPython".expandtabs())

# 判断是否以指定的字符结尾
# name.endswith()

# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# name.encode()

# name.format_map()

# 字符串的格式化
# name.format()

# 检测 str 是否包含在字符串中,如果beg和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# name.find()

# 跟find()方法一样，只不过如果str不在字符串中会报一个异常
# name.index()

# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# name.isalnum()

# 如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
# name.isalpha()

# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
# name.isdecimal()

# 如果字符串只包含数字则返回 True 否则返回 False..
# name.isdigit()

# 如果字符串是有效的Python标识符，则返回True，否则返回False
# name.isidentifier()

# 判断是否是小写
# name.islower()

# 如果字符串中只包含数字字符，则返回 True，否则返回 False
# name.isnumeric()

# 如果字符串可打印，则返回True，否则返回False
# name.isprintable()

# 如果字符串中只包含空格，则返回 True，否则返回 False.
# name.isspace()

# 如果字符串是标题化的(见 title())则返回 True，否则返回 False
# name.istitle()

# 判断是否是大写
# name.isupper()

# 如果字符串中的所有字符都是ASCII码，则返回True，否则返回False
# name.isascii()

# 连接字符（连接的是可迭代对象）
# name.join()

# 转换字符串中所有大写字符为小写.
# name.lower()

# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格
# name.ljust()

# 去除空格
# name.lstrip()

# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
# name.maketrans()

# 返回一个三元组，其中包含分隔符之前的部分，即分隔符本身，以及后面的部分
# name.partition()

# 替换指定的字符或字符串
# name.replace()

# 类似于 find()函数，不过是从右边开始查找
# name.rfind()

# 类似于 index()，不过是从右边开始
# name.rindex()

# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串/
# name.rjust()

# 使用指定的分隔符将字符串划分为三个部分
# name.rpartition()

# 返回字符串中的单词列表，使用sep作为分隔符字符串
# name.rsplit()

# 去除空格
# name.rstrip()

# 分割字符串，并将分割后的结果返回为一个list
# name.split()

# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符
# name.splitlines()

# 判断是否以指定的字符结尾/开始
# name.startswith()

# 去除空格
# name.strip()

# 将字符串中大写转换为小写，小写转换为大写
# name.swapcase()

# 返回"标题化"的字符串,就是说所有单词都是以大写开始
print(name.title())

# 根据str给出的表(包含256个字符)转换 string 的字符,要过滤掉的字符放到 deletechars 参数中
# name.translate()

# 转换字符串中的小写字母为大写
# name.upper()

# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
# name.zfill()
