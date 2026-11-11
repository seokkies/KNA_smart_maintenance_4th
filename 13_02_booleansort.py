#실습 1
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
print(df.shape)
df1 = df[df["비스킷두께"] >= 16]
df2 = df[df["비스킷두께"] < 16]
print(df1.shape)
print(len(df1))
print(len(df2))
print(len(df1) + len(df2)) #결측치 제외 데이터 갯수 186 ->결측 14개
print(pd.isna(df["비스킷두께"]).sum()) #실제 결측 14개 확인
print()

#실습 2
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df1 = df[(df['비스킷두께']>= 16) & (df['사이클타임']>= 25)]
df2 = df[(df['비스킷두께']>= 16) | (df['사이클타임']>= 25)]
print("조건1:", len(df1), "조건2:", len(df2))
df3 = df[~(df["품질등급"] == "불량")]
print("불량이 아닌 행:", len(df3))
print()

#실습 3
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df1 = df[df["품질등급"].isin(["주의", "불량"])]
print("조건1:", len(df1))
df2 = df[df["비스킷두께"].between(10,16)]
print("조건2:", len(df2))
df3 = df[df["설비ID"].str.contains("A")]
df4 = df[(df["설비ID"].str.split('-').str[1] == "A") & (df["설비ID"].str.split('-').str[2] == "01")]
print("조건3:", len(df3), len(df4))
print()

#실습 4
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df1 = df.sort_values("비스킷두께", ascending=False).head(5)
print(df1)
df2 = df.sort_values(["품질등급", "사이클타임"], ascending=[True, False]).head(5)
print(df2)
print()

#실습 5
import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv")
df1 = df[(df["품질등급"] != "양품") & (df["비스킷두께"] >= 16)]
df2 = df1.sort_values("비스킷두께", ascending=False)
print("조건통과 줄 수:",len(df2))
print(df2.head(5))
df3 = df[(df["품질등급"] != "양품") & (df["비스킷두께"] < 16)]
df4 = df[(df["품질등급"] != "양품")] 
print("양품 아닌 결측치 수:", (len(df4) - (len(df3) + len(df2))))