# -*- coding: utf-8 -*-
"""
@author: 东风
@file: pandas_mysql.py
@time: 2019/12/28 11:06
"""

import pymysql
import pandas as pd
import time
from sqlalchemy import create_engine

# 性能比较好
start = time.time()
con = pymysql.connect(host="127.0.0.1", user="root", password="abc123", db="db_kid_story")
data_sql = pd.read_sql(
    "select user_id,amt,create_time from t_user_bean_tran_detail where status=2 and create_time>=current_date", con)
data_sql.to_csv("D:/data/t_user_bean_tran_detail.csv")
end = time.time()
print(end - start)

# start = time.time()
# con = create_engine("mysql+pymysql://root:abc123@localhost:3306/db_kid_story", echo=True)
# data = pd.read_sql_table("t_user_bean_tran_detail", con)
# data.to_csv("D:/data/t_user_bean_tran_detail1.csv")
# end = time.time()
# print(end - start)
