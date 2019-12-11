# -*- coding: utf-8 -*-
"""
@author: 东风
@file: py_mysql.py
@time: 2019/12/11 18:22
"""

# https://www.cnblogs.com/m0488/p/9442125.html
import pymysql

conn = pymysql.connect(user='root', password='', database='test', charset='utf8')
cursor = conn.cursor()

# 不带条件查询
# query = ('select user_id, user_name, pay_amount from t_count limit 10')
# cursor.execute(query)
# for (user_id, user_name) in cursor:
#     print(user_id, user_name)
# cursor.close()
# conn.close()


# 带条件查询
# 不论是什么数据类型，占位符都用%s
query = ('select user_id, user_name,pay_amount from t_count where pay_amount > %s limit 10')
cursor.execute(query, (100))
for (user_id, user_name, pay_amount) in cursor:
    print(user_id, user_name, pay_amount)
cursor.close()
conn.close()

