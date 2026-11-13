#실습 1
import pandas as pd

df = pd.read_csv("data/14_hydraulic_qc.csv")
print(df["검사결과"].value_counts())
print(df.groupby("검사결과")["온도"].agg(["mean", "std", "max"]).round(2))
summary = df.groupby("검사결과").agg(평균온도=("온도", "mean"), 평균냉각효율=("냉각효율", "mean"), 측정수=("온도", "count"))
print(summary.round(2))
print()

#실습 2
import pandas as pd
df = pd.read_csv("data/14_hydraulic.csv")
marked = df.copy()
marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
marked["편차"] = marked["온도"] - marked["그룹평균"]
print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))
idx = marked["편차"].abs().idxmax()
print(marked.loc[idx, ["온도", "그룹평균", "편차"]].round(2))
temp_table = pd.pivot_table(
    df,
    index="밸브상태",
    columns="운전부하",
    values="온도",
    aggfunc="mean",
    margins=True,
    margins_name="전체"
)
print(temp_table.round(2))
print(pd.crosstab(df["냉각기상태"], df["운전부하"]))
print()

#실습 3
import pandas as pd
df = pd.read_csv("data/14_hydraulic.csv")
corr1 = df["온도"].corr(df["진동"]) # 온도와 진동의 상관계수
corr2 = df["온도"].corr(df["압력"])
corr3 = df["온도"].corr(df["냉각효율"])
print(round(corr1, 3), round(corr2, 3), round(corr3, 3)) # 0.931 0.284 -0.951 온도와 냉각효율이 강한 음의 상관관계
corr_table =  df[["온도", "진동", "압력", "냉각효율"]].corr()
print(corr_table.round(3))
print()

#실습 4
import pandas as pd
df = pd.read_csv("data/14_hydraulic_qc.csv")
sensor_cols = df.select_dtypes(include="number").columns.tolist()
corr_matrix = df[sensor_cols].corr()
rows = []

for i in range(len(sensor_cols)):
    for j in range(i + 1, len(sensor_cols)):
        a = sensor_cols[i]
        b = sensor_cols[j]

        rows.append({
            "지표1": a,
            "지표2": b,
            "상관계수": corr_matrix.loc[a, b]
        })

pair_table = pd.DataFrame(rows)
pair_table["절댓값"] = pair_table["상관계수"].abs()
print("전체 짝:", len(pair_table))
over_04 = pair_table[pair_table["절댓값"] >= 0.4]
print("0.4 이상:", len(over_04))
over_095 = pair_table[pair_table["절댓값"] >= 0.95]
print("0.95 이상:", len(over_095))
top5 = over_095.sort_values(
    "절댓값", ascending=False
).head(5)
print(top5.round(3))
print()

#실습 5
import pandas as pd

cycle = pd.read_csv("data/14_hydraulic.csv")
standard = pd.read_csv("data/14_hydraulic_std.csv")

print("기준표 중복 개수:", standard["냉각기상태"].duplicated().sum())
merged = pd.merge(cycle, standard, on="냉각기상태", how="left")
print("병합 결과:", merged.shape)
add_cols = ["상태설명","권장점검주기","담당팀","위험도"]
print("추가 열 결측치:")
print(merged[add_cols].isna().sum())
merged["온도구간"] = pd.cut(merged["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"], include_lowest=True)
print("온도 구간별 측정수:")
print(merged["온도구간"].value_counts().sort_index())
report = merged.groupby("온도구간", observed=False).agg(측정수=("온도", "count"), 평균온도=("온도", "mean"), 온도표준편차=("온도", "std"), 평균냉각효율=("냉각효율", "mean"), 평균위험도=("위험도", "mean"),
평균점검주기=("권장점검주기", "mean"))
print(report.round(2))

cross_table = pd.crosstab(merged["냉각기상태"], merged["온도구간"])
print("냉각기상태별 온도구간 교차표:")
print(cross_table)
corr_efficiency = merged["온도"].corr(merged["냉각효율"])
corr_vibration = merged["온도"].corr(merged["진동"])
print("온도와 냉각효율 상관계수:", round(corr_efficiency, 3))
print("온도와 진동 상관계수:", round(corr_vibration, 3))
report = merged.groupby("냉각기상태").agg(측정수=("온도", "count"), 평균온도=("온도", "mean"), 온도표준편차=("온도", "std"), 평균냉각효율=("냉각효율", "mean"), 위험도=("위험도", "first"),
    점검주기=("권장점검주기", "first"))

report = report.sort_values(["위험도", "평균온도"], ascending=[False, False])
print("설비 상태 진단표:")
print(report.round(2))
