#실습 1

import pandas as pd  
df = pd.read_csv('data/13_diecasting_small.csv')
print(df["형체력"].head(3))
df1 = df[["형체력","실린더압력"]]
print(df1.shape, df1.dtypes)
print(df1["형체력"].shape, df1["형체력"].dtypes)
print()

#실습 2
import pandas as pd  
df = pd.read_csv('data/13_diecasting_small.csv')
print(df.loc[0, '샷'], df.iloc[0]['샷'])
df1 = df.sort_values('형체력', ascending=False)
print(df1.loc[0, '샷'], df1.iloc[0]['샷'])

#실습 3
import pandas as pd  
df = pd.read_csv('data/13_diecasting_small.csv')
print(df.columns) #['샷', '설비ID', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급']
df1 = df.iloc[0:5, [2,6]] # 5줄, [2,6]열
print(df1.head(5))
print(df1.shape)

#실습 4
import pandas as pd  
df = pd.read_csv('data/13_diecasting_shot.csv')
print(df.shape)
print(df.columns) #['샷', '설비ID', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급']
df1 = df.iloc[0:10, [1,5,7]]
print(df1.tail())
print(df1.shape)