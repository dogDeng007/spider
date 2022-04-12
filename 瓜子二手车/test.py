import pandas as pd


def draw_cars():
    pd_data = pd.read_excel('多线程瓜子二手车666.xlsx')
    # print(pd_data.head())           # 打印前五行数据

    pd_data['汽车名称'] = pd_data['车辆概况'].map(lambda x: x.split(" ")[0])

    name = pd_data['汽车名称'].value_counts()
    name1 = name.index.tolist()  # 车龄年代分布
    name2 = name.tolist()  # 车龄年代分布数量
    print(name1)
    print(name2)


    pd_data.loc[:, '表显里程1'] = pd_data['表显里程'].str.replace('万公里', '').astype('float32')  # 去除 30 ’万公里‘
    pd_data['里程区间'] = pd.cut(pd_data['表显里程1'], [0, 2, 4, 6, 8, 10, 20], labels=['0-2', '2-4', '4-6', '6-8', '8-10', '>10'])
    mile = pd_data['里程区间'].value_counts()
    mile1 = mile.index.tolist()  # 变速箱种类
    mile2 = mile.tolist()  # 变速箱种类对应数量'''
    #print(mile1)
    #print(mile2)
    '''
    ['4-6', '6-8', '2-4', '8-10', '>10', '0-2']
    [415, 374, 351, 261, 243, 176]
    '''


    pd_data = pd_data.dropna(subset=['最低首付'])                 # 删除空格
    pd_data['价格区间'] = pd.cut(pd_data['最低首付'], [0, 3, 5, 8,10, 15], labels=['0-3', '3-5', '5-8', '8-10', '>10'])
    price = pd_data['价格区间'].value_counts()
    price1 = price.index.tolist()  # 变速箱种类
    price2 = price.tolist()  # 变速箱种类对应数量'''
    #print(price1)
    #print(price2)
    '''
    ['0-3', '3-5', '5-8', '8-10', '>10']
    [859, 491, 199, 62, 33]
    '''



    tras = pd_data['过户情况'].value_counts()
    tras1 = tras.index.tolist()  # 变速箱种类
    tras2 = tras.tolist()  # 变速箱种类对应数量
    #print(tras1)
    #print(tras2)
    '''
    ['0次过户', '1次过户', '2次过户', '3次过户', '4次过户', '5次过户', '6次过户', '8次过户', '10次过户', '14次过户']
    [851, 811, 159, 80, 32, 13, 4, 1, 1, 1]
    '''


    disp = pd_data['汽车排量'].value_counts()
    disp1 = disp.index.tolist()  # 变速箱种类
    disp2 = disp.tolist()  # 变速箱种类对应数量
    #print(disp1)
    #print(disp2)
    '''
    ['1.6L', '2.0T', '1.5L', '2.0L', '1.5T', '1.4T', '1.8L', '1.6T', '1.8T', '1.4L', '2.4L', '2.5L', '1.2T', '1.3T', '3.0T', '1.3L', '2.7L', '3.0L', '1.0L', '1.0T', '1.2L', '3.6L', '3.5L', '2.3L', '2.3T', '2.8L', '2.7T', '2.4T', '0.9T', '3.6T']
    [342, 296, 292, 207, 149, 129, 90, 88, 71, 60, 45, 40, 33, 16, 15, 14, 10, 9, 9, 8, 7, 3, 3, 3, 3, 1, 1, 1, 1, 1]
    '''



    chg = pd_data['变速箱'].value_counts()
    chg1 = chg.index.tolist()  # 变速箱种类
    chg2 = chg.tolist()  # 变速箱种类对应数量
    #print(chg1)
    #print(chg2)
    '''
    ['自动', '手动']
    [1731, 216]
    '''


    age = pd_data['车龄'].value_counts()
    age1 = age.index.tolist()  # 车龄年代分布
    age2 = age.tolist()  # 车龄年代分布数量
    #print(age1)
    #print(age2)
    '''
    ['2016年', '2017年', '2018年', '2015年', '2014年', '2019年', '2013年', '2012年', '2020年', '2011年', '2021年', '2010年', '2009年', '2007年']
    [339, 273, 244, 239, 203, 200, 136, 101, 88, 77, 26, 21, 12, 1]
    '''



    pd_data.to_excel('多线程瓜子二手车777.xlsx')

if __name__ == '__main__':
    draw_cars()



'''
df = pd.read_excel('test.xlsx')

df.loc[:, '年龄666'] = df['年龄'].str.replace('元', '').astype('int32')  #去除 30  元
df['姓名1'] = df['姓名'].map(lambda x: x.split(" ")[1])
df=df.dropna(subset=['测试'])

print(df)

df.to_excel('out.xlsx',sheet_name="sheetname",index=False)


pd_data['价格区间'] = pd.cut(pd_data['年龄'], [0,5,10,15], labels=['0-5','5-10','10-15'])
x = pd_data['价格区间'].value_counts()
x1 = x.index.tolist()  # 变速箱种类
x2 = x.tolist()        # 变速箱种类对应数量'''



