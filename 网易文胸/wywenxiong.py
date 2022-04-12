'''
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856130970&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=1&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856339147&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=2&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856354947&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=3&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
'''
import requests
import time, random
from faker import Faker
import pandas as pd
from icecream import ic

def spider_page():
    #url = 'http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856130970&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=1&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0'
    url = 'http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1636770025413&itemId=3991647&tag=%E5%85%A8%E9%83%A8&size=20&page=2&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0'
    headers = {
        'Cookie': 'yx_from=web_search_baidu; yx_aui=ada226e7-929f-419c-af99-53ad3eda94f0; mail_psc_fingerprint=01caf6305f28d3e4b8cfe162559acaac; yx_s_device=92db99a-a0c8-22cd-47c3-61d5b24664; yx_but_id=c18807c330874f4aaae2799cd51cdf9fd04f970cabedddc6_v1_nl; P_INFO=18392144506|1636766426|1|yanxuan_web|00&99|null&null&null#CN&null#10#0|&0||18392144506; yx_login_type=0; yx_user_login=true; yx_search_history=%5B%22%u68C9%u8884%u5973%22%2C%22%u7761%u8863%22%2C%22%u68C9%u8884%22%2C%22%u6587%u80F8%22%5D; _ntes_nuid=8b972d5bdb6dba81fd57ccfbac593c87; BAIDU_SSP_lcr=https://www.baidu.com/link?url=zyQS1ZWw9NX5Xw50muitOHx0kkWJG3WT51-8azp0ZDa&wd=&eqid=ca2a415f0000e3c900000005618f20af; _ntes_nnid=f1c2812145357d2b883902c65c421256,1636769976319; yx_delete_cookie_flag=true; yx_stat_seesionId=ada226e7-929f-419c-af99-53ad3eda94f01636769983423; yx_stat_ypmList=; yx_show_painted_egg_shell=false; yx_new_user_modal_show=1; yx_page_key_list=http%3A//you.163.com/search%3Fkeyword%3D%25E6%25A3%2589%25E8%25A2%2584%25E5%25A5%25B3%26timestamp%3D1636769989980%26_stat_search%3Dhistory%26searchWordSource%3D5%26_stat_referer%3Dindex%23page%3D1%26sortType%3D0%26descSorted%3Dtrue%26categoryId%3D0%26matchType%3D0%2Chttp%3A//you.163.com/item/detail%3Fid%3D3991647%26_stat_area%3D1%26_stat_referer%3Dsearch%26_stat_query%3D%25E6%25A3%2589%25E8%25A2%2584%25E5%25A5%25B3%26_stat_count%3D169%26_stat_searchversion%3Dmmoe_model-1.1.0-1.3; yx_stat_seqList=v_315469b8cb%7Cv_f72eac7e53%3B-1%3Bv_0e93fce746%3Bc_6b9da68e5d%3Bv_315469b8cb%3B-1',
        'Referer': 'http://you.163.com/item/detail?id=3987228&_stat_area=3&_stat_referer=search&_stat_query=%E6%96%87%E8%83%B8&_stat_count=132&_stat_searchversion=dcn_model-1.1.0-1.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.9 Safari/537.36'
    }

    resp = requests.get(url, headers = headers)

    if resp.status_code == 200:
        comts_List = resp.json()['data']['commentList']

        size = [item['skuInfo'][0] for item in comts_List]
        colors = [item['skuInfo'][1] for item in comts_List]
        times = [item['createTime'] for item in comts_List]
        for t in times:
            pass
        content_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t/1000))
        print(content_time)
        star = [item['star'] for item in comts_List]
        memberLevel = [item['memberLevel'] for item in comts_List]
        pic = [item['picList'] for item in comts_List]
        content = [item['content'] for item in comts_List]

        # 保存数据
        pd_data = pd.DataFrame({
            '尺码': size,
            '颜色': colors,
            '下单时间': content_time,
            '评分': star,
            '会员等级': memberLevel,
            '图片展示': pic,
            '评论': content
        })

        pd.set_option('display.max_columns', None)  # 显示完整的列
        pd.set_option('display.max_rows', None)  # 显示完整的行
        pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
        return pd_data

fake = Faker(locale='zh_CN')

# 获取多页
def get_all_page(all_page_num):
    # 存储表
    df_all = pd.DataFrame()
    # 循环页数
    for page in range(all_page_num):
        # 打印进度
        print(f'-------------正在获取第{page + 1}页的文胸信息-------------')
        # 调用函数
        pd_data = spider_page()
        # 追加
        df_all = df_all.append(pd_data, ignore_index=True)
        # 随机休眠
        time.sleep(random.random()*4)

    df_all.to_excel('网易文胸.xlsx', index=False)

if __name__ == '__main__':
    get_all_page(5)