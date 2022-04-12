'''test_list = [88, 97, 91, 78, 14, 44, 86, 89, 99, 94, 41, 19, 36, 66, 16, 80, 45, 82, 39, 98, 82]

def is_duplicated(lst):
    for x in test_list:
        if lst.count(x) > 1:
            print(x, '重复次数：', lst.count(x))
            return True
    return False

print(is_duplicated(test_list))


def is_duplicated(lst):
    print(len(test_list) != len(set(lst)))
is_duplicated(test_list)
import random
test_list = random.sample(range(1, 10), 8)
print(test_list)


test_list = [123, 'xyz', 'zara', 'abc', 'xyz']
print(test_list)
new_list = test_list[::-1]
print(new_list)

[123, 'xyz', 'zara', 'abc', 'xyz']
['xyz', 'abc', 'zara', 'xyz', 123]

print(test_list)
# list.reverse() 这一步操作的返回值是一个None，其作用的结果，需要通过打印被作用的列表才可以查看出具体的效果。
test_list.reverse()
print(test_list)

[123, 'xyz', 'zara', 'abc', 'xyz']
['xyz', 'abc', 'zara', 'xyz', 123]


test_list = [14, 88, 97, 91, 78, 14, 44, 86, 89, 99, 94, 41, 19, 36, 66, 16, 80, 45, 82, 39, 98, 82, 14]

def find_deplicated(lst):
    result = []
    for x in test_list:
        if lst.count(x) > 1 and x not in result:
            result.append(x)
    return result
print(find_deplicated(test_list))

[14, 82]


def feibo(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + feibo(x[1:])

print(feibo([1, 1, 2, 3, 5]))

12


test_list = [14, 88, 97, 91, 78, 14, 44, 86, 89, 99, 94, 41, 19, 36, 66, 16, 80, 45, 82, 39, 98, 82, 14]

def max_data(lst):
    for x in lst:
        if x not in lst:
            return None
        else:
            return max(lst, key = lambda x: lst.count(x))

print(max_data(test_list))

14


test_list = [88, 97, 91, 78, 14, 44, 86, 89, 99, 94, 41, 19, 36, 66, 16, 80, 45, 82, 39, 98, 82, 14]
def head(lst):
    return lst[-1] if len(lst) > 0 else None

print(head(test_list))

14


for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j) + '*' + str(i) + '=' + str(j*i), end= '\t' )
    print()



def pair(x):
    return list(zip(x[:-1], x[1:]))

print(pair([5, 7, 9]))

[(5, 7), (7, 


from random import shuffle, randint
# 0 -100 抽取十位随机整数
lst = [randint(0, 100) for x in range(10)]
print(lst)
shuffle(lst)
print(lst)
'''
#代码功能是测试一下shuffle()函数
import random
number = []
for index in range(1, 11):
    number.append(index)
print(number)

random.shuffle(number)

for index in range(5):
    print(number[index])








