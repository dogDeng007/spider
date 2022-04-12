from MyQR import myqr

myqr.run(
    words='http://weixin.qq.com/r/ph1udgjEAlV9rUwV90i0',    # 二维码中的信息
    picture='8.gif',            # 二维码的图片
    colorized=True,            # 设置二维码是否有颜色
    save_name='81.gif'    # 输出的二维码图片
)