import json
from icecream import ic
import requests
import prettytable as pt

# 闯入url
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=2&n=10&w=许嵩'
# 获取浏览器响应
resp = requests.get(url)
# 转json格式数据
json_text = json.loads(resp.text[9:-1])
# 获取所有音乐列表
song_list = json_text['data']['song']['list']
music_list = []
tb = pt.PrettyTable()
tb.field_names = ['序号', '歌名', '歌手', '专辑']
count = 0
# 格式化输出
for song in song_list:
    # 歌曲名称
    songname = song['songname']
    # 歌曲id
    songmid = song['songmid']
    # 歌手名称
    singer = song['singer'][0]['name']
    # 专辑名称
    albumname = song['albumname']
    print(songname, singer, albumname)
    tb.add_row([count, songname, singer, albumname])
    music_list.append([songmid, songname, singer])
    count += 1
print(tb)

# 下载音乐
while True:
    input_index = int(input('请输入你要下载歌曲的(-1退出)序号:'))
    if input == -1:
        break
    download_info = music_list[input_index]
    print(download_info)
