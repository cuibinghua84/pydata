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
# mycursor = mydb.cursor()
# sql = "insert into sites (name, url) values (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taotao', 'https://www.taotao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "记录插入成功")
# mycursor.close()
# mydb.commit()

# 获取记录ID

