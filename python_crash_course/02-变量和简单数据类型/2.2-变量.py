# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 2.2-变量.py
@time: 2019/10/30 10:55
"""
import keyword

message = "Hello Python world!"
print(message)
message = "Hello Python Crash world!"
print(message)

"""
变量的命名规则
1、变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头
2、变量名不能包含空格，但可使用下划线来分隔其中的单词
3、不要将Python关键字和函数名作为变量名，即不要使用Python保留用于特殊用途的单词
4、变量名应既简短又具有描述性
5、慎用小写字母l和大写字母O，因为他们可能被人错看成数字1和0
"""
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

# 避免命名错误：使用前忘记了给它赋值；输入变量名时拼写不不正确
