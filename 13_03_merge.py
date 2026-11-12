#실습 1
import pandas as pd
df1 = pd.read_csv("data/13_diecasting_shot.csv")
df2 = pd.read_csv("data/13_diecasting_master.csv")
print(df1, df2) # 설비 ID 중복 
df3 = df1.merge(df2, on="설비ID")
print(df3.head(5).to_string(index=False))
print(df3.shape)
print()

#실습 2
import pandas as pd
df1 = pd.read_csv("data/13_diecasting_shot.csv")
df2 = pd.read_csv("data/13_diecasting_master.csv")
df3 = df1.merge(df2, how="inner")
df4 = df1.merge(df2, how="outer")
df5 = df1.merge(df2, how="left")
print("inner: ", len(df3))
print("left: ", len(df5))
print("outer: ", len(df4))
df6 = df1[(df1["설비ID"].str.split("-").str[1] == "C") & (df1["설비ID"].str.split("-").str[2] == "01")]
print("15행 차이나는 이유:", len(df6)) #DIE-C-01이 shot에만 존재하는 자료임
print(df4.tail(1)) #DIE-D-01 이 master에만 존재하므로 200 + 1 = 201개의 outer 줄수 존재

#실습 3
import pandas as pd
df = pd.read_csv("data/13_diecasting_shot.csv")
df1 = df.iloc[:100,:]
df2 = df.iloc[100:,:]
print(df1.shape, df2.shape)
# df3 = pd.concat([df1, df2]) 첫행 날아감
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)
print()

#실습 4
import pandas as pd
df1 = pd.read_csv("data/13_diecasting_shot.csv")
df2 = pd.read_csv("data/13_diecasting_master.csv")
df3 = df1.merge(df2, how="inner")
print(len(df3))
df3 = df3[df3["라인"].notna()]
df4 = df3[df3["품질등급"] != "양품"]
print(len(df4))
df5 = df4.sort_values("비스킷두께", ascending=False)
df6 = df5[["샷", "설비ID", "라인", "비스킷두께", "품질등급"]]
print(df6.head(5))