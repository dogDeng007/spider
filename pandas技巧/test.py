import pandas as pd
import numpy as np

# Series
score = {'语文': 99, '数学': 99, '英文': 99, '物理':88, '化学':88}
pd_data = pd.Series(data=score)
print(pd_data)

'''
语文    99
数学    99
英文    99
物理    88
化学    88
dtype: int64
'''

# Series-DataFram
pd_data = pd_data.reset_index()
pd_data.columns = ['科目', '分数']
print(pd_data)
'''
   科目  分数
0  语文  99
1  数学  99
2  英文  99
3  物理  88
4  化学  88
'''