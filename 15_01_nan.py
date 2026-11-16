#실습 1
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
LOG = DATA / "15_사출성형_로그.csv"

df = pd.read_csv(LOG)
print(df.shape)  # (16, 7)

print(df.isna().sum())
print("전체 결측치:", df.isna().sum().sum())

print("사출압력 0:", (df["사출압력"] == 0).sum())
print("스크루속도 -999:", (df["스크루속도"] == -999).sum())
print("배럴온도 999:", (df["배럴온도"] == 999).sum())
print()

#실습 2
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
PROC = DATA / '15_사출성형_공정.csv'
LOG = DATA / '15_사출성형_로그.csv'

df = pd.read_csv(PROC)
print("데이터 크기:", df.shape)
print(df.head(3))
df.info()
print(df["최대사출속도"].describe()[["count", "min", "max"]])
print()

#실습 3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
LOG = DATA / "15_사출성형_로그.csv"
log_raw = pd.read_csv(LOG)
print("기본 결측치:", log_raw.isna().sum().sum()) 
NA_RULES = {"배럴온도": [999], "스크루속도": [-999]}
log_clean = pd.read_csv(LOG, na_values=NA_RULES)
print("1차 변환 결측치:", log_clean.isna().sum().sum())  # 8개

NA_RULES["사출압력"] = [0]
log_clean = pd.read_csv(LOG, na_values=NA_RULES)
print("2차 변환 결측치:", log_clean.isna().sum().sum())  # 10개
print(log_clean.isna().sum())
print("정답 열 변화 없음:", log_raw["불량여부"].equals(log_clean["불량여부"]))
print()

#실습 4
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PROC = DATA / "15_사출성형_공정.csv"

df = pd.read_csv(PROC)
count = df.isna().sum()
ratio_pct = count / len(df) * 100
missing_summary = pd.DataFrame({"결측 개수": count, "결측 비율(%)": ratio_pct})
missing_summary = missing_summary[missing_summary["결측 개수"] > 0]
print(missing_summary.round(1))
print("결측 열 개수:", len(missing_summary))
print("전체 결측치:", int(count.sum()))
print()

# 실습 5
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PROC = DATA / "15_사출성형_공정.csv"

df = pd.read_csv(PROC)
missing_rate = (df.isna().mean() * 100).sort_values(ascending=False)
print("결측률 상위 3개 열:")
print(missing_rate.head(3).round(1))
row_missing = df.isna().sum(axis=1)
print("완전한 행:", int((row_missing == 0).sum()))
print("결측 있는 행:", int((row_missing > 0).sum()))
print("결측 5개 이상인 행:", int((row_missing >= 5).sum()))
print()

# 실습 6
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PROC = DATA / "15_사출성형_공정.csv"

df = pd.read_csv(PROC)
cols = ["최대사출속도", "감압시간"]
print(df[cols].isna().sum())
print(df[cols].isna().head(10))
both_missing = df["최대사출속도"].isna() & df["감압시간"].isna()
print("동시 결측 행:", int(both_missing.sum()))
print("동시 결측 비율:", round(both_missing.mean() * 100, 1), "%")
print(df.loc[both_missing, ["측정시각", "사출기"]])
one_missing = ((df["최대사출속도"].isna()) ^ (df["감압시간"].isna()))
print("한 열만 결측:", int(one_missing.sum()))
both_observed = (df["최대사출속도"].notna() & df["감압시간"].notna())
print("두 열 모두 관측:", int(both_observed.sum()))
print()