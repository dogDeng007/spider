import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from icecream import ic
import random

# 数据存储
f = open('jd口罩2.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '价格',
    '评论数量',
    '店铺名称',
    '详情',
    '标签'
])
# 写入表格
csv_writer.writeheader()

# 驱动加载
driver = webdriver.Chrome()

# 打开网站
driver.get('https://www.jd.com/')

# 页面滑动函数
def drop_down():
    for page in range(1, 12, 2):
        time.sleep(1)
        j = page/9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' %j
        driver.execute_script(js)

# 等待网页加载完成，不是死等；加载完成即可
driver.implicitly_wait(10)

# 定位输入框并且输入搜索关键字
driver.find_element_by_css_selector('#key').send_keys('黑丝')
driver.find_element_by_css_selector('#key').send_keys(Keys.ENTER)
#driver.find_element_by_css_selector('.button').click()
driver.implicitly_wait(5)
drop_down()


def spider_page():
    # 获取所有的li标签
    lis = driver.find_elements_by_css_selector('.gl-item')

    for li in lis:
        title = li.find_element_by_css_selector('.p-name em').text.replace('\n', '')
        price = li.find_element_by_css_selector('.p-price strong i').text
        cmts_num = li.find_element_by_css_selector('.p-commit strong a').text
        shop_name = li.find_element_by_css_selector('.p-shop span a').text
        details = li.find_element_by_css_selector('.p-img a').get_attribute('href')
        icons = li.find_elements_by_css_selector('.p-icons i')
        icon = ','.join([x.text for x in icons])
        ic(title, price, cmts_num, shop_name, details, icon)

        dit = {
            '标题': title,
            '价格': price,
            '评论数量': cmts_num,
            '店铺名称': shop_name,
            '详情': details,
            '标签': icon
        }
        csv_writer.writerow(dit)

for page in range(1, 20+1):
    print(f'-----------------正在抓取第{page}页数据-----------------')
    time.sleep(random.random()*6) # 延时防止被反爬
    spider_page()

    # 点击翻页
    next_page = driver.find_element_by_css_selector('.pn-next').click()

driver.quit()