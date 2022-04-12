import time

from selenium import webdriver

# 驱动加载
driver = webdriver.Chrome()

# 打开网站
driver.get('https://music.163.com/')

# 查找并点击排行榜
driver.find_element_by_xpath('//*[@id="g_nav2"]/div/ul/li[2]/a/em').click()

# 定位iframe
iframe = driver.find_element_by_xpath('//*[@id="g_iframe"]')

# 先进入到iframe
driver.switch_to.frame(iframe)

# 点击音乐
#driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/div/div/div/span/a/b').click()
driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/div/div/a/img').click()

info_list = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]')
time.sleep(2)
print(info_list.text)


