import random
from selenium import webdriver
from icecream import ic
import time
import csv

f = open('暖一杯茶.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '用户名称',
    '评论时间',
    '评论内容'
])
# 写入表格
csv_writer.writeheader()

# 驱动加载
driver = webdriver.Chrome()

# 打开网站
driver.get('https://music.163.com/#/song?id=1371780785')

# 等待网页加载完成，不是死等；加载完成即可
driver.implicitly_wait(10)

# 定位iframe
iframe = driver.find_element_by_css_selector('.g-iframe')

# 先进入到iframe
driver.switch_to.frame(iframe)

# 下拉页面到最底部
js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
driver.execute_script(js)

def spider_page():
    # 获取所有评论列表 div标签
    divs = driver.find_elements_by_css_selector('.itm')
    print(len(divs))

    for div in divs:
        user_name = div.find_element_by_css_selector('.cnt.f-brk a').text
        hot_cmts = div.find_element_by_css_selector('.cnt.f-brk').text.split('：')[1]
        cmts_time = div.find_element_by_css_selector('.time.s-fc4').text

        ic(user_name, hot_cmts, cmts_time)

        dit = {
            '用户名称': user_name,
            '评论时间': cmts_time,
            '评论内容': hot_cmts
        }
        csv_writer.writerow(dit)

for page in range(1, 300+1):
    print(f'-------------正在抓取第{page}页-------------')
    time.sleep(random.random() * 3)  # 延时防止被反爬
    spider_page()
    # 点击翻页
    driver.find_element_by_css_selector('.znxt').click()

# 退出浏览器
driver.quit()

