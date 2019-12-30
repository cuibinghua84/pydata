# -*- coding: utf-8 -*-
# 作者      : p_bhcui
# 创建时间  : 2019/12/30 10:55
# 文件      : pandas_test.py
# IDE       : PyCharm

import pymysql
import pandas as pd
from db_con import con_kid_story, con_kp_data

data_sql = pd.read_sql(
    """SELECT 
            date_sub(curdate(),interval 1 day) as statis_day,
            client_platform AS software_platform, 
            client_version AS software_version, 
            client_channel AS channel, goods_id, 
            goods_info,	
            trade_type AS trade_type,	
            payment_mode AS payment_mode,	
            sum( total_fee / 100 ) AS total_income,	
            count(*) AS total_cnt,	
            count( DISTINCT uin ) AS total_user 
        FROM trade_order 
        WHERE payment_info <> 'vc' 
        and DATE_FORMAT(start_time,'%Y-%m-%d') = date_sub(curdate(),interval 1 day)
        group by 
            client_platform,
            client_version,
            client_channel,
            goods_id,
            goods_info,
            trade_type,
            payment_mode
        """,
    con_kid_story)
# print(data_sql)
data_sql.to_sql('t_md_kidreader_income_sum', con_kp_data, index=False, if_exists='append')
