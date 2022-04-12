import json

# emoji 表情在[]内
s = set()
with open('comments.txt') as f:
    for line in f.readlines():
        t = json.loads(line.strip())['text']

        s_idx = t.find('[')
        e_idx = t.find(']')
        # print(line, s_idx, e_idx)
        if 0 <= s_idx < e_idx:
            s.add(t[s_idx+1:e_idx])

print(s)