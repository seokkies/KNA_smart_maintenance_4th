#실습 1
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
PROC = ROOT / 'data' / '15_사출성형_공정.csv'
df = pd.read_csv(PROC)
print("원본:", df.shape)
rows_removed = df.dropna()
print("행 제거:", rows_removed.shape)
cols_removed = df.dropna(axis=1)
print("열 제거:", cols_removed.shape)
print()

#실습 2
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
PROC = ROOT / 'data' / '15_사출성형_공정.csv'

df = pd.read_csv(PROC)
print("all:", df.dropna(how='all').shape)
print("thresh20:", df.dropna(thresh=20).shape)
print("불량여부 결측치:", df["불량여부"].isna().sum())
target_clean = df.dropna(subset=["불량여부"])
print("정답 열 기준:", target_clean.shape)
sample = df.head(4).copy()
sample.loc[sample.index[3], "불량여부"] = pd.NA
train = sample.dropna(subset=["불량여부"])
confirm = sample[sample["불량여부"].isna()]
print("학습용:", train.shape)
print("확인용:", confirm.shape)
print()

#실습 3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
PROC = ROOT / 'data' / '15_사출성형_공정.csv'

df = pd.read_csv(PROC)
feature_cols = [
    col for col in df.columns
        if col not in ["측정시각", "불량여부", "사출기"]
]
print("공정변수 개수:", len(feature_cols))
missing_rate = df[feature_cols].isna().mean()
print("공정변수 결측률:")
print((missing_rate * 100).round(1))
remove_cols = missing_rate[missing_rate >= 0.4].index.tolist()
print("제거 대상:", remove_cols)
clean_df = df.drop(columns=remove_cols)
print("제거 후 크기:", clean_df.shape)
print("남은 열 이름:", clean_df.columns.tolist())
print()

#실습 4
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
PROC = ROOT / 'data' / '15_사출성형_공정.csv'

df = pd.read_csv(PROC)
original = df.copy()
rows_removed = df.dropna()
thresh20 = df.dropna(thresh=20)
total_rows = len(df)
def get_summary(data):
    rows = len(data)
    lost_rate = (total_rows - rows) / total_rows * 100
    defect_count = int(data["불량여부"].sum())
    defect_rate = data["불량여부"].mean() * 100

    return {
        "행 수": rows,
        "손실률(%)": round(lost_rate, 1),
        "불량 개수": defect_count,
        "불량 비율(%)": round(defect_rate, 1)
    }
summary = pd.DataFrame({
    "원본": get_summary(original),
    "기본 행 제거": get_summary(rows_removed),
    "thresh=20": get_summary(thresh20)
}).T

print(summary)