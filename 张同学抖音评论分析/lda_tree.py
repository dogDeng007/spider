import json

from pyecharts import options as opts
from pyecharts.charts import Tree

def hold_topic(topic):
    i = 0
    res = ''
    while i < len(topic):
        res += topic[i: i+40]
        res += '\n'
        i += 40
    return res[0:-1]

data = []
data.append({'name': '张同学视频评论主题', 'children': []})

doc_f = open('./res/docs.txt', 'r', encoding='utf-8')
doc_json = json.loads(doc_f.readlines()[0].strip())

f = open('./res/topics.txt', 'r', encoding='utf-8')

for i, line in enumerate(f.readlines()):
    topic_arr = data[0]['children']
    topic = {}
    cols = line.strip().split(': ')
    holded_topic = hold_topic(cols[1])
    topic['name'] = f'{cols[0]}\n{holded_topic}'
    topic['children'] = []

    for doc in doc_json[str(i)]:
        cmt_case = {'name': doc}
        topic['children'].append(cmt_case)

    topic_arr.append(topic)

c = (
    Tree(init_opts=opts.InitOpts(width='1800px', height='2000px') )
    .add("", data, pos_right='100', pos_left='center')
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    .render("tree_base.html")
)