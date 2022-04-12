import cv2
import numpy as np

def read_pic():
    '''# 加载图片
    img = cv2.imread("./pic1.jpg")
    cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 获取图片尺寸
    img = cv2.imread("./pic1.jpg")
    h, w, ch = img.shape
    print('原图尺寸：', h, w, ch)

    new_h = int(h / 2)
    new_w = int(w / 2)

    res = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite('./half_pic1.jpg', res)

    # 获取图片尺寸
    img = cv2.imread("./half_pic1.jpg")
    h, w, ch = img.shape
    print('缩半原图尺寸：', h, w, ch)

    img = cv2.imread("./pic1.jpg")
    h, w, ch = img.shape
    print(h, w, ch)
    # (x0,y0) (x1,y1) 矩阵
    x0, y0 = 200, 80
    x1, y1 = 880, 960
    # img 是一个按行扫描的矩阵
    res = img[y0:y1, x0:x1]
    print('截取后 H,W=', res.shape[:2])
    cv2.imwrite('./pic.jpg', res)
'''
    # 读取原始图片
    image = cv2.imread('./pic1.jpg')
    (h, w) = image.shape[:2]
    print("SOURCE", image.shape)

    # 定义水印所在区域,矩形
    mask = np.zeros((h, w, 1), dtype=np.uint8)
    mask[909:943, 517:706] = np.ones((943 - 909, 706 - 517, 1), dtype=np.uint8) * 255

    # 去掉深色的像素 ， 140 是个魔术数，需要调参
    for y in range(909, 943):
        for x in range(517, 706):
            if sum(image[y, x]) / 3 < 140:
                mask[y, x] = (0)

    # 观察mask
    new_h = int(h / 2)
    new_w = int(w / 2)
    mask2 = cv2.resize(mask, (new_w, new_h))
    cv2.imshow('初始选区', mask2)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    mask = cv2.dilate(mask, kernel)

    mask2 = cv2.resize(mask, (new_w, new_h))
    cv2.imshow('膨胀后选区', mask2)
    cv2.waitKey(0)

    # 修复图片
    dst = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

    cv2.imwrite('./pic1_inp2.jpg', dst)

if __name__ == '__main__':
    read_pic()