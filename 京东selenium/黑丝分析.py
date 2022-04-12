import pandas as pd

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
rcv_data = pd.read_csv(open('./jd黑丝.csv'))

# 删除重复记录
rcv_data = rcv_data.drop_duplicates()
# 删除缺失值
rcv_data = rcv_data.dropna()

# 抽样展示5条数据
print(rcv_data.sample(5))




