'''
1. 定义一个列表，并按照降序排序
'''
import operator
import random
test_list = random.sample(range(100, 1000), 10)
print('排序前：', test_list)

sort_list = sorted(test_list, reverse=True)
print('排序后：', sort_list)


'''
2. 判断是否为偶数（分别用普通函数和匿名函数实现）
'''
test_list = random.sample(range(10, 100), 5)
print(test_list)
for i in test_list:
    if i%2 == 0:
        print('True')
    else:
        print('False')

require_test = [x%2 == 0 for x in test_list]
print(require_test)

'''
3. 如何使用匿名函数对字典中的列表进行排序
'''

test_list = [{'name':'zs', 'age':20}, {'name':'ls', 'age':19}]
print(sorted(test_list, key=operator.itemgetter('age'), reverse=False))




