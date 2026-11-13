#실습 1
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")
print(df.shape) #(120, 8)
print(df["밸브상태"].value_counts(),df["밸브상태"].value_counts(normalize=True).round(3)) #정상 지연 경미 심각 91 20 20 19
print(df["운전부하"].value_counts(),df["운전부하"].value_counts(normalize=True).round(3))
print()

#실습 2
import pandas as pd

df = pd.read_csv("data/14_hydraulic_qc.csv")
print(df.shape) #(200, 11)
print(df["검사결과"].value_counts()) # 합격 188  불합격 12
pf = df["검사결과"].value_counts(normalize=True)
print(pf.round(3))
print(f"불합격 백분율 {pf["불합격"]*100}%")
print()

#실습 3
import pandas as pd
df = pd.read_csv("data/14_hydraulic.csv")
print("최대값:", df["진동"].max(), "최소값:", df["진동"].min())
df1 = df.copy()
df1.loc[df1["진동"] < 0.6, "이름표"] = "약함"
df1.loc[(df1["진동"] >= 0.6) & (df1["진동"] < 0.7), "이름표"] = "보통"
df1.loc[(df1["진동"] >= 0.7) & (df1["진동"] < 10), "이름표"] = "강함"
print(df1["이름표"].value_counts()) # 120개니깐 미지정값 없네용
print()

#실습 4
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")
print(df["냉각기상태"].value_counts())
means = df.groupby("냉각기상태")["온도"].mean()
print(means.round(2))
max_temp = df.groupby("냉각기상태")["온도"].max()
print("평균 차이:", round(means.loc["고장"] - means.loc["정상"], 2))
print()
#실습 5
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv")
total = df["밸브상태"].value_counts()
print("전체 건수")
print(total)
df1 = df[df["result"] == "고장"]
failure = df1["밸브상태"].value_counts()
print("고장 건수")
print(failure)
ratio = (failure / total).round(3)
print("고장 비율")
print(ratio)
print("고장 비율 최고:", ratio.idxmax())
print("최고 비율:", ratio.max())