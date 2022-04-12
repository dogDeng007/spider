import re
import pymysql
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
browser = webdriver.Chrome()
def get_one_page(name):
    '''获取单个页面'''
    print("-----------------------------------------------获取第一页-------------------------------------------------------")
    try:
        browser.get("https://www.taobao.com")
        input = WebDriverWait(browser, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        input.send_keys(name)
        button = WebDriverWait(browser, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")))
        button.click()
        pages = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
        print("----即将解析第一页信息----")
        get_info(name)
        print("----第一页信息解析完成----")
        return pages.text
    except TimeoutException:
        return get_one_page(name)
def get_next_page(page,name):
     """获取下一页"""
     print("---------------------------------------------------正在获取第{0}页----------------------------------------".format(page))
     try:
        input = WebDriverWait(browser, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        input.send_keys(page)
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        button.click()
        WebDriverWait(browser,10).until(
             EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page)))
        print("-----即将解析第{0}页信息-----".format(page))
        get_info(name)
        print("-----第{0}页信息解析完成-----".format(page))
     except TimeoutException:
        return get_next_page(page,name)
def get_info(name):
    """获取详情"""
    WebDriverWait(browser,20).until(EC.presence_of_element_located((
        By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
    text = browser.page_source
    html = pq(text)
    items = html('#mainsrp-itemlist .items .item').items()
    for item in items:
        data = []
        image = item.find(".pic .img").attr("data-src")
        price = item.find(".price").text().strip().replace("\n","")
        deal = item.find(".deal-cnt").text()[:-2]
        title = item.find(".title").text().strip()
        shop = item.find(".shop").text().strip()
        location = item.find(".location").text()
        data.append([shop, location, title, price, deal, image])
        for dt in data:
            save_to_mysql(dt,name)
def save_to_mysql(data,name):
    """存储到数据库"""
    db= pymysql.connect(host = "localhost",user = "root",password = "211314",port = 3306, db = "spiders",charset = "utf8")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS {0}(shop VARCHAR(20),location VARCHAR(10),title VARCHAR(255),price VARCHAR(20),deal VARCHAR(20), image VARCHAR(255))".format(name))
    sql = "INSERT INTO {0} values(%s,%s,%s,%s,%s,%s)".format(name)
    try:
        if cursor.execute(sql,data):
            db.commit()
            print("********已入库**********")
    except:
        print("#########入库失败#########")
        db.rollback()
    db.close()
def main(name):
    pages = get_one_page(name)
    pages = int(re.compile("(\d+)").findall(pages)[0])
    for page in range(1,pages+1):
       get_next_page(page,name)
if __name__ == '__main__':
    name = "男装"
    main(name)