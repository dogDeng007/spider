# 导入pdfplumber
import pdfplumber as pf
from icecream import ic
import pandas as pd

'''# 读取pdf文件，保存为pdf实例
pdf = pf.open('蔬菜.pdf')

# 访问第一页
first_page = pdf.pages[0]

# 自动读取表格信息，返回列表
table = first_page.extract_table()

# 将列表转为df
table_df = pd.DataFrame(table[1:], columns=table[0])

# 保存excel
table_df.to_excel('蔬菜.xlsx')
ic(table_df)

with pf.open("蔬菜.pdf") as p:
    for i in range(20):
        page = p.pages[i]
        textdata = page.extract_text()
        data = open('蔬菜.text', 'a')
        data.write(textdata)'''



#PDF转Word1import pdfplumber
from docx import Document
with pf.open("蔬菜.pdf") as p:
        page = p.pages[2]
        textdata = page.extract_text()
        # 新建一个空白的word文档
        document = Document()
        # 将变量textdata导进去
        content = document.add_paragraph(textdata)
        # 命名新建word文档
        document.save("蔬菜.docx")