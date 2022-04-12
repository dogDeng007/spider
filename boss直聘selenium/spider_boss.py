# 导入模块
import csv
import random
import time
from icecream import ic
from selenium import webdriver
# 键盘绑定事件
from selenium.webdriver.common.keys import Keys
# 实例化浏览器对象
driver = webdriver.Chrome()

f = open('招聘1.xlsx', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '薪资',
    '公司名称',
    '公司信息',
    '经验要求',
    '标签',
    '福利',
])
# 写入表格
csv_writer.writeheader()

# 打开网址
driver.get('https://www.zhipin.com/c100010000/?query=python&ka=sel-city-100010000')
# 等待网页加载完成，不是死等；加载完成即可
driver.implicitly_wait(10)
# 定位输入框并且输入搜索关键字
#driver.find_element_by_xpath("//p[@class='ipt-wrap']/input[@class='ipt-search']")
#driver.find_element_by_css_selector('.ipt-search').send_keys('Python')
# 点击搜索按钮
#driver.find_element_by_css_selector('.btn.btn-search').click()  # 鼠标事件
#driver.find_element_by_css_selector('.btn.btn-search').send_keys(Keys.ENTER)  # 键盘事件
#driver.find_element_by_css_selector('#filter-box > div > div.condition-box > dl > dd > a:nth-child(3)').click()
# 等待网页加载完成
driver.implicitly_wait(10)

def spider_boss():
    # 获取数据内容
    lis = driver.find_elements_by_css_selector('.job-list ul li')  # 获取多个li标签加s
    print(lis) # 返回列表

    for li in lis:
        title = li.find_element_by_css_selector('.job-area-wrapper span').text
        salary = li.find_element_by_css_selector('.job-limit.clearfix span').text
        cop_name = li.find_element_by_css_selector('.name a').text
        cop_info = li.find_element_by_css_selector('.company-text p').text

        exprence = li.find_element_by_css_selector('.job-limit.clearfix p').text
        tags = li.find_element_by_css_selector('.tags span').text
        welfare = li.find_element_by_css_selector('.info-desc').text
        ic(title, salary, cop_name, cop_info, exprence, tags, welfare)
        dit = {
            '标题': title,
            '薪资': salary,
            '公司名称': cop_name,
            '公司信息': cop_info,
            '经验要求': exprence,
            '标签': tags,
            '福利': welfare,
        }
        csv_writer.writerow(dit)
for page in range(1, 5+1):
    print(f'-----------------正在抓取第{page}页数据-----------------')
    time.sleep(random.random()*3) # 延时防止被反爬
    spider_boss()
    # 点击翻页
    next_page = driver.find_element_by_css_selector('.next')
    if next_page:
        next_page.click()
    else:
        print('没有数据了~~')

# 退出浏览器
driver.quit()





