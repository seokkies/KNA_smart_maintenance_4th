#실습 1
import pandas as pd

df = pd.read_csv("data/12_metro_compressor.csv")
print("파일 줄 수:",df.shape)
print(df.head())

#실습 2
df1 = df[["측정시각", "오일온도", "모터전류"]]
print("측정시각, 오일온도, 모터전류 줄 수:", df1.shape)
df2 = pd.read_csv("data/12_metro_compressor.csv", nrows=20)
print("nrow=20 줄 수:", df2.shape)

#실습 3
df = pd.read_csv("data/12_metro_compressor_semicolon.csv")
print(df.shape) # (200,1)로 하나의 열로 판정한다

df = pd.read_csv("data/12_metro_compressor_semicolon.csv",sep=";",encoding="utf-8")
print(df.shape) # (200,7)로 열 분류 완료

#실습 4
df = pd.read_csv("data/12_metro_compressor_semicolon.csv",sep=";",encoding="utf-8")
df1 = df[["측정시각", "오일온도", "모터전류"]].head(50)
print(df1.head(5))
print("df1 줄 수:", df1.shape)