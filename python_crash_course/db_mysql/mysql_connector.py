# -*- coding: utf-8 -*-
"""
@author: 东风
@file: mysql_connector.py
@time: 2019/12/11 18:22
"""

# https://blog.csdn.net/weixin_43998473/article/details/86286299

import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="runoob_db"
)
# print(mydb)

mycursor = mydb.cursor()

# 创建数据库
# mycursor = mydb.cursor()
# mycursor.execute("create database runoob_db")

# 查看所有数据库
# mycursor = mydb.cursor()
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# 创建数据表
# mycursor = mydb.cursor()
# mycursor.execute("create table sites (name varchar(255), url varchar(255))")

# 查看数据表
# mycursor = mydb.cursor()
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# 创建主键
# mycursor = mydb.cursor()
# mycursor.execute("alter table sites add column id int auto_increment primary key")
# 或直接在建表是添加主键
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

# 插入数据
# mycursor = mydb.cursor()
# sql = "insert into sites (name, url) values (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "记录插入成功")
# mycursor.close()
# mydb.close()

# 批量插入
"""mycursor = mydb.cursor()
sql = "insert into sites (name, url) values (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taotao', 'https://www.taotao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "记录插入成功")
mycursor.close()
mydb.commit()
"""
# 获取记录ID
"""mycursor = mydb.cursor()
sql = "insert into sites (name, url) values (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
mycursor.execute(sql, val)
mydb.commit()
print("1 条记录已插入，ID：", mycursor.lastrowid)
mycursor.close()
mydb.close()
"""

# 查询数据
"""
mycursor = mydb.cursor()
mycursor.execute("select * from sites")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.close()
mydb.close
"""

# 读取指定字段
"""
mycursor = mydb.cursor()
mycursor.execute("select name, url from sites")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.close()
mydb.close()
"""

# 只读取一条记录：fetchone()
# mycursor.execute("select * from sites")
# myresult = mycursor.fetchone()
# print(myresult)
# mydb.close()

# where 条件语句
# sql = "select * from sites where name = 'RUNOOB'"

# 通配符%
# sql = "select * from sites where url like '%oo%'"
# mycursor.execute(sql)
# for x in mycursor:
#     print(x)

# 防止SQL注入攻击，使用%s占位符转义查询条件
# sql = "select * from sites where name = %s"
# na = ("RUNOOB", )
# mycursor.execute(sql, na)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# 排序
# sql = "select * from sites order by name"

# 降序
# sql = "select * from sites order by name desc"

# 读取前3条记录
# sql = "select * from sites limit 3"

# 从第二条开始读取前3条记录
# sql = "select * from sites limit 3 offset 1"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# 删除记录
# sql = "delete from sites where name = 'stackoverflow'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, " 条记录删除")

# 防止SQL注入，使用%s占位符转义删除语句的条件
# sql = "delete from sites where name = %s"
# na = ("RUNOOB", )
# mycursor.execute(sql, na)
# mydb.commit()
# print(mycursor.rowcount, " 条记录删除")

# 更新数据
# sql = "update sites set name = 'ZH' where name='Zhihu'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, " 条记录被修改")

# 防止SQL注入，使用%s占位符
sql = "update sites set name = %s where name = %s"
val = ('GG', 'Google')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")


