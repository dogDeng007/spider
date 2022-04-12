import os
from pdf2docx import Converter

# 获取当前工作目录
file_path = os.getcwd()

# 遍历所有文件
for file in os.listdir(file_path):
    # 获取文件后缀
    suff_name = os.path.splitext(file)[1]

    # 过滤非pdf格式文件
    if suff_name != '.pdf':
        continue
    # 获取文件名称
    file_name = os.path.splitext(file)[0]
    # pdf文件名称
    pdf_name = os.getcwd() + '\\' + file
    # 要转换的docx文件名称
    docx_name = os.getcwd() + '\\' + file_name + '.docx'
    # 加载pdf文档
    cv = Converter(pdf_name)
    cv.convert(docx_name)
    cv.close()
