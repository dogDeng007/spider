list1 = ['positibe', 'negtive', 'middle']
list2 = [3406, 1084, 12686]
print(list2)
print(type(list2))



import openpyxl as op

def op_toexcel(data,filename): # openpyxl库储存数据到excel
    wb = op.Workbook() # 创建工作簿对象
    ws = wb['Sheet'] # 创建子表
    ws.append(['词汇', '词频']) # 添加表头
    for i in range(len(data[0])):
        d = data[0][i], data[1][i]
        ws.append(d) # 每次写入一行
    wb.save(filename)

if __name__ == '__main__':
    data = [list1, list2]
    filename = 'b站.xlsx'
    op_toexcel(data, filename)






