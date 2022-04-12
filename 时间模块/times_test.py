import datetime
import time
from icecream import ic
from datetime import date

import datetime

# datetime.timedelta类
now = datetime.datetime.now()
# 获取当前时间
print(now)
# 获取30天后的时间
print(now + datetime.timedelta(days=30))
# 获取30天前的时间
print(now - datetime.timedelta(days=30))

'''
# datetime类型
now = datetime.datetime.now()
print(now, type(now))

today = datetime.datetime.today()
print(today, type(today))

# 转换成字符串
d1 = datetime.datetime.now().strftime('%Y/%m/%d')
print(d1,type(d1))


# 时间戳
ic(time.time())


# 时间字符串
ic(time.strftime('%Y/%m/%d %H:%M:%S'))


# 时间元组
ic(time.localtime())


# 今天的日期
#print(date.today())
'''
2021-11-16
'''

# 格式化时间
d1 = date(2021, 11, 16)
s = d1.isoformat()
'''
2021-11-17
'''


# 日历显示：(年，第几周，星期)
ic(d1.isocalendar())

# 获取星期(1~7)
ic(d1.isoweekday())

# 获取星期(0~6)
ic(d1.weekday())

# 格式化时间
ic(d1.strftime('%Y/%m/%d'))

# 时间戳转换为类似于元组的形式(localtime)
ic(d1.timetuple())'''