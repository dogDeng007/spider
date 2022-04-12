import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from icecream import ic
import random

# 驱动加载
driver = webdriver.Chrome()

# 打开网站
driver.get('https://music.163.com/')

# 等待网页加载完成，不是死等；加载完成即可
driver.implicitly_wait(10)

# 查找并点击排行榜
#driver.find_element_by_xpath('//*[@id="g_nav2"]/div/ul/li[2]/a/em').click()

# 定位输入框并且输入搜索关键字
driver.find_element_by_css_selector('.txt.j-flag').send_keys('Linked')

# 点击搜索按钮
driver.find_element_by_css_selector('.txt.j-flag').send_keys(Keys.ENTER)  # 键盘事件

# 定位iframe
iframe = driver.find_element_by_xpath('//*[@id="g_iframe"]')

# 先进入到iframe
driver.switch_to.frame(iframe)

# 点击进入音乐
driver.find_element_by_css_selector('.s-fc7').click()

def spider_cmts():

    # 获取所有评论列表 div标签
    divs = driver.find_elements_by_css_selector('.cmmts.j-flag .itm')
    print(divs)

    for div in divs:
        user_name = div.find_element_by_css_selector('.cnt.f-brk a').text
        hot_cmts = div.find_element_by_css_selector('.cnt.f-brk').text.split('：')[1]
        cmts_time = div.find_element_by_css_selector('.time.s-fc4').text

        ic(user_name, hot_cmts, cmts_time)

for page in range(1, 5+1):
    print(f'-----------------正在抓取第{page}页数据-----------------')
    time.sleep(random.random()*3) # 延时防止被反爬
    spider_cmts()

    # 点击翻页
    next_page = driver.find_element_by_css_selector('#auto-id-T7nSo92vCVHfrgXc')
    #next_page = driver.find_element_by_id('auto-id-T7nSo92vCVHfrgXc')
    if next_page:
        next_page.click()
    else:
        print('没有数据了~~')

# 退出浏览器
driver.quit()