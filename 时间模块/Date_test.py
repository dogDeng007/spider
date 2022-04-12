# -!- coding: utf-8 -!-

import pandas as pd

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据

# 读取数据
rcv_data = pd.read_excel('全国高校数据.xlsx')

# 抽样展示5条数据
print(rcv_data.sample(5))

