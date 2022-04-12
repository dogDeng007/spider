import os

print(os.listdir('E:\python\project++'))
'''
['.idea', 'college', 'Daily test', 'mult_xiangqin', 'pandas技巧', 'travel_summer', '动图获取', '匿名函数', '打针', '文件操作', '汉服小姐姐', '猫眼_动态网站', '王思聪语录', '瓜子二手车', '网易文胸', '腾讯招聘', '萌妹子', '虎牙']
'''



'''
print(os.getcwd())

E:\python\project++\文件操作
'''

'''
# 删除文件夹
os.rmdir('read.txt')
print('文件删除成功！')

文件删除成功！
'''



'''
# 删除文件
os.remove('new_read.txt')
print('删除成功！')

删除成功！

'''












'''
# 重命名文件
os.rename('read.txt', 'new_read.txt')
print('重命名成功！')


重命名成功！
'''
















'''
#1.只读模式打开文件
file = open('read1.txt')

# 2. 读取文件内容
text = file.read()
print(text)

# 3.关闭文件
file.close()


# 1.读写模式打开文件
f = open('img.png', 'rb')

# 2. 写入文件内容
for i in f:
    print(i)
print('代码执行结束！')

# 3.关闭文件
f.close()


代码执行结束！
'''