'''
语文  88
数学  99
英语  77
物理  86
化学  89
'''

import pandas as pd

# Sereis->list
grades = {'语文':88, '数学':99, '英语':77, '物理':86, '化学':89}
data = pd.Series(data=grades)

subject = data.index.tolist()
score = data.tolist()

print(subject)
print(score)

'''
['语文', '数学', '英语', '物理', '化学']
[88, 99, 77, 86, 89]
'''