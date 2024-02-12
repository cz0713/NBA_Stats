import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
import requests
import time
import json
from pprint import pprint
from openpyxl import Workbook

stats_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=PTS"


r = requests.get(url=stats_url).json()
# pretty_r = json.dumps(r, indent=1)
# pprint(r)
table_headers = r['resultSet']['headers']
data = r['resultSet']['rowSet']

df1 = pd.DataFrame(data, columns=table_headers)
# print(df1.to_string())

df_cols = ['Year', 'Season Type'] + table_headers

season_types = ['Regular%20Season', 'Playoffs']
years = ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24']

df = pd.DataFrame(columns=df_cols)

for y in years:
    for s in season_types:
        stats_url = f"https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season={y}&SeasonType={s}&StatCategory=PTS"
        r = requests.get(url=stats_url).json()
        data = r['resultSet']['rowSet']

        temp_df1 = pd.DataFrame(data, columns=table_headers)
        temp_df2 = pd.DataFrame({'Year':[y for i in range(len(temp_df1))],
                                'Season Type':[s for i in range(len(temp_df1))]})
        temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
        df = pd.concat([df, temp_df3], axis=0)
        print(f'Finished scraping data for the {y} {s}')
        # lag = np.random.uniform(low=5, high=40)
        # time.sleep(lag)

print(df.to_string())
df.to_excel('nba_player_data.xlsx', index=False)
print("Process completed!")