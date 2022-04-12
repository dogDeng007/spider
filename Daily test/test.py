from faker import Faker
from icecream import ic

# 实例化一个fake对象
fake = Faker('zh_CN')   #中文

# 打印20条信息
for i in range(20):
    name = fake.name()      # 姓名
    sfz = fake.ssn()       # 身份证号码
    phone = fake.phone_number()    # 手机号
    province = fake.province()      # 随机省份
    city = fake.city()      # 随即城市
    dis = fake.district()       # 随机地区

    ic(name)
    ic(sfz)
    ic(province)
    ic(province)
    ic(city)
    ic(dis)