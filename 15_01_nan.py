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