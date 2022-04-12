'''
动态猫眼票房
'''
import requests
from fake_useragent import UserAgent

# 获取信息
def spider_info():
    url = 'https://piaofang.maoyan.com/dashboard-ajax/movie?orderType=0&uuid=179f8c72776c8-0c35671867296b-5c4f2f15-1fa400-179f8c72776c8'
    headers = {
        'Cookie': '_lxsdk_cuid=179f8c72776c8-0c35671867296b-5c4f2f15-1fa400-179f8c72776c8; _lxsdk=F7933F80CA5711EBAC892B26EEC0B00924ED29BDF2F2491A9D76F87D6C9C3FA6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1623376472; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1623376504; __mta=256646836.1623376645061.1623377243341.1623377244495.9; _lxsdk_s=179f8c72777-402-19b-bf1%7C%7C36',
        'Referer': 'https://piaofang.maoyan.com/dashboard/movie',
        'User-Agent': str(UserAgent().random)
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            # print(resp.json())
            return resp.json()
        else:
            print('something wrong!')
    except:
        return None

# 提取信息
def parse_info(json):
    movies = json['movieList']['list']
    # print(movies)
    for item in movies:
        piaofang = {}
        piaofang['影片'] = item['movieInfo']['movieName']
        piaofang['上映时间'] = item['movieInfo']['releaseInfo']
        piaofang['综合票房'] = item['sumBoxDesc']
        piaofang['票房占比'] = item['boxRate']
        piaofang['排片场次'] = item['showCount']
        piaofang['排片占比'] = item['showCountRate']
        piaofang['场均人次'] = item['avgShowView']
        piaofang['上座率'] = item['avgSeatView']
        print(piaofang)
        # 利用生成器每次循环都返回一个数据
        yield piaofang

def save_infor(results):
    '''
    存储格式化的电影票房数据HTML文件
    :param results: 电影票房数据的生成器
    :return: None
    '''
    rows = ''
    for piaofang in results:
        # 利用Python中的format字符串填充html表格中的内容
        row = '<tr>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '<td class="text-center">{}</td>' \
              '</tr>'.format(piaofang['影片'],
                             piaofang['上映时间'],
                             piaofang['综合票房'],
                             piaofang['票房占比'],
                             piaofang['排片场次'],
                             piaofang['排片占比'],
                             piaofang['场均人次'],
                             piaofang['上座率'])
        # 利用字符串拼接循环存储每个格式化的电影票房信息
        rows = rows + '\n' + row
    # 利用字符串拼接处格式化的HTML页面
    piaofang_html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">  
        <script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
        <script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <style>
        body{
                height: 100%;
                width: 100%;
                background: url('./2.jpg') no-repeat;
                background-size: cover;
                position: absolute;
                overflow: hidden;
            }
        </style>
    <body>
    
    <table class="table table-hover">
        <h3 class="text-center">猫眼专业版-电影票房</h3>
        <thead>
            <tr>
            <th class="text-center" bgcolor="#7fff00">影片</th>
            <th class="text-center" bgcolor="#ff2a39">上映时间</th>
            <th class="text-center" bgcolor="#3420ff">综合票房</th>
            <th class="text-center" bgcolor="#ff33e0">票房占比</th>
            <th class="text-center" bgcolor="#ffebcd">排片场次</th>
            <th class="text-center" bgcolor="#1cfff0">排片占比</th>
            <th class="text-center" bgcolor="#fff38e">场均人次</th>
            <th class="text-center" bgcolor="#fffa27">上座率</th>
            </tr>
            ''' + rows + '''
        </thead>
    </table>
    
    </body>
    </html>
    '''
    # 存储已经格式化的html页面
    with open('piaofang.html', 'w', encoding='utf-8') as f:
        f.write(piaofang_html)

if __name__ == '__main__':
    # 获取信息
    json = spider_info()
    # 解析信息
    result = parse_info(json)
    # 保存信息
    save_infor(result)
