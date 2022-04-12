"""
[课程内容]: Python零基础之 QQ音乐爬虫

[课题介绍]：通过python程序，下载QQ音乐免费音乐和绿钻音乐

[授课老师]: 青灯教育-巳月

[上课时间]: 20:05

[第三方库]：
    requests >>> pip install requests
    prettytable >>> pip install PrettyTable

[开发环境]：
    版  本：python 3.8
    编辑器：pycharm 2021.2

先听一下歌, 等一下后面进来的同学, 20:05开始讲课 有什么喜欢听的歌 也可以发在公屏上

[没听懂?]
课后的回放录播资料找木子老师微信: python10010
+python安装包 安装教程视频
+pycharm 社区版  专业版 及 激活码免费

课前赠送资料, 网站合计/接口/开发者工具的使用

案例实现的思路分析:
    一. 搜索功能
    二. 下载歌曲功能

代码实现流程:
    发送请求 >>> 获取数据 >>> 解析数据 >>> 保存数据
    搜索功能
        1. 发送请求 向以前的搜索功能接口发送 请求
        2. 获取数据 获取所有歌曲信息数据
        3. 解析数据 歌曲 歌手名 专辑 歌曲mid(用来下载歌曲必须要的参数)
        4. 格式化输出
    下载歌曲功能
        1. 通过获取的歌曲mid 拼接 需要的音乐url
        2. 发送网络请求 需要的音乐url
        3. 获取数据 获取 里面生成的 部分音乐链接 合并 (mp3 数据所在的链接了)
        4. 发送请求 (mp3 数据所在的链接了)
        5. 获取数据 音乐二进制数据
        6. 保存数据
"""
import time

import requests  # 发送网络请求
import json
import prettytable as pt
from icecream import ic
from tqdm import tqdm

name = input('请输入你想要下载的歌曲或者歌手名称:')

# 1. 发送请求
url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w={name}'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4878.0 Safari/537.36',
    'referer': 'https://y.qq.com/',
    'cookie': 'tvfe_boss_uuid=f0542efb9d5afa8f; pgv_pvid=3513549893; fqm_pvqid=19f09c8f-6393-48c0-89a8-a66d66effba8; ts_uid=9619573218; ts_refer=www.baidu.com/; RK=SLMc/7yEXe; ptcz=04d244800864a7991e28ebbca4029cafeb59af3398b03a7d8e7d6a4270f5d566; tmeLoginType=2; euin=7KSz7wnlNenF; fqm_sessionid=5b834678-7e69-4ad7-af51-b76cbe2e95da; pgv_info=ssid=s457338140; _qpsvr_localtk=0.7189543215478622; ptui_loginuin=570607808; login_type=1; wxunionid=; psrf_qqunionid=19742D7970E1762A57C9DC853E39C0DD; wxrefresh_token=; wxopenid=; psrf_access_token_expiresAt=1654431564; psrf_qqopenid=B987B555BDFB0C5F783A7283EF15872F; psrf_musickey_createtime=1646655564; qqmusic_key=Q_H_L_5aiZQ1W8q7L4RQmM4nlPPBTYd2zcPnty6yx6KX11_CuOoqyWm1SAziA; qm_keyst=Q_H_L_5aiZQ1W8q7L4RQmM4nlPPBTYd2zcPnty6yx6KX11_CuOoqyWm1SAziA; psrf_qqrefresh_token=F2600C600F8EF65DF189F17C37813654; qm_keyst=Q_H_L_5aiZQ1W8q7L4RQmM4nlPPBTYd2zcPnty6yx6KX11_CuOoqyWm1SAziA; psrf_qqaccess_token=A052AFFC796679CE579ED06AF6B594C2; uin=570607808; ts_last=y.qq.com/n/ryqq/search'
}
# 2. 获取所有歌曲信息数据
response = requests.get(url).text

# 格式化json
json_str = response[9: -1]
json_dict = json.loads(json_str)

# 3. 解析数据 歌曲 歌手名 专辑 歌曲mid(用来下载歌曲必须要的参数)
song_list = json_dict['data']['song']['list']
tb = pt.PrettyTable()
tb.field_names = ['序号', '歌名', '歌手', '专辑']
music_info_list = []
count = 0
# 4. 格式化输出
for song in song_list:
    songname = song['songname']
    songmid = song['songmid']
    singer = song['singer'][0]['name']
    albumname = song['albumname']
    tb.add_row([count, songname, singer, albumname])
    music_info_list.append([songmid, songname, singer])
    count += 1
print(tb)

while True:
    input_index = eval(input('请输入你要下载的歌曲序号(-1)退出:'))
    if input_index == -1:
        break
    # 提取需要下载音乐的信息
    download_info = music_info_list[input_index]
    # 提取需要下载音乐的songmid
    songmid = download_info[0]
    # 1. 通过获取的歌曲mid 拼接 需要的音乐url
    music_info_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch", "filename":"M800","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","filename":"M800","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid
    # 2. 发送网络请求
    json_data = requests.get(url=music_info_url, headers=headers).json()
    # 3. 获取数据
    purl = json_data['req_0']['data']['midurlinfo'][0]['purl']
    # 拼接url
    media_url = 'https://dl.stream.qqmusic.qq.com/' + purl
    # 4. 发送请求 (mp3 数据所在的链接了)
    # 5. 获取数据 音乐二进制数据
    music_data = requests.get(media_url).content
    # 6. 保存数据
    with open(f'歌曲下载/{download_info[1]}-{download_info[2]}.mp3', mode='wb') as f:
        print('download......')
        for i in tqdm(range(0, 10)):
            f.write(music_data)
            time.sleep(0.05)
    print(f'{download_info[1]}, 下载完成!')