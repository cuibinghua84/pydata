# -*- coding: utf-8 -*-
# 作者      : p_bhcui
# 创建时间  : 2019/12/30 15:14
# 文件      : db_con.py
# IDE       : PyCharm

from pymysql import connect
from sqlalchemy import create_engine

con_kid_story = connect(host='127.0.0.1', user='root', password='abc123', db='kidbook_new')
print(con_kid_story)

con_kp_data = create_engine('mysql+pymysql://root:abc123@localhost:3306/kp_data')
print(con_kp_data)