x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

print(list(zip(x, y, z)))
'''
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
'''

'''
grade_list = [656, 602, 610, 618, 663, 695, 622, 645, 677, 640]  # 10名600分以上的学生成绩列表
# 升序列表: [602, 610, 618, 622, 640, 645, 656, 663, 677, 695]
print(f"升序列表: {sorted(grade_list)}")  # 升序排序
# 降序列表: [695, 677, 663, 656, 645, 640, 622, 618, 610, 602]
print(f"降序列表: {sorted(grade_list, reverse=True)}")  # 降序排序


#字符串反转
str1 = '人生短短几个秋啊'
rev_str = list(reversed(str1))
print(str1)
print(''.join(rev_str))

# 列表反转
list1 = list(range(5,11))
rev_list = list(reversed(list1))
print(list1)
print(rev_list)
'''
[5, 6, 7, 8, 9, 10]
[10, 9, 8, 7, 6, 5]
'''

tuple1 = tuple(range(1,6))
rev_tup = tuple(reversed(tuple1))
print(tuple1)
print(rev_tup)
'''
(1, 2, 3, 4, 5)
(5, 4, 3, 2, 1)
'''

from functools import reduce
# 求0-100之和
def add(x, y):
    return x+y

sum = reduce(add, range(1, 101))
print(sum)
5050



def if_odd(n):
    return n % 2 == 1

odd_list = list(filter(if_odd, [8, 9, 7, 5, 7, 6, 2, 4, 3]))
print(odd_list)
[9, 7, 5, 7, 3]

# 求平方
def square(x):
    return x*x

new_list = list(map(square, [8, 9, 7, 5, 7, 6, 2, 4, 3]))
print(new_list)


new_list1 = list(map(lambda x:x*x, [8, 9, 7, 5, 7, 6, 2, 4, 3]))
print(new_list1)

[64, 81, 49, 25, 49, 36, 4, 16, 9]
'''

'''
[9, 7, 5, 7, 3]
'''

'''
# 找出成绩大于等于80的学生
score = [80, 81, 72, 75, 98, 79, 88]
result = [x for x in score if x >= 80]
print('成绩大于等于80的学生：', result)

成绩大于等于80的学生： [80, 81, 98, 88]


# 求圆面积

import random
# 生成10-100之间的随机列表
list  = [random.randint(10, 100) for x in range(10)]
print(list)

[83, 95, 16, 43, 66, 24, 11, 92, 38, 85]

import math
r = 10
result = lambda r:math.pi*r*r
print('圆面积为：', result(r))
圆面积为： 314.1592653589793
'''

