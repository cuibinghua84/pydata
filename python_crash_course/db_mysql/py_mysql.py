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
# query = ('select user_id, user_name,pay_amount from t_count where pay_amount > %s limit 10')
# cursor.execute(query, (100))
# for (user_id, user_name, pay_amount) in cursor:
#     print(user_id, user_name, pay_amount)
# cursor.close()
# conn.close()

# 插入数据
# conn = pymysql.connect(user='root', password='', database='test', charset='utf8')
# cursor = conn.cursor()
# query = ('insert into t_count (user_id,user_name,pay_amount,pay_cnt,user_tel,max_time,column2) values (%s, %s, %s, %s, %s, %s, %s)')
# cursor.execute(query, (14104, '吴虞宝贝', 7.0, 3, 15170716685, '2017-02-17 12:24:36', '2020-11-07'))
# conn.commit()
# cursor.close()
# conn.close()

# 修改数据
# conn = pymysql.connect(user='root', password='', database='test', charset='utf8')
# cursor = conn.cursor()
# query = ('update t_count set user_name = %s where id= %s')
# cursor.execute(query, ('数据汇', 22))
# conn.commit()
# cursor.close()
# conn.close()

# 删除数据
conn = pymysql.connect(user='root', password='', database='test', charset='utf8')
cursor = conn.cursor()
query = ('delete from t_count where id=%s')
cursor.execute(query, 22)
conn.commit()
cursor.close()
conn.close()
