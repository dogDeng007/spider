import pandas as pd

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据

pd_data = pd.read_excel('./测试.xlsx')
pd_data.loc[:, '表显里程new'] = pd_data['表显里程'].str.replace('万公里', '').astype('float32')    # 去除 30 ’万公里‘
print(pd_data.loc[:, '表显里程new'].round(1))

# 提取年份
#pd_data['month'] = pd_data['Date'].dt.month



'''
Year = pd.DatetimeIndex(pd_data['Date']).year
Month = pd.DatetimeIndex(pd_data['Date']).month
day = pd.DatetimeIndex(pd_data['Date']).day
pd_data.insert(0, 'Year', Year)
pd_data.insert(1, 'Month', Month)
pd_data.insert(2, 'day', day)


max_view_total = pd_data[pd_data['view_total'] == pd_data['view_total'].min()]
print(max_view_total)

pd_data1 = pd_data.copy()  # 生成一个副本, 防止数据损坏
pd_data['view_total'] = pd_data['view_total'].apply(lambda x: x[:-1])       # 通过匿名函数解决

pd_data['f985'] = pd_data['f985'].apply(lambda x: '是' if x == 1 else '否')       # 通过匿名函数解决
pd_data['f211'] = pd_data['f985'].apply(lambda x: '是' if x == 1 else '否')       # 通过匿名函数解决
print(pd_data)

# 统计不同过户次数车辆平均里程
pd_data.loc[:, '表显里程new'] = pd_data['表显里程'].str.replace('万公里', '').astype('float32')    # 去除 30 ’万公里‘
trans_mile = pd_data.groupby('过户情况')['表显里程new'].mean()
print(trans_mile.reset_index())

# 重命名
pd_data = pd_data.rename(columns = {'车辆概况':'车辆详情'})
print(pd_data)


# 找出在 过户情况 中所有'0次'的汽车
cars = pd_data[pd_data['过户情况'].str.contains('0次')]
print(cars.reset_index(drop=True))

pd_data.loc[:, '表显里程new'] = pd_data['表显里程'].str.replace('万公里', '').astype('float32')  # 去除 30 ’万公里‘
# 划分区间
pd_data['里程区间'] = pd.cut(pd_data['表显里程new'], [0, 2, 4, 6, 8, 10, 20],
                             labels=['0-2', '2-4', '4-6', '6-8', '8-10', '>10'])
mile = pd_data['里程区间'].value_counts()
mile1 = mile.index.tolist()         # 里程区间分类
mile2 = mile.tolist()               # 里程区间分类对应数量
print(mile1)
print(mile2)



# 对 汽车名称 这一列按照空格分割 并取第一个字符
pd_data['汽车名称'] = pd_data['车辆概况'].map(lambda x: x.split(" ")[0])
name = pd_data['汽车名称'].value_counts()
# 汽车名称分类
name1 = name.index.tolist()
# 汽车名称对应数量
name2 = name.tolist()
print(name1)
print(name2)

# 统计 过户分类 以及对应次数
trans_count = pd_data['过户情况'].value_counts()
# 针对于过户情况的分类
x1_data = trans_count.index.tolist()
x11_data = trans_count.index
x12_data = trans_count.index.values
# 类后各组数据的统计
x2_data = trans_count.tolist()
print('index.tolist():', x1_data)
print('index:', x11_data)
print('index.values:', x12_data)
print('x2:', x2_data)



#x1_data = x.index.tolist() #index, index.values, index.tolist()

# 找出在 车辆概况 中以'大众'开头的
cars = pd_data[pd_data['车辆概况'].str.startswith('大众')]


# 找出在 车辆概况 中以'豪华型'结尾的
cars = pd_data[pd_data['车辆概况'].str.endswith('豪华型')]
print(cars)


# 找出在 车辆概况 中包含'进口'的
cars = pd_data[pd_data['车辆概况'].str.contains('进口')]


# 多条件筛选数据
print(pd_data[(pd_data['车龄'] == '2018年') | (pd_data['变速箱'] == '自动')])

print(pd_data[['车辆概况', '全款价']])
# 查看头尾文件
print('头文件:', pd_data.head())
print('尾文件:', pd_data.tail())


# 如果有缺失值，删除此行
exist_col = pd_data.dropna()

# 统计缺失值个数
null_count = pd_data.isnull().sum()
print(null_count)


# 填充数据 我选择了8.888,你随意
pd_data.fillna(8.888, inplace=True)'''