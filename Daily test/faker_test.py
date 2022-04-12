'''
pip install faker
'''
from faker import Faker
fake = Faker(locale = 'zh_CN')

# 生成5条个人信息
for i in range(5):
    print(f'第{i+1}个人信息如下：', fake.profile())

'''
第1个人信息如下： {'job': '工长', 'company': '菊风公司网络有限公司', 'ssn': '530112194208099250', 'residence': '天津市婷县东城沈阳路Y座 395802', 'current_location': (Decimal('-44.750624'), Decimal('74.315880')), 'blood_group': 'A-', 'website': ['https://www.nl.com/', 'http://chen.cn/', 'https://www.lilin.cn/'], 'username': 'lichao', 'name': '詹红梅', 'sex': 'F', 'address': '湖北省呼和浩特县南湖成都路u座 255339', 'mail': 'xiulan06@hotmail.com', 'birthdate': datetime.date(1993, 6, 13)}
第2个人信息如下： {'job': '医疗器械销售代表', 'company': '天开信息有限公司', 'ssn': '13013219490419544X', 'residence': '内蒙古自治区娟县海陵刘街G座 529004', 'current_location': (Decimal('3.907486'), Decimal('93.448971')), 'blood_group': 'O-', 'website': ['http://www.tao.cn/', 'https://www.cuiqiu.cn/', 'http://qiangxia.cn/', 'http://www.pingjing.cn/'], 'username': 'gangfang', 'name': '何秀芳', 'sex': 'F', 'address': '重庆市贵阳县清城哈尔滨路i座 171613', 'mail': 'songqiang@gmail.com', 'birthdate': datetime.date(1974, 2, 10)}
第3个人信息如下： {'job': '旅游产品销售', 'company': '巨奥科技有限公司', 'ssn': '433101195306163505', 'residence': '重庆市上海市友好赵街B座 871399', 'current_location': (Decimal('-16.599713'), Decimal('66.806667')), 'blood_group': 'A-', 'website': ['https://www.jiangliao.cn/', 'https://jia.cn/', 'http://if.cn/', 'http://www.49.com/'], 'username': 'yangcao', 'name': '黄小红', 'sex': 'F', 'address': '江西省哈尔滨市花溪佛山路Z座 193056', 'mail': 'swen@hotmail.com', 'birthdate': datetime.date(1943, 6, 25)}
第4个人信息如下： {'job': '建筑制图/模型/渲染', 'company': '迪摩信息有限公司', 'ssn': '330204194112284564', 'residence': '澳门特别行政区文县滨城张路y座 987574', 'current_location': (Decimal('-56.3441425'), Decimal('19.279135')), 'blood_group': 'B-', 'website': ['http://www.juanli.cn/', 'http://www.io.com/', 'http://min.net/'], 'username': 'yan45', 'name': '楚伟', 'sex': 'F', 'address': '陕西省六安市门头沟潜江路I座 111666', 'mail': 'hhan@hotmail.com', 'birthdate': datetime.date(1964, 10, 10)}
第5个人信息如下： {'job': '生产主管', 'company': '商软冠联网络有限公司', 'ssn': '610800198205117557', 'residence': '新疆维吾尔自治区小红市花溪易路x座 483650', 'current_location': (Decimal('70.056298'), Decimal('-80.291666')), 'blood_group': 'A+', 'website': ['https://aq.cn/', 'http://www.chang.net/'], 'username': 'li77', 'name': '欧桂芝', 'sex': 'F', 'address': '福建省太原市沈北新合山路B座 440615', 'mail': 'leixiuying@yahoo.com', 'birthdate': datetime.date(2007, 6, 14)}
'''
