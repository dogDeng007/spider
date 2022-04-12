import os
import requests
import re

from selenium import webdriver
import time

save_file = r'抖音短视频\\'
# 文件保存路径
if not os.path.exists(save_file):
    os.mkdir(save_file)

def change_title(title):
    pattern = re.compile(r'[\/\\\:\*\?\"\<\>\|]')
    new_title = re.sub(pattern, '_', title)
    return new_title


# 页面滑动函数
def drop_down():
    for page in range(1, 100, 4):
        time.sleep(1)
        j = page/9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' %j
        driver.execute_script(js)

# 加载驱动
driver = webdriver.Chrome()
# 打开目标网址
driver.get('https://www.douyin.com/user/MS4wLjABAAAADuTJkeJeDbKDjdbwNeB8bP81pVX_MWRnncAbPyu2DiE')
# 延迟三秒打开页面
time.sleep(3)
# 调用自动下滑函数
drop_down()

lis = driver.find_elements_by_css_selector('div._927ae3b0dd790b5b62eae61c7d2fa0bc-scss > div:nth-child(2) > ul li')
for li in lis:
    li_url = li.find_element_by_css_selector('a').get_attribute('href')
    #print(li_url)

    # 1. 发送请求
    headers = {
        'Referer': 'https://www.douyin.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4651.0 Safari/537.36',
        'cookie': 'ttwid=1%7Cy07zoYkoxh90nEDN0p46kPksuWyfQRvWojXibL1Mecc%7C1634437652%7C7a03eab7646b1dece5830e3ddd3d7d62ada886079ffb431640d58afe006ed2c4; _tea_utm_cache_6383=undefined; douyin.com; MONITOR_WEB_ID=09929d96-a1aa-422b-949e-8a4b87b58f21; passport_csrf_token_default=5cfabdc8a6737d87e9aa41c6c6877832; passport_csrf_token=5cfabdc8a6737d87e9aa41c6c6877832; _tea_utm_cache_1300=undefined; s_v_web_id=verify_kuulzc63_0o8IxtyR_8ed9_400b_8ktm_mWgwaCUm0unt; ttcid=38ca27dbd3d542b884be6602edd09da318; n_mh=T2Dx4H8f55qitmdWxyat0ydvyKjlAouuMm_W9Cp3Dt8; sso_uid_tt=cfb72ba9598bff9352828a60e3fe932f; sso_uid_tt_ss=cfb72ba9598bff9352828a60e3fe932f; toutiao_sso_user=29ef6859fb47e959e9e44e04244716d0; toutiao_sso_user_ss=29ef6859fb47e959e9e44e04244716d0; odin_tt=27426051f7a717325d01a5b1e6de067ca1e77754ccde8ac5d01ab46d78d651d5d086594fc68ef0b2003b7149752e391a85551c21abeaf1dd1be47ed96e2e2502; passport_auth_status_ss=236a0c6330546e8e55c22d3db7013446%2C; sid_guard=c5302d49f9d884bb29753fbc3058d50f%7C1634437703%7C5183999%7CThu%2C+16-Dec-2021+02%3A28%3A22+GMT; uid_tt=3d2a41afbc2b9db9e00a230fbe5a25c9; uid_tt_ss=3d2a41afbc2b9db9e00a230fbe5a25c9; sid_tt=c5302d49f9d884bb29753fbc3058d50f; sessionid=c5302d49f9d884bb29753fbc3058d50f; sessionid_ss=c5302d49f9d884bb29753fbc3058d50f; sid_ucp_v1=1.0.0-KDhjNjVhNDdlMDVjZTVhODNkYWI3ZjkwNzRmYmE1NTlkYjZhOGViZWIKFwi3iJCHnYyUARDHlK6LBhjvMTgGQPQHGgJscSIgYzUzMDJkNDlmOWQ4ODRiYjI5NzUzZmJjMzA1OGQ1MGY; ssid_ucp_v1=1.0.0-KDhjNjVhNDdlMDVjZTVhODNkYWI3ZjkwNzRmYmE1NTlkYjZhOGViZWIKFwi3iJCHnYyUARDHlK6LBhjvMTgGQPQHGgJscSIgYzUzMDJkNDlmOWQ4ODRiYjI5NzUzZmJjMzA1OGQ1MGY; passport_auth_status=236a0c6330546e8e55c22d3db7013446%2C; FOLLOW_YELLOW_POINT_USER=MS4wLjABAAAA6ZQ5xEpEBo8tspMAC7ehXEcHs7JybDRoyOQcEKaKMXI; FOLLOW_YELLOW_POINT_STATUE_INFO=1%2F1634470738878; __ac_nonce=0616c06b2005ed9a5632c; __ac_signature=_02B4Z6wo00f01ZnqTEwAAIDA-uCMJvP7NJWZzkjAAAcXE4YuvsWFv3wiF3TJO-s7WL5tp2CUupZDFmQqhK6ySy4EYKpeboqmefiuMuI3yfWitSlNmX1UoEAIhufR0gVqpXmJruGF4Ef72ZyGe0; msToken=aBPLK2LYEfdc4C3i_mx9JKzoA_PFxDDSDkBds2_9WnczlzmUp7iJqh4CfIvP8mshpsHoJ8z49QMTIFmo1Y-1_fs2Am4AS1lnYEvNOnYhODSdfRT2vY4nTIKL; tt_scid=cuKv4W7ln1d.N5a5GA8CK2WVzRDdkBdxg-MQ05JR-f--9wDNugz-qUPl7c7REHOP74ac; msToken=UOTNJ7Pqv9YU9AFpN47U3UlvWw3204vsYiJ79MprL8TgK6sIvJ44vKe6GjAluKkwEitlMdNMqkptO8ocGEfFR7-YpnubRYUcIvW4Tmll5yBubJnGrMdFRA=='
    }

    # 2.获取数据
    resp = requests.get(li_url, headers = headers)

    # 3.解析数据
    title = re.findall('<title data-react-helmet="true">(.*?)</title>', resp.text)[0]
    href = re.findall('src(.*?)%3D%22', resp.text)[1]
    video_url = requests.utils.unquote(href).replace('":"', 'https:')  # 解码

    #video_url = requests.utils.quote(href)  编码

    # 4.保存数据
    video_content = requests.get(url=video_url).content
    new_title = change_title(title)
    with open(save_file + new_title + '.mp4', mode='wb') as fin:
        fin.write(video_content)
        print(title+'.mp4文件下载完成！！')