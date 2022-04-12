import requests
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}

params = {
    'num': 'YUBAO34E',
    'offset': 0,
    'limit': 2000
}

url = 'https://www.hurun.net/zh-CN/Rank/HsRankDetailsList'
page_text = requests.get(url=url, headers=headers, params=params).json()


df = pd.DataFrame(
        columns=['gender',
        'brithday',
        'age',
        'name',
        'photo',
        'birth_place',
        'permanent_China',
        'rank',
        'rank_change',
        'rich_wealth',
        'rich_wealth_change',
        'rich_comName_cn',
        'rich_industry_cn'])
for info in page_text['rows']:
    gender = info['hs_Character'][0]['hs_Character_Gender']
    brithday = info['hs_Character'][0]['hs_Character_Birthday']
    age = info['hs_Character'][0]['hs_Character_Age']
    name = info['hs_Character'][0]['hs_Character_Fullname_Cn']
    photo = info['hs_Character'][0]['hs_Character_Photo']
    birth_place = info['hs_Character'][0]['hs_Character_BirthPlace_Cn']
    permanent_China = info['hs_Character'][0]['hs_Character_Permanent_Cn']
    rank = info['hs_Rank_Rich_Ranking']
    rank_change = info['hs_Rank_Rich_Ranking_Change']
    rich_wealth = info['hs_Rank_Rich_Wealth']
    rich_wealth_change = info['hs_Rank_Rich_Wealth_Change']
    rich_comName_cn = info['hs_Rank_Rich_ComName_Cn']
    rich_industry_cn = info['hs_Rank_Rich_Industry_Cn']

    df.loc[len(df) + 1,:] = [gender, brithday, age, name, photo, birth_place, permanent_China, rank, rank_change, rich_wealth, rich_wealth_change, rich_comName_cn, rich_industry_cn]
print(df)
df['birth_place_split'] = df['birth_place'].str.split('-')
df['birth_place_split'] = df['birth_place_split'].apply(lambda x:'' if len(x) == 1 else x[1])
df['photo_split'] = df['photo'].apply(lambda x:x.split('/')[-1])
print(df.head())
df.to_csv('rich.csv', index=False)